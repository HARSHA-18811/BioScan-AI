import React, { useState } from 'react';
import { 
  CheckCircle2, 
  AlertTriangle, 
  ShieldAlert, 
  RefreshCw, 
  BarChart3, 
  Clock, 
  Leaf, 
  Bug, 
  Pill, 
  Droplets, 
  ShieldCheck, 
  Sparkles, 
  Check, 
  Info,
  FlaskConical,
  Sprout,
  Activity
} from 'lucide-react';
import { AnalysisResponse } from '../types';

interface ResultsPageProps {
  result: AnalysisResponse | null;
  onAnalyseAnother: () => void;
  onViewResearch: () => void;
}

export const ResultsPage: React.FC<ResultsPageProps> = ({ 
  result, 
  onAnalyseAnother, 
  onViewResearch 
}) => {
  const [activeTreatmentTab, setActiveTreatmentTab] = useState<'organic' | 'chemical' | 'prevention'>('organic');

  if (!result) {
    return (
      <div className="max-w-2xl mx-auto py-24 px-4 text-center space-y-4">
        <div className="w-16 h-16 mx-auto rounded-full bg-slate-900 border border-slate-800 flex items-center justify-center text-slate-500 shadow-inner">
          <Leaf className="w-8 h-8 text-teal-400" />
        </div>
        <h2 className="text-xl font-bold text-white">No Leaf Analysis Result Available</h2>
        <p className="text-xs text-slate-400 max-w-md mx-auto">
          Please upload and scan a leaf photo to identify the plant, diagnose potential diseases, and receive targeted treatment solutions.
        </p>
        <button
          onClick={onAnalyseAnother}
          className="px-6 py-2.5 rounded-xl bg-teal-500 text-slate-950 text-xs font-bold hover:bg-teal-400 shadow-lg shadow-teal-500/20 transition inline-flex items-center space-x-2"
        >
          <Leaf className="w-4 h-4" />
          <span>Upload Leaf Image</span>
        </button>
      </div>
    );
  }

  const confidencePct = (result.confidence * 100).toFixed(1);
  const details = result.pathological_details;
  const leafName = details.leaf_name || result.leaf_name || `${result.plant_name} Leaf`;
  const isHealthy = result.is_healthy;

  return (
    <div className="max-w-5xl mx-auto px-4 py-8 space-y-8">
      {/* Top Action Bar */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-slate-800/80">
        <div>
          <div className="flex items-center space-x-2 text-xs">
            <span className="font-mono text-teal-400 font-semibold uppercase tracking-wider">
              Diagnostic Report #{result.id.slice(0, 8)}
            </span>
            <span className="text-slate-600">•</span>
            <span className="text-slate-400 flex items-center space-x-1">
              <Clock className="w-3.5 h-3.5 text-slate-500" />
              <span>{new Date(result.timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}</span>
            </span>
          </div>
          <h1 className="text-2xl sm:text-3xl font-extrabold text-white tracking-tight mt-1 flex items-center space-x-2.5">
            <span>Leaf Diagnosis & Treatment Plan</span>
          </h1>
        </div>

        <div className="flex flex-wrap items-center gap-2.5">
          <button
            onClick={onAnalyseAnother}
            className="px-4 py-2.5 rounded-xl bg-teal-500 hover:bg-teal-400 text-slate-950 text-xs font-bold flex items-center space-x-2 shadow-lg shadow-teal-500/20 transition"
          >
            <RefreshCw className="w-4 h-4" />
            <span>Analyse Another Leaf</span>
          </button>
          <button
            onClick={onViewResearch}
            className="px-3.5 py-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 text-slate-300 border border-slate-800 text-xs font-semibold flex items-center space-x-1.5 transition"
          >
            <BarChart3 className="w-4 h-4 text-slate-400" />
            <span>Diagnostics Log</span>
          </button>
        </div>
      </div>

      {/* 3 Core Deliverables: Leaf Name, Disease Diagnosis, Treatment Solution */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        
        {/* Left Column: Core Results (2 cols wide) */}
        <div className="lg:col-span-2 space-y-6">

          {/* 1) NAME OF THE LEAF CARD */}
          <div className="bg-slate-900/80 border border-slate-800 rounded-2xl p-6 sm:p-7 backdrop-blur shadow-xl relative overflow-hidden">
            <div className="absolute top-0 right-0 w-48 h-48 bg-teal-500/5 rounded-full blur-3xl pointer-events-none" />
            
            <div className="flex items-center space-x-2 text-xs font-mono font-semibold uppercase tracking-wider text-teal-400 mb-2">
              <Leaf className="w-4 h-4" />
              <span>1. Identified Leaf Specimen</span>
            </div>

            <div className="flex flex-col sm:flex-row sm:items-baseline justify-between gap-2 border-b border-slate-800/80 pb-4">
              <div>
                <h2 className="text-3xl sm:text-4xl font-extrabold text-white tracking-tight">
                  {leafName}
                </h2>
                <div className="flex flex-wrap items-center gap-2 mt-2">
                  {details.scientific_name && (
                    <span className="text-xs font-serif italic text-teal-300 bg-teal-950/60 border border-teal-800/40 px-2.5 py-0.5 rounded-md">
                      {details.scientific_name}
                    </span>
                  )}
                  {details.plant_family && (
                    <span className="text-xs text-slate-400 bg-slate-950 px-2.5 py-0.5 rounded-md border border-slate-800 font-mono">
                      {details.plant_family} Family
                    </span>
                  )}
                  <span className="text-xs text-slate-400 bg-slate-950 px-2.5 py-0.5 rounded-md border border-slate-800">
                    Host: {result.plant_name}
                  </span>
                </div>
              </div>

              <div className="bg-slate-950/80 border border-slate-800 px-3.5 py-2 rounded-xl text-right sm:text-right">
                <span className="text-[10px] uppercase font-mono tracking-wider text-slate-400 block">AI Match Confidence</span>
                <span className="text-xl font-bold font-mono text-teal-400">{confidencePct}%</span>
              </div>
            </div>

            <p className="text-xs sm:text-sm text-slate-300 leading-relaxed mt-4">
              {result.scientific_summary}
            </p>
          </div>

          {/* 2) CHECK ANY DISEASES CAUSING IT CARD */}
          <div className="bg-slate-900/80 border border-slate-800 rounded-2xl p-6 sm:p-7 backdrop-blur shadow-xl space-y-5">
            <div className="flex items-center justify-between">
              <div className="flex items-center space-x-2 text-xs font-mono font-semibold uppercase tracking-wider text-cyan-400">
                <Bug className="w-4 h-4" />
                <span>2. Disease & Pathology Assessment</span>
              </div>
              
              <span className={`inline-flex items-center space-x-1.5 px-3 py-1 rounded-full text-xs font-bold border ${
                isHealthy 
                  ? 'bg-emerald-500/15 text-emerald-400 border-emerald-500/30' 
                  : 'bg-rose-500/15 text-rose-400 border-rose-500/30'
              }`}>
                {isHealthy ? (
                  <>
                    <CheckCircle2 className="w-4 h-4 text-emerald-400" />
                    <span>HEALTHY FOLIAGE</span>
                  </>
                ) : (
                  <>
                    <AlertTriangle className="w-4 h-4 text-rose-400" />
                    <span>DISEASE DETECTED</span>
                  </>
                )}
              </span>
            </div>

            {/* Condition & Pathogen Profile */}
            <div className={`p-5 rounded-xl border ${
              isHealthy
                ? 'bg-emerald-950/20 border-emerald-800/40 text-emerald-200'
                : 'bg-rose-950/20 border-rose-800/40 text-rose-200'
            }`}>
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
                <div>
                  <span className="text-[10px] uppercase font-mono tracking-wider opacity-75 block">Diagnosed Condition</span>
                  <h3 className="text-2xl font-black tracking-tight text-white mt-0.5">
                    {result.condition_name}
                  </h3>
                </div>
                <div className="text-left sm:text-right">
                  <span className="text-[10px] uppercase font-mono tracking-wider opacity-75 block">Causal Pathogen</span>
                  <span className="text-sm font-semibold text-slate-100 font-serif italic">
                    {details.causal_agent || 'None (Normal Cellular Tissue)'}
                  </span>
                </div>
              </div>

              {details.pathogen_type && details.pathogen_type !== 'None' && (
                <div className="mt-3 pt-3 border-t border-rose-800/30 flex items-center gap-2 text-xs">
                  <span className="px-2 py-0.5 rounded bg-rose-900/40 border border-rose-700/50 text-[11px] font-mono text-rose-300">
                    Pathogen Type: {details.pathogen_type}
                  </span>
                </div>
              )}
            </div>

            {/* Symptoms & Tissue Impact */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs">
              <div className="p-4 rounded-xl bg-slate-950/60 border border-slate-800/80 space-y-1.5">
                <span className="text-teal-400 font-mono font-semibold uppercase text-[10px] block">
                  Observed Foliar Symptoms
                </span>
                <p className="text-slate-300 text-[11px] leading-relaxed">
                  {details.symptoms || (isHealthy 
                    ? "Uniform green coloration, intact lamina, clean venation, no necrotic spots or chlorosis." 
                    : "Characteristic necrotic spots, chlorotic halos, or fungal pustules detected on blade.")}
                </p>
              </div>

              <div className="p-4 rounded-xl bg-slate-950/60 border border-slate-800/80 space-y-1.5">
                <span className="text-cyan-400 font-mono font-semibold uppercase text-[10px] block">
                  Pathology & Tissue Impact
                </span>
                <p className="text-slate-300 text-[11px] leading-relaxed">
                  {details.pathology || (isHealthy 
                    ? "Mesophyll tissue active in photosynthesis with optimal stomatal respiration." 
                    : "Cellular disruption caused by pathogen penetration, enzymatic degradation, or spore colonization.")}
                </p>
              </div>
            </div>
          </div>

          {/* 3) SOLUTION & TREATMENT FOR THAT CARD */}
          <div className="bg-slate-900/80 border border-slate-800 rounded-2xl p-6 sm:p-7 backdrop-blur shadow-xl space-y-6">
            <div className="flex items-center space-x-2 text-xs font-mono font-semibold uppercase tracking-wider text-emerald-400">
              <Pill className="w-4 h-4" />
              <span>3. Recommended Solution & Treatment Plan</span>
            </div>

            {/* Treatment Selector Tabs */}
            <div className="flex items-center space-x-2 border-b border-slate-800 pb-3">
              <button
                onClick={() => setActiveTreatmentTab('organic')}
                className={`px-3.5 py-1.5 rounded-lg text-xs font-semibold flex items-center space-x-1.5 transition ${
                  activeTreatmentTab === 'organic'
                    ? 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/40'
                    : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800'
                }`}
              >
                <Sprout className="w-3.5 h-3.5" />
                <span>Organic / Natural Solution</span>
              </button>

              <button
                onClick={() => setActiveTreatmentTab('chemical')}
                className={`px-3.5 py-1.5 rounded-lg text-xs font-semibold flex items-center space-x-1.5 transition ${
                  activeTreatmentTab === 'chemical'
                    ? 'bg-cyan-500/20 text-cyan-300 border border-cyan-500/40'
                    : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800'
                }`}
              >
                <FlaskConical className="w-3.5 h-3.5" />
                <span>Chemical Fungicide / Treatment</span>
              </button>

              <button
                onClick={() => setActiveTreatmentTab('prevention')}
                className={`px-3.5 py-1.5 rounded-lg text-xs font-semibold flex items-center space-x-1.5 transition ${
                  activeTreatmentTab === 'prevention'
                    ? 'bg-teal-500/20 text-teal-300 border border-teal-500/40'
                    : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800'
                }`}
              >
                <ShieldCheck className="w-3.5 h-3.5" />
                <span>Prevention & Care</span>
              </button>
            </div>

            {/* Tab 1: Organic Treatment */}
            {activeTreatmentTab === 'organic' && (
              <div className="space-y-4">
                <div className="p-4 rounded-xl bg-emerald-950/20 border border-emerald-800/40 space-y-2">
                  <div className="flex items-center space-x-2 text-emerald-400 font-semibold text-xs">
                    <Sprout className="w-4 h-4" />
                    <span>Biological & Organic Remedies</span>
                  </div>
                  <p className="text-xs sm:text-sm text-slate-200 leading-relaxed">
                    {details.treatment_organic || "Apply organic neem oil spray or beneficial Bacillus subtilis biofungicide. Remove and safely dispose of any severely infected lower leaves."}
                  </p>
                </div>

                {details.immediate_actions && details.immediate_actions.length > 0 && (
                  <div className="space-y-2">
                    <span className="text-[11px] font-mono uppercase tracking-wider text-slate-400 font-semibold block">
                      Immediate Action Steps:
                    </span>
                    <div className="space-y-2">
                      {details.immediate_actions.map((action, i) => (
                        <div key={i} className="flex items-start space-x-2.5 text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-lg border border-slate-800/60">
                          <Check className="w-4 h-4 text-emerald-400 shrink-0 mt-0.5" />
                          <span>{action}</span>
                        </div>
                      ))}
                    </div>
                  </div>
                )}
              </div>
            )}

            {/* Tab 2: Chemical Treatment */}
            {activeTreatmentTab === 'chemical' && (
              <div className="space-y-4">
                <div className="p-4 rounded-xl bg-cyan-950/20 border border-cyan-800/40 space-y-2">
                  <div className="flex items-center space-x-2 text-cyan-400 font-semibold text-xs">
                    <FlaskConical className="w-4 h-4" />
                    <span>Recommended Agricultural Spray Solutions</span>
                  </div>
                  <p className="text-xs sm:text-sm text-slate-200 leading-relaxed">
                    {details.treatment_chemical || "No synthetic chemical intervention required for healthy vegetative tissue. In case of active infection, use labeled protective fungicides such as Mancozeb or Chlorothalonil."}
                  </p>
                </div>

                <div className="p-3 rounded-lg bg-slate-950/60 border border-slate-800 text-[11px] text-slate-400 leading-relaxed flex items-start space-x-2">
                  <Info className="w-4 h-4 text-cyan-400 shrink-0 mt-0.5" />
                  <span>
                    <strong>Application Protocol:</strong> Always spray during calm weather (early morning or dusk) to prevent chemical drift and ensure full coverage on both leaf undersides and upper surfaces.
                  </span>
                </div>
              </div>
            )}

            {/* Tab 3: Prevention Guide */}
            {activeTreatmentTab === 'prevention' && (
              <div className="space-y-3">
                <span className="text-[11px] font-mono uppercase tracking-wider text-slate-400 font-semibold block">
                  Cultural Practices & Long-Term Crop Protection:
                </span>
                <div className="space-y-2">
                  {(details.prevention_guide || [
                    "Ensure adequate plant spacing to allow optimal air circulation and rapid drying after rain.",
                    "Use drip irrigation or soaker hoses to keep foliage dry and prevent water-splash dispersal of spores.",
                    "Rotate crops annually with non-host plant families to disrupt pathogen life cycles.",
                    "Disinfect shears and pruning tools with 70% alcohol between plants."
                  ]).map((point, idx) => (
                    <div key={idx} className="flex items-start space-x-2.5 text-xs text-slate-300 bg-slate-950/60 p-3 rounded-xl border border-slate-800/80">
                      <ShieldCheck className="w-4 h-4 text-teal-400 shrink-0 mt-0.5" />
                      <span>{point}</span>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        </div>

        {/* Right Column: Auxiliary Panel (Confidence Meter, Top Candidates, Meta) */}
        <div className="space-y-6">

          {/* Top Model Candidates */}
          <div className="bg-slate-900/80 border border-slate-800 rounded-2xl p-6 backdrop-blur shadow-xl space-y-4">
            <h4 className="text-xs font-mono uppercase tracking-wider text-slate-400 font-semibold flex items-center space-x-2">
              <Activity className="w-4 h-4 text-teal-400" />
              <span>Top Model Predictions</span>
            </h4>

            <div className="space-y-3">
              {result.top_predictions.map((pred, idx) => {
                const prob = (pred.confidence * 100).toFixed(1);
                return (
                  <div key={idx} className="space-y-1.5 p-3 rounded-xl bg-slate-950/60 border border-slate-800/60">
                    <div className="flex items-center justify-between text-xs">
                      <span className="font-semibold text-slate-200">
                        {pred.leaf_name || `${pred.plant} Leaf`}
                      </span>
                      <span className="font-mono text-teal-400 font-bold">{prob}%</span>
                    </div>
                    <div className="text-[11px] text-slate-400">
                      Condition: <span className={pred.is_healthy ? 'text-emerald-400' : 'text-rose-400'}>{pred.condition}</span>
                    </div>
                    <div className="w-full h-1.5 rounded-full bg-slate-800 overflow-hidden">
                      <div 
                        className={`h-full rounded-full transition-all duration-500 ${
                          idx === 0 ? 'bg-teal-400' : 'bg-slate-600'
                        }`}
                        style={{ width: `${prob}%` }}
                      />
                    </div>
                  </div>
                );
              })}
            </div>
          </div>

          {/* Specimen & Model Specifications */}
          <div className="bg-slate-900/80 border border-slate-800 rounded-2xl p-6 backdrop-blur shadow-xl space-y-3 text-xs">
            <h4 className="text-xs font-mono uppercase tracking-wider text-slate-400 font-semibold mb-2">
              Analysis Metadata
            </h4>
            
            <div className="space-y-2 text-[11px] font-mono text-slate-400 border-t border-slate-800/80 pt-3">
              <div className="flex justify-between">
                <span>File Name:</span>
                <span className="text-slate-200 truncate max-w-[150px]">{result.image_filename}</span>
              </div>
              <div className="flex justify-between">
                <span>Classification Engine:</span>
                <span className="text-slate-200 font-semibold">{result.model_name}</span>
              </div>
              <div className="flex justify-between">
                <span>Spatial Input:</span>
                <span className="text-slate-200 font-semibold">224 × 224 sRGB</span>
              </div>
              <div className="flex justify-between">
                <span>Model Version:</span>
                <span className="text-teal-400 font-semibold">{result.model_version}</span>
              </div>
            </div>
          </div>

          {/* Educational Disclaimer */}
          <div className="p-4 rounded-2xl bg-amber-500/10 border border-amber-500/25 space-y-2 text-xs text-amber-200/90 leading-relaxed">
            <div className="flex items-center space-x-2 text-amber-300 font-bold">
              <ShieldAlert className="w-4 h-4 text-amber-400 shrink-0" />
              <span>Educational Research Prototype</span>
            </div>
            <p className="text-[11px]">
              BioScan AI is an educational computer vision prototype. Predictions and treatments provided are for research and reference, and should be verified with local agricultural extension experts.
            </p>
          </div>
        </div>

      </div>
    </div>
  );
};
