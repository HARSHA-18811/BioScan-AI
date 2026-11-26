import React from 'react';
import { 
  Info, 
  GraduationCap, 
  Target, 
  AlertCircle, 
  Lightbulb, 
  Compass, 
  Rocket, 
  User, 
  School,
  FileCode2
} from 'lucide-react';

export const AboutPage: React.FC = () => {
  return (
    <div className="max-w-4xl mx-auto px-4 py-8 space-y-12">
      {/* Title */}
      <div className="space-y-3 text-center sm:text-left">
        <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-teal-500/10 text-teal-300 border border-teal-500/20 text-xs font-mono">
          <GraduationCap className="w-3.5 h-3.5" />
          <span>Academic Experiential Learning Project</span>
        </div>
        <h1 className="text-3xl sm:text-4xl font-extrabold text-white tracking-tight">
          About BioScan AI
        </h1>
        <p className="text-sm text-slate-400 leading-relaxed">
          An academic research prototype investigating the intersection of deep convolutional neural networks and botanical foliar pathology.
        </p>
      </div>

      {/* Structured Sections */}
      <div className="space-y-8">
        
        {/* Academic Project Metadata (Editable Placeholders) */}
        <div className="bg-slate-900/60 border border-slate-800 rounded-3xl p-6 sm:p-8 backdrop-blur space-y-4">
          <div className="flex items-center space-x-3 text-teal-400">
            <School className="w-6 h-6" />
            <h2 className="text-lg font-bold text-white">Academic Project Credentials</h2>
          </div>
          <p className="text-xs text-slate-400 leading-relaxed">
            This system was constructed as an experiential learning and research project exploring modern computer vision techniques for biological data analysis.
          </p>

          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs font-mono pt-2">
            <div className="p-4 rounded-xl bg-slate-950 border border-slate-800">
              <span className="text-slate-500 block mb-1">Course / Semester:</span>
              <span className="text-slate-200">[Semester 3 - Biology & Computational Sciences]</span>
            </div>
            <div className="p-4 rounded-xl bg-slate-950 border border-slate-800">
              <span className="text-slate-500 block mb-1">Student / Researcher:</span>
              <span className="text-slate-200">[Student Name / Editable Placeholder]</span>
            </div>
            <div className="p-4 rounded-xl bg-slate-950 border border-slate-800">
              <span className="text-slate-500 block mb-1">Academic Mentor / Faculty:</span>
              <span className="text-slate-200">[Faculty Advisor Name / Editable Placeholder]</span>
            </div>
            <div className="p-4 rounded-xl bg-slate-950 border border-slate-800">
              <span className="text-slate-500 block mb-1">Institution / Department:</span>
              <span className="text-slate-200">[University Department / Editable Placeholder]</span>
            </div>
          </div>
        </div>

        {/* Problem Statement */}
        <div className="bg-slate-900/60 border border-slate-800 rounded-3xl p-6 sm:p-8 backdrop-blur space-y-3">
          <div className="flex items-center space-x-3 text-amber-400">
            <AlertCircle className="w-6 h-6" />
            <h2 className="text-lg font-bold text-white">Problem Statement</h2>
          </div>
          <p className="text-xs text-slate-300 leading-relaxed">
            Plant foliar diseases—such as fungal rusts, bacterial spots, and oomycete blights—cause estimated worldwide crop yield losses of 20% to 40% annually, severely threatening global food security. Traditional identification depends heavily on manual visual scouting by certified plant pathologists, a practice that is labor-intensive, geographically constrained, and slow during seasonal outbreaks.
          </p>
        </div>

        {/* Proposed Solution */}
        <div className="bg-slate-900/60 border border-slate-800 rounded-3xl p-6 sm:p-8 backdrop-blur space-y-3">
          <div className="flex items-center space-x-3 text-cyan-400">
            <Lightbulb className="w-6 h-6" />
            <h2 className="text-lg font-bold text-white">Proposed AI Solution</h2>
          </div>
          <p className="text-xs text-slate-300 leading-relaxed">
            BioScan AI proposes a modular, reproducible deep learning system that couples high-throughput image preprocessing with lightweight convolutional backbones (MobileNetV2 and custom multi-scale CNNs). The system validates foliar specimen health status, provides top-k candidate probability distributions, and accompanies every diagnosis with botanical etiology and management literature.
          </p>
        </div>

        {/* Project Scope */}
        <div className="bg-slate-900/60 border border-slate-800 rounded-3xl p-6 sm:p-8 backdrop-blur space-y-3">
          <div className="flex items-center space-x-3 text-emerald-400">
            <Compass className="w-6 h-6" />
            <h2 className="text-lg font-bold text-white">Current Project Scope</h2>
          </div>
          <p className="text-xs text-slate-300 leading-relaxed">
            The initial phase focuses on 15 foliar categories across major commercial crops (Apple, Corn, Grape, Potato, Tomato), spanning fungal infections (scab, rust, blight), bacterial spots, and healthy vegetative baselines.
          </p>
          <div className="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-400">
            <strong>Educational Scope Boundary:</strong> This application is explicitly designed as an academic educational research prototype and is not certified for commercial agronomy or medical human diagnostics.
          </div>
        </div>

        {/* Future Scope */}
        <div className="bg-slate-900/60 border border-slate-800 rounded-3xl p-6 sm:p-8 backdrop-blur space-y-3">
          <div className="flex items-center space-x-3 text-indigo-400">
            <Rocket className="w-6 h-6" />
            <h2 className="text-lg font-bold text-white">Future Research Roadmap</h2>
          </div>
          <ul className="text-xs space-y-2 text-slate-300 pl-4 list-disc">
            <li><strong>Module Expansion:</strong> Cellular microscopy imaging, stomatal density analysis, and fungal hyphae segmentation.</li>
            <li><strong>Explainable AI (XAI):</strong> Integrated Grad-CAM heatmaps to visually highlight the precise lesion pixels informing classification.</li>
            <li><strong>Multi-Modal Data:</strong> Combining spectral drone photography with soil sensor telemetry and local weather data.</li>
            <li><strong>Cloud Integration:</strong> Optional Supabase or cloud object storage integration via modular repository interfaces.</li>
          </ul>
        </div>
      </div>
    </div>
  );
};
