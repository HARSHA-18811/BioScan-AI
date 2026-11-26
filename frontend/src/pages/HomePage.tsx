import React from 'react';
import { 
  ArrowRight, 
  UploadCloud, 
  Cpu, 
  FileCheck2, 
  Microscope, 
  Layers, 
  ShieldCheck, 
  Activity, 
  Dna, 
  Sparkles, 
  ChevronRight, 
  BookOpen,
  CheckCircle2,
  AlertTriangle,
  BarChart3
} from 'lucide-react';

interface HomePageProps {
  onStartAnalysis: () => void;
  onExploreResearch: () => void;
}

export const HomePage: React.FC<HomePageProps> = ({ 
  onStartAnalysis, 
  onExploreResearch 
}) => {
  const symptomGallery = [
    {
      title: "Healthy Vegetative Leaf",
      crop: "Solanum & Malus Taxa",
      color: "from-emerald-500/20 to-teal-500/10 border-emerald-500/30",
      accent: "text-emerald-400",
      dot: "bg-emerald-400",
      description: "Intact epidermal cuticle, uniform palisade chlorophyll a/b absorption, optimal turgor pressure, zero necrotic lesions.",
      mechanism: "Non-pathogenic vegetative baseline"
    },
    {
      title: "Apple Scab Necrosis",
      crop: "Venturia inaequalis",
      color: "from-lime-500/20 to-slate-900 border-lime-500/30",
      accent: "text-lime-400",
      dot: "bg-lime-400",
      description: "Subcuticular stromata penetrate cuticle, producing velvety olive-brown circular lesions leading to premature leaf defoliation.",
      mechanism: "Ascomycete cuticular penetration"
    },
    {
      title: "Corn Common Rust",
      crop: "Puccinia sorghi",
      color: "from-amber-500/20 to-slate-900 border-amber-500/30",
      accent: "text-amber-400",
      dot: "bg-amber-400",
      description: "Airborne dikaryotic urediniospores infect stomata, erupting through the epidermis in raised cinnamon-brown powdery pustules.",
      mechanism: "Basidiomycete uredinia pustules"
    },
    {
      title: "Early Blight Bullseye",
      crop: "Alternaria solani",
      color: "from-rose-500/20 to-slate-900 border-rose-500/30",
      accent: "text-rose-400",
      dot: "bg-rose-400",
      description: "Necrotrophic secretion of alternariol toxins produces characteristic concentric zonate rings bordered by yellow chlorotic halos.",
      mechanism: "Target-board concentric necrosis"
    },
    {
      title: "Bacterial Spot",
      crop: "Xanthomonas perforans",
      color: "from-cyan-500/20 to-slate-900 border-cyan-500/30",
      accent: "text-cyan-400",
      dot: "bg-cyan-400",
      description: "Phytopathogenic bacteria colonize apoplast via open stomata and hydathodes, causing dark angular water-soaked greasy spots.",
      mechanism: "Intercellular apoplastic degradation"
    }
  ];

  return (
    <div className="space-y-24 py-8">
      {/* Hero Section */}
      <section className="relative overflow-hidden pt-12 pb-16">
        {/* Subtle background glow */}
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[700px] h-[400px] bg-gradient-to-tr from-teal-500/10 via-cyan-500/10 to-transparent blur-3xl pointer-events-none rounded-full" />

        <div className="max-w-5xl mx-auto text-center px-4 relative z-10 space-y-6">
          <div className="inline-flex items-center space-x-2 px-3 py-1.5 rounded-full bg-slate-900/90 border border-teal-500/30 text-teal-300 text-xs font-medium tracking-wide">
            <Sparkles className="w-3.5 h-3.5 text-cyan-400" />
            <span>AI-Powered Biological Image Analysis & Foliar Diagnostics</span>
          </div>

          <h1 className="text-4xl sm:text-5xl lg:text-6xl font-extrabold text-white tracking-tight leading-[1.15]">
            Understanding Foliar Biology Through <br />
            <span className="text-transparent bg-clip-text bg-gradient-to-r from-teal-400 via-cyan-400 to-emerald-400">
              Artificial Intelligence
            </span>
          </h1>

          <p className="max-w-2xl mx-auto text-base sm:text-lg text-slate-300 font-normal leading-relaxed">
            BioScan AI applies deep convolutional neural networks to biological foliar imagery, 
            enabling automated detection and morphological feature extraction of plant diseases across agricultural crops.
          </p>

          {/* Action CTA Buttons */}
          <div className="flex flex-col sm:flex-row items-center justify-center gap-4 pt-4">
            <button
              onClick={onStartAnalysis}
              className="w-full sm:w-auto px-8 py-3.5 rounded-xl bg-gradient-to-r from-teal-500 to-cyan-500 text-slate-950 font-bold text-sm flex items-center justify-center space-x-2 shadow-lg shadow-teal-500/25 hover:shadow-cyan-500/40 hover:scale-[1.02] active:scale-[0.98] transition-all duration-150"
            >
              <span>Start Image Analysis</span>
              <ArrowRight className="w-4 h-4 stroke-[2.5]" />
            </button>

            <button
              onClick={onExploreResearch}
              className="w-full sm:w-auto px-7 py-3.5 rounded-xl bg-slate-900 hover:bg-slate-800 text-slate-200 border border-slate-700/80 font-semibold text-sm flex items-center justify-center space-x-2 hover:border-slate-600 transition-all duration-150"
            >
              <BookOpen className="w-4 h-4 text-slate-400" />
              <span>Explore Methodology</span>
            </button>
          </div>

          {/* Live quick badges */}
          <div className="pt-8 flex flex-wrap items-center justify-center gap-6 text-xs text-slate-400 font-mono">
            <div className="flex items-center space-x-2">
              <span className="w-2 h-2 rounded-full bg-teal-400" />
              <span>15 Supported Foliar Classes</span>
            </div>
            <div className="flex items-center space-x-2">
              <span className="w-2 h-2 rounded-full bg-cyan-400" />
              <span>MobileNetV2 CNN Architecture</span>
            </div>
            <div className="flex items-center space-x-2">
              <span className="w-2 h-2 rounded-full bg-emerald-400" />
              <span>Zero-Simulation Real Inference</span>
            </div>
          </div>
        </div>
      </section>

      {/* Macroscopic Foliar Symptom Gallery */}
      <section className="max-w-6xl mx-auto px-4">
        <div className="text-center space-y-2 mb-10">
          <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-teal-500/10 text-teal-300 text-xs font-semibold border border-teal-500/20">
            <Microscope className="w-3.5 h-3.5 text-teal-400" />
            <span>Phytopathological Symptom Morphology · Visual Diagnosis Profiles</span>
          </div>
          <h2 className="text-2xl sm:text-3xl font-bold text-white tracking-tight">
            Macroscopic Foliar Symptom Profiles
          </h2>
          <p className="text-sm text-slate-400 max-w-2xl mx-auto">
            Deep convolutional neural networks learn spatial feature abstractions mirroring the biochemical and tissue-level consequences of pathogen colonization.
          </p>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-4">
          {symptomGallery.map((item, idx) => (
            <div 
              key={idx}
              className={`bg-gradient-to-b ${item.color} rounded-2xl p-4 border flex flex-col justify-between hover:scale-[1.02] transition-transform duration-200`}
            >
              <div className="space-y-2">
                <div className="flex items-center gap-2">
                  <span className={`w-2.5 h-2.5 rounded-full ${item.dot}`} />
                  <span className="text-[11px] font-mono uppercase text-slate-400">Specimen #{idx + 1}</span>
                </div>
                <h3 className={`text-sm font-bold ${item.accent}`}>{item.title}</h3>
                <p className="text-[11px] font-serif italic text-slate-300">{item.crop}</p>
                <p className="text-xs text-slate-400 leading-relaxed pt-1">{item.description}</p>
              </div>
              <div className="pt-4 mt-3 border-t border-slate-800/80 text-[10px] text-slate-400">
                <span className="font-semibold block text-slate-300">Pathology Mode:</span>
                {item.mechanism}
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* 3-Step Process */}
      <section className="max-w-6xl mx-auto px-4">
        <div className="text-center space-y-2 mb-12">
          <h2 className="text-xs font-mono uppercase tracking-widest text-teal-400 font-semibold">How It Works</h2>
          <p className="text-2xl sm:text-3xl font-bold text-white">Three-Step Scientific Workflow</p>
          <p className="text-sm text-slate-400 max-w-xl mx-auto">
            From raw foliar specimen to deep feature inference and pathological insights.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 relative">
          {/* Step 1 */}
          <div className="bg-slate-900/60 border border-slate-800 rounded-2xl p-6 relative group hover:border-teal-500/40 transition-colors">
            <div className="w-12 h-12 rounded-xl bg-teal-500/10 border border-teal-500/20 flex items-center justify-center text-teal-400 mb-4 group-hover:scale-110 transition-transform">
              <UploadCloud className="w-6 h-6" />
            </div>
            <div className="text-xs font-mono text-teal-400 font-semibold uppercase tracking-wider mb-1">Step 01</div>
            <h3 className="text-lg font-bold text-white mb-2">Image Upload & Validation</h3>
            <p className="text-sm text-slate-400 leading-relaxed">
              Upload RGB leaf images (JPEG, PNG). The system validates byte integrity, converts to sRGB, resizes to 224×224, and applies ImageNet z-score normalization.
            </p>
          </div>

          {/* Step 2 */}
          <div className="bg-slate-900/60 border border-slate-800 rounded-2xl p-6 relative group hover:border-teal-500/40 transition-colors">
            <div className="w-12 h-12 rounded-xl bg-cyan-500/10 border border-cyan-500/20 flex items-center justify-center text-cyan-400 mb-4 group-hover:scale-110 transition-transform">
              <Cpu className="w-6 h-6" />
            </div>
            <div className="text-xs font-mono text-cyan-400 font-semibold uppercase tracking-wider mb-1">Step 02</div>
            <h3 className="text-lg font-bold text-white mb-2">Deep Feature Extraction</h3>
            <p className="text-sm text-slate-400 leading-relaxed">
              Inverted residual blocks isolate vein structures, chlorosis gradients, and necrotic margins using depthwise separable convolutions (8.5× speedup).
            </p>
          </div>

          {/* Step 3 */}
          <div className="bg-slate-900/60 border border-slate-800 rounded-2xl p-6 relative group hover:border-teal-500/40 transition-colors">
            <div className="w-12 h-12 rounded-xl bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-center text-emerald-400 mb-4 group-hover:scale-110 transition-transform">
              <FileCheck2 className="w-6 h-6" />
            </div>
            <div className="text-xs font-mono text-emerald-400 font-semibold uppercase tracking-wider mb-1">Step 03</div>
            <h3 className="text-lg font-bold text-white mb-2">Calibrated Diagnosis & Audit</h3>
            <p className="text-sm text-slate-400 leading-relaxed">
              Generates top predictions, calibrated probability distributions, causal pathogen taxonomy, and persists the record to the SQLite audit log.
            </p>
          </div>
        </div>
      </section>

      {/* Deep Learning Architecture Features */}
      <section className="max-w-6xl mx-auto px-4">
        <div className="bg-slate-900/50 border border-slate-800 rounded-3xl p-8 sm:p-12 relative overflow-hidden">
          <div className="max-w-3xl space-y-6">
            <div className="inline-flex items-center space-x-2 text-xs font-mono uppercase tracking-wider px-3 py-1 rounded-full bg-teal-500/10 text-teal-400 border border-teal-500/20">
              <ShieldCheck className="w-4 h-4 text-teal-400" />
              <span>Deep Learning Architecture & Reliability</span>
            </div>

            <h2 className="text-2xl sm:text-3xl font-extrabold text-white tracking-tight">
              Parameter-Efficient Botanical Computer Vision
            </h2>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs pt-2">
              <div className="bg-slate-950/70 border border-slate-800 p-4 rounded-xl space-y-2">
                <span className="font-bold text-teal-300 block">Depthwise Separable Convolutions</span>
                <p className="font-mono text-cyan-300 text-[11px]">Cost_sep / Cost_std = (1 / N) + (1 / D_K²)</p>
                <p className="text-slate-400 leading-relaxed">
                  Reduces computational operations by 88.9% (~8.5× speedup) for edge deployment without sacrificing diagnostic accuracy.
                </p>
              </div>

              <div className="bg-slate-950/70 border border-slate-800 p-4 rounded-xl space-y-2">
                <span className="font-bold text-amber-300 block">Softmax Probability Calibration</span>
                <p className="font-mono text-amber-200 text-[11px]">p_k = exp(z_k / T) / ∑ exp(z_j / T)</p>
                <p className="text-slate-400 leading-relaxed">
                  Statistical confidence is not clinical diagnosis. Post-hoc temperature scaling (T=1.80) curtails uncalibrated overconfidence.
                </p>
              </div>
            </div>

            <div className="pt-2 flex flex-wrap gap-4">
              <button
                onClick={onStartAnalysis}
                className="px-6 py-2.5 rounded-xl bg-teal-500 hover:bg-teal-400 text-slate-950 font-semibold text-xs transition-colors flex items-center gap-1.5"
              >
                <span>Try Foliar Classifier</span>
                <ArrowRight className="w-3.5 h-3.5" />
              </button>
              <button
                onClick={onExploreResearch}
                className="px-5 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-semibold text-xs transition-colors flex items-center gap-1.5"
              >
                <BookOpen className="w-3.5 h-3.5 text-teal-400" />
                <span>Read Full Methodology</span>
              </button>
            </div>
          </div>
        </div>
      </section>

      {/* Academic Disclaimer Banner */}
      <section className="max-w-4xl mx-auto px-4 text-center">
        <div className="bg-amber-950/20 border border-amber-500/20 rounded-2xl p-5 text-xs text-slate-400 flex items-center justify-center gap-3">
          <AlertTriangle className="w-5 h-5 text-amber-400 shrink-0" />
          <span>
            <strong>Educational Research Prototype:</strong> BioScan AI is built for academic experiential learning in biological computer vision. Model predictions are not a substitute for expert plant pathology scouting or clinical laboratory diagnosis.
          </span>
        </div>
      </section>
    </div>
  );
};
