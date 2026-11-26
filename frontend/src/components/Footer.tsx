import React from 'react';
import { ShieldCheck, Cpu, Database, Binary, GitFork } from 'lucide-react';

export const Footer: React.FC = () => {
  return (
    <footer className="mt-20 border-t border-slate-800/80 bg-[#070b14] text-slate-400 text-sm">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8 mb-8">
          {/* Brand and Mission */}
          <div className="md:col-span-2 space-y-3">
            <div className="flex items-center space-x-2">
              <span className="font-bold text-base text-white">BioScan <span className="text-teal-400">AI</span></span>
              <span className="text-[10px] bg-slate-800 text-teal-300 px-2 py-0.5 rounded border border-slate-700 font-mono">
                v1.0.0 Research Edition
              </span>
            </div>
            <p className="text-slate-400 text-xs leading-relaxed max-w-md">
              An experiential learning computer vision system designed to explore deep learning applications in biological foliar pathology, specimen classification, and automated botanical diagnostics.
            </p>
            <div className="flex items-center space-x-4 text-xs text-slate-500 pt-2">
              <span className="flex items-center space-x-1">
                <Cpu className="w-3.5 h-3.5 text-teal-400" />
                <span>PyTorch / MobileNet</span>
              </span>
              <span className="flex items-center space-x-1">
                <Database className="w-3.5 h-3.5 text-cyan-400" />
                <span>FastAPI + SQLite</span>
              </span>
              <span className="flex items-center space-x-1">
                <GitFork className="w-3.5 h-3.5 text-emerald-400" />
                <span>Modular Architecture</span>
              </span>
            </div>
          </div>

          {/* Supported Genera */}
          <div>
            <h4 className="text-xs font-semibold text-slate-200 uppercase tracking-wider mb-3">Supported Flora</h4>
            <ul className="text-xs space-y-1.5 text-slate-400">
              <li>• Malus domestica (Apple)</li>
              <li>• Zea mays (Corn / Maize)</li>
              <li>• Vitis vinifera (Grape)</li>
              <li>• Solanum tuberosum (Potato)</li>
              <li>• Solanum lycopersicum (Tomato)</li>
            </ul>
          </div>

          {/* Research Principles */}
          <div>
            <h4 className="text-xs font-semibold text-slate-200 uppercase tracking-wider mb-3">Academic Rigor</h4>
            <ul className="text-xs space-y-1.5 text-slate-400">
              <li>• Zero simulated predictions</li>
              <li>• Stratified split evaluation</li>
              <li>• Repeatable random seeds</li>
              <li>• Statistical probability metrics</li>
              <li>• Modular scientific extensions</li>
            </ul>
          </div>
        </div>

        {/* Disclaimer Card */}
        <div className="border border-amber-500/20 bg-amber-500/5 rounded-xl p-4 mb-8 flex items-start space-x-3 text-xs text-amber-200/90 leading-relaxed">
          <ShieldCheck className="w-5 h-5 text-amber-400 shrink-0 mt-0.5" />
          <div>
            <span className="font-semibold text-amber-300">Academic Research Disclaimer: </span>
            BioScan AI is an educational research prototype. Its predictions are not a substitute for certified plant pathology assessment, professional agronomist field scouting, or laboratory microbial assays. Statistical confidence indicates mathematical softmax probability, not guaranteed real-world diagnosis.
          </div>
        </div>

        <div className="pt-6 border-t border-slate-800/60 flex flex-col sm:flex-row items-center justify-between text-xs text-slate-500">
          <p>© {new Date().getFullYear()} BioScan AI Research Project. Built for biological data analysis and deep learning exploration.</p>
          <p className="mt-2 sm:mt-0 font-mono text-[11px] text-slate-400">
            Status: Fully Reproducible Pipeline
          </p>
        </div>
      </div>
    </footer>
  );
};
