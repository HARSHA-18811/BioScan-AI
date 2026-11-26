import React, { useState, useRef, useCallback } from 'react';
import { 
  UploadCloud, 
  FileCheck, 
  Trash2, 
  RefreshCw, 
  AlertTriangle, 
  Cpu, 
  CheckCircle, 
  FileQuestion,
  HelpCircle,
  Sparkles,
  Info
} from 'lucide-react';
import { api } from '../services/api';
import { AnalysisResponse, HealthStatus } from '../types';
import { SAMPLE_LEAVES, dataUriToFile, SampleLeaf } from '../utils/sampleImages';

interface AnalysisPageProps {
  health: HealthStatus | null;
  onAnalysisComplete: (result: AnalysisResponse) => void;
  onViewDemoNotice?: () => void;
}

export const AnalysisPage: React.FC<AnalysisPageProps> = ({ 
  health, 
  onAnalysisComplete 
}) => {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [previewUrl, setPreviewUrl] = useState<string | null>(null);
  const [isDragging, setIsDragging] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const [fileDetails, setFileDetails] = useState<{ size: string; name: string; type: string } | null>(null);
  
  const fileInputRef = useRef<HTMLInputElement>(null);

  const validateAndSetFile = (file: File) => {
    setErrorMessage(null);

    // Validate type
    const validTypes = ['image/jpeg', 'image/png', 'image/jpg'];
    if (!validTypes.includes(file.type.toLowerCase())) {
      setErrorMessage(`Invalid file format '${file.type || 'unknown'}'. Please upload a valid PNG or JPEG image.`);
      return false;
    }

    // Validate size (max 10MB)
    const maxBytes = 10 * 1024 * 1024;
    if (file.size > maxBytes) {
      setErrorMessage(`File size (${(file.size / (1024 * 1024)).toFixed(2)} MB) exceeds 10 MB limit.`);
      return false;
    }

    setSelectedFile(file);
    setFileDetails({
      name: file.name,
      size: `${(file.size / 1024).toFixed(1)} KB`,
      type: file.type
    });

    const url = URL.createObjectURL(file);
    setPreviewUrl(url);
    return true;
  };

  const handleDragOver = useCallback((e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(true);
  }, []);

  const handleDragLeave = useCallback((e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(false);
  }, []);

  const handleDrop = useCallback((e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(false);
    if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
      validateAndSetFile(e.dataTransfer.files[0]);
    }
  }, []);

  const handleFileInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files.length > 0) {
      validateAndSetFile(e.target.files[0]);
    }
  };

  const handleRemoveImage = () => {
    if (previewUrl) {
      URL.revokeObjectURL(previewUrl);
    }
    setSelectedFile(null);
    setPreviewUrl(null);
    setFileDetails(null);
    setErrorMessage(null);
    if (fileInputRef.current) {
      fileInputRef.current.value = '';
    }
  };

  const handleSelectSample = async (sample: SampleLeaf) => {
    try {
      setIsLoading(true);
      const file = await dataUriToFile(sample.dataUri, sample.filename);
      validateAndSetFile(file);
    } catch (err: any) {
      setErrorMessage(`Failed to load specimen: ${err.message}`);
    } finally {
      setIsLoading(false);
    }
  };

  const handleAnalyze = async () => {
    if (!selectedFile) return;

    setIsLoading(true);
    setErrorMessage(null);

    try {
      const response = await api.predictImage(selectedFile);
      onAnalysisComplete(response);
    } catch (err: any) {
      const msg = err.message || 'An error occurred during inference.';
      if (msg.includes('Failed to fetch') || msg.includes('NetworkError') || msg.includes('connect')) {
        setErrorMessage(
          "Unable to connect to the BioScan AI backend server. Please verify that the backend is running at http://127.0.0.1:8000 (run: python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 in the backend folder)."
        );
      } else {
        setErrorMessage(msg);
      }
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="max-w-4xl mx-auto px-4 py-8 space-y-8">
      {/* Title */}
      <div className="text-center space-y-2">
        <h1 className="text-3xl font-extrabold text-white tracking-tight">Foliar Image Analysis</h1>
        <p className="text-sm text-slate-400 max-w-xl mx-auto">
          Upload a leaf specimen photograph. BioScan AI will identify the leaf, diagnose potential diseases, and provide targeted treatment solutions.
        </p>
      </div>

      {/* Backend connection notice (only if backend is offline) */}
      {health === null && (
        <div className="p-3.5 rounded-xl bg-amber-500/10 border border-amber-500/30 flex items-center space-x-2.5 text-xs text-amber-200">
          <AlertTriangle className="w-4 h-4 text-amber-400 shrink-0" />
          <span>Connecting to backend server on <code className="bg-slate-900 px-1 py-0.5 rounded text-amber-300 font-mono">http://localhost:8000</code>... Make sure the FastAPI server is running.</span>
        </div>
      )}

      {/* Upload Box */}
      <div className="bg-slate-900/60 border border-slate-800 rounded-3xl p-6 sm:p-8 backdrop-blur-sm shadow-xl">
        {!previewUrl ? (
          <div
            onDragOver={handleDragOver}
            onDragLeave={handleDragLeave}
            onDrop={handleDrop}
            onClick={() => fileInputRef.current?.click()}
            className={`border-2 border-dashed rounded-2xl p-10 text-center cursor-pointer transition-all duration-200 ${
              isDragging
                ? 'border-teal-400 bg-teal-500/10 scale-[0.99]'
                : 'border-slate-700/80 hover:border-teal-500/50 hover:bg-slate-800/30'
            }`}
          >
            <input
              type="file"
              ref={fileInputRef}
              onChange={handleFileInputChange}
              accept=".jpg,.jpeg,.png,image/jpeg,image/png"
              className="hidden"
            />
            <div className="w-16 h-16 mx-auto mb-4 rounded-2xl bg-slate-800/80 border border-slate-700 flex items-center justify-center text-teal-400 group-hover:scale-110 transition-transform">
              <UploadCloud className="w-8 h-8" />
            </div>
            <h3 className="text-base font-semibold text-white mb-1">
              Drag & drop specimen photo, or <span className="text-teal-400 underline underline-offset-2">browse</span>
            </h3>
            <p className="text-xs text-slate-400 max-w-sm mx-auto mb-4">
              Supports JPEG and PNG leaf captures up to 10 MB. Ensure foliage is centered and well-lit.
            </p>
            <div className="inline-flex items-center space-x-3 text-[11px] font-mono text-slate-400 bg-slate-950/60 px-3 py-1.5 rounded-lg border border-slate-800">
              <span>RGB Color-space</span>
              <span>•</span>
              <span>224×224 Normalization</span>
              <span>•</span>
              <span>Format Header Verified</span>
            </div>
          </div>
        ) : (
          <div className="space-y-6">
            {/* Image Preview & Details */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6 items-center">
              <div className="relative rounded-2xl overflow-hidden bg-slate-950 border border-slate-800 flex items-center justify-center aspect-square max-h-72 mx-auto">
                <img
                  src={previewUrl}
                  alt="Specimen preview"
                  className="w-full h-full object-contain"
                />
                <div className="absolute top-2 right-2 px-2 py-1 bg-slate-950/80 backdrop-blur rounded text-[10px] font-mono text-teal-400 border border-slate-800">
                  Pre-inference Preview
                </div>
              </div>

              <div className="space-y-4">
                <div>
                  <h4 className="text-xs uppercase font-mono tracking-wider text-teal-400 font-semibold mb-1">
                    Specimen Details
                  </h4>
                  <p className="text-base font-semibold text-white break-all">{fileDetails?.name}</p>
                </div>

                <div className="grid grid-cols-2 gap-3 text-xs">
                  <div className="bg-slate-950 p-3 rounded-xl border border-slate-800">
                    <span className="text-slate-400 block mb-0.5">File Size</span>
                    <span className="font-mono text-white font-medium">{fileDetails?.size}</span>
                  </div>
                  <div className="bg-slate-950 p-3 rounded-xl border border-slate-800">
                    <span className="text-slate-400 block mb-0.5">MIME Type</span>
                    <span className="font-mono text-white font-medium">{fileDetails?.type}</span>
                  </div>
                </div>

                <div className="flex items-center space-x-3 pt-2">
                  <button
                    onClick={() => fileInputRef.current?.click()}
                    disabled={isLoading}
                    className="flex-1 px-4 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold flex items-center justify-center space-x-2 transition border border-slate-700"
                  >
                    <RefreshCw className="w-3.5 h-3.5" />
                    <span>Replace Image</span>
                  </button>
                  <button
                    onClick={handleRemoveImage}
                    disabled={isLoading}
                    className="px-4 py-2.5 rounded-xl bg-rose-500/10 hover:bg-rose-500/20 text-rose-400 text-xs font-semibold flex items-center justify-center space-x-2 transition border border-rose-500/30"
                  >
                    <Trash2 className="w-3.5 h-3.5" />
                    <span>Remove</span>
                  </button>
                </div>
              </div>
            </div>

            {/* Error Message */}
            {errorMessage && (
              <div className={`p-4 rounded-2xl flex items-start space-x-3.5 text-xs border transition-all ${
                errorMessage.includes('No plant leaf detected')
                  ? 'bg-amber-500/10 border-amber-500/40 text-amber-200 shadow-lg shadow-amber-500/5'
                  : 'bg-rose-500/10 border-rose-500/30 text-rose-200'
              }`}>
                <AlertTriangle className={`w-5 h-5 shrink-0 mt-0.5 ${
                  errorMessage.includes('No plant leaf detected') ? 'text-amber-400' : 'text-rose-400'
                }`} />
                <div className="space-y-1">
                  <div className="font-semibold text-sm">
                    {errorMessage.includes('No plant leaf detected') ? 'Specimen Verification Warning' : 'Inference Notice'}
                  </div>
                  <p className="leading-relaxed">{errorMessage}</p>
                  {errorMessage.includes('No plant leaf detected') && (
                    <div className="pt-1 text-[11px] text-amber-300/80 font-mono">
                      🍃 Tip: Please take or upload a clear, well-lit photo of a plant leaf or foliar tissue.
                    </div>
                  )}
                </div>
              </div>
            )}

            {/* Analyse Action Button */}
            <div className="pt-2">
              <button
                onClick={handleAnalyze}
                disabled={isLoading}
                className="w-full py-4 rounded-2xl bg-gradient-to-r from-teal-500 via-cyan-500 to-teal-500 text-slate-950 font-bold text-sm flex items-center justify-center space-x-2 shadow-lg shadow-teal-500/25 hover:shadow-cyan-500/40 hover:scale-[1.01] active:scale-[0.99] disabled:opacity-60 disabled:cursor-not-allowed transition-all duration-150"
              >
                {isLoading ? (
                  <>
                    <RefreshCw className="w-4 h-4 animate-spin" />
                    <span>Executing CNN Inference Pipeline...</span>
                  </>
                ) : (
                  <>
                    <Cpu className="w-4 h-4 stroke-[2.5]" />
                    <span>Analyse Leaf Specimen</span>
                  </>
                )}
              </button>
            </div>
          </div>
        )}
      </div>

      {/* Quick Scientific Calibration Specimens */}
      <div className="bg-slate-900/40 border border-slate-800 rounded-3xl p-6">
        <div className="flex items-center justify-between mb-4">
          <div className="flex items-center space-x-2">
            <Sparkles className="w-4 h-4 text-teal-400" />
            <h3 className="text-sm font-semibold text-white">Instant Research Specimens</h3>
          </div>
          <span className="text-[11px] font-mono text-slate-400">Click to load & test</span>
        </div>
        <p className="text-xs text-slate-400 mb-4">
          Don't have a leaf photo on hand? Select any synthesized calibration leaf from our foliar library to test the preprocessing and inference pipeline immediately:
        </p>

        <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-5 gap-3">
          {SAMPLE_LEAVES.map((sample) => (
            <button
              key={sample.id}
              onClick={() => handleSelectSample(sample)}
              disabled={isLoading}
              className="p-3 rounded-xl bg-slate-950/80 border border-slate-800 hover:border-teal-500/50 hover:bg-slate-900 text-left transition group"
            >
              <div className="w-full aspect-square rounded-lg bg-slate-900 mb-2 overflow-hidden flex items-center justify-center border border-slate-800">
                <img
                  src={sample.dataUri}
                  alt={sample.name}
                  className="w-16 h-16 object-contain group-hover:scale-110 transition-transform"
                />
              </div>
              <p className="text-[11px] font-semibold text-slate-200 truncate">{sample.name}</p>
              <p className="text-[10px] text-slate-400 font-mono truncate">{sample.plant}</p>
              <span className={`inline-block mt-1 text-[9px] px-1.5 py-0.5 rounded ${
                sample.isHealthy ? 'bg-emerald-500/15 text-emerald-400' : 'bg-amber-500/15 text-amber-400'
              }`}>
                {sample.isHealthy ? 'Healthy' : 'Symptomatic'}
              </span>
            </button>
          ))}
        </div>
      </div>
    </div>
  );
};
