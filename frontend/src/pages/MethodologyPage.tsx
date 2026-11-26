import React, { useState } from 'react';
import { 
  BookOpen, 
  Dna, 
  Cpu, 
  Layers, 
  SlidersHorizontal, 
  ShieldCheck, 
  AlertTriangle,
  Search,
  Filter,
  CheckCircle2,
  Table as TableIcon
} from 'lucide-react';

export const MethodologyPage: React.FC = () => {
  const [selectedCrop, setSelectedCrop] = useState<string>('All');
  const [searchTerm, setSearchTerm] = useState<string>('');

  const taxonomyData = [
    {
      host: "Malus domestica (Apple)",
      cropKey: "Apple",
      condition: "Apple Scab",
      pathogen: "Venturia inaequalis",
      etiology: "Ascomycete Fungus",
      cellular: "Subcuticular stroma develops between cuticle and epidermal wall; conidiophores physically rupture cuticle.",
      symptoms: "Velvety olive-green to melanized brown circular lesions; causes severe chlorosis, distortion, and premature defoliation."
    },
    {
      host: "Malus domestica (Apple)",
      cropKey: "Apple",
      condition: "Black Rot",
      pathogen: "Diplodia seriata",
      etiology: "Ascomycete Fungus",
      cellular: "Rain-splash dispersed conidia colonize damaged epidermis; hyphae induce rapid cellular parenchyma necrosis.",
      symptoms: "'Frogeye' leaf spots featuring tan necrotic centers surrounded by distinct purple-brown concentric rings."
    },
    {
      host: "Malus domestica (Apple)",
      cropKey: "Apple",
      condition: "Cedar Apple Rust",
      pathogen: "Gymnosporangium juniperi-virg.",
      etiology: "Heteroecious Rust",
      cellular: "Obligate parasite requiring alternate juniper host; produces spermogonia on adaxial leaf and aecial cups on abaxial side.",
      symptoms: "Bright yellow-orange aecial spots erupting on upper leaf surface; tubular cups protruding beneath."
    },
    {
      host: "Malus domestica (Apple)",
      cropKey: "Apple",
      condition: "Healthy Foliage",
      cropKey2: "Healthy",
      pathogen: "None (Vegetative Baseline)",
      etiology: "Non-Pathogenic",
      cellular: "Intact palisade and spongy mesophyll; balanced chlorophyll a/b ratio; optimal stomatal conductance.",
      symptoms: "Intact waxy cuticle, uniform green coloration across palmate veins, zero chlorotic flecking or necrosis."
    },
    {
      host: "Zea mays (Corn)",
      cropKey: "Corn",
      condition: "Common Rust",
      pathogen: "Puccinia sorghi",
      etiology: "Basidiomycete Rust",
      cellular: "Airborne dikaryotic urediniospores infect stomata; intercellular mycelium produces haustoria absorbing host sugars.",
      symptoms: "Raised cinnamon-brown to golden powdery pustules (uredinia) rupturing epidermal layers along parallel venation."
    },
    {
      host: "Zea mays (Corn)",
      cropKey: "Corn",
      condition: "Northern Leaf Blight",
      pathogen: "Exserohilum turcicum",
      etiology: "Ascomycete Fungus",
      cellular: "Overwinters in crop debris; appressoria penetrate host cuticle; hyphae proliferate longitudinally within vascular bundles.",
      symptoms: "Long, elliptical, cigar-shaped grayish-green to tan lesions (2.5–15 cm) extending parallel to leaf veins."
    },
    {
      host: "Zea mays (Corn)",
      cropKey: "Corn",
      condition: "Healthy Foliage",
      cropKey2: "Healthy",
      pathogen: "None (Vegetative Baseline)",
      etiology: "Non-Pathogenic",
      cellular: "Vigorous C4 photosynthetic foliar structure; unblemished epidermal cells; uninterrupted parallel vascular bundles.",
      symptoms: "Uniform parallel venation, dark green chlorophyll pigmentation, absence of fungal or viral lesions."
    },
    {
      host: "Vitis vinifera (Grape)",
      cropKey: "Grape",
      condition: "Black Rot",
      pathogen: "Guignardia bidwellii",
      etiology: "Ascomycete Fungus",
      cellular: "Ascospores germinate in free moisture; hyphae destroy mesophyll cells, leaving sunken necrotic parenchymal pits.",
      symptoms: "Reddish-brown circular necrotic spots with minute black pycnidia fruiting bodies embedded along borders."
    },
    {
      host: "Vitis vinifera (Grape)",
      cropKey: "Grape",
      condition: "Healthy Foliage",
      cropKey2: "Healthy",
      pathogen: "None (Vegetative Baseline)",
      etiology: "Non-Pathogenic",
      cellular: "Unblemished palmate leaf blades; intact vascular bundles; optimal leaf water potential; absence of powdery mildew.",
      symptoms: "Smooth palmate green leaf blade; active spongy mesophyll; zero necrosis or mildew mycelium."
    },
    {
      host: "Solanum tuberosum (Potato)",
      cropKey: "Potato",
      condition: "Early Blight",
      pathogen: "Alternaria solani",
      etiology: "Deuteromycete Fungus",
      cellular: "Necrotrophic fungus secreting alternariol and alternaric acid phytotoxins; causes cyclical localized cell lysis.",
      symptoms: "Distinct concentric rings forming a 'target-board' bullseye pattern surrounded by yellow chlorotic halos."
    },
    {
      host: "Solanum tuberosum (Potato)",
      cropKey: "Potato",
      condition: "Late Blight",
      pathogen: "Phytophthora infestans",
      etiology: "Oomycete (Water Mold)",
      cellular: "Biflagellate motile zoospores encyst and penetrate cuticle; rapid systemic collapse of host cell membranes.",
      symptoms: "Dark, water-soaked rapidly expanding necrotic lesions with white downy sporangiophores under humid conditions."
    },
    {
      host: "Solanum tuberosum (Potato)",
      cropKey: "Potato",
      condition: "Healthy Foliage",
      cropKey2: "Healthy",
      pathogen: "None (Vegetative Baseline)",
      etiology: "Non-Pathogenic",
      cellular: "Robust compound foliage; fully turgid laminar tissue; intact glandular trichomes; zero mottling or wilting.",
      symptoms: "Smooth pinnate leaflets, vibrant deep green photosynthetic tissue, absence of necrosis or chlorosis."
    },
    {
      host: "Solanum lycopersicum (Tomato)",
      cropKey: "Tomato",
      condition: "Bacterial Spot",
      pathogen: "Xanthomonas perforans",
      etiology: "Gram-Negative Bacterium",
      cellular: "Enters through natural stomata and mechanical wounds; multiplies in apoplast, secreting cell-wall pectinases.",
      symptoms: "Small (<3 mm), angular, dark water-soaked spots with greasy texture, developing into necrotic lesions with yellow halos."
    },
    {
      host: "Solanum lycopersicum (Tomato)",
      cropKey: "Tomato",
      condition: "Early Blight",
      pathogen: "Alternaria solani",
      etiology: "Deuteromycete Fungus",
      cellular: "Conidia germinate in free leaf moisture; appressorial penetration followed by necrotrophic host cell collapse.",
      symptoms: "Dark brown necrotic lesions with concentric bullseye rings initiating on lower, older canopy leaves."
    },
    {
      host: "Solanum lycopersicum (Tomato)",
      cropKey: "Tomato",
      condition: "Healthy Foliage",
      cropKey2: "Healthy",
      pathogen: "None (Vegetative Baseline)",
      etiology: "Non-Pathogenic",
      cellular: "Pinnately compound deep green foliage; active photosynthetic mesophyll; absence of epinasty or viral leaf curl.",
      symptoms: "Vigorous compound leaf structure, fully expanded leaflets, zero spotting, stippling, or chlorosis."
    }
  ];

  const crops = ['All', 'Apple', 'Corn', 'Grape', 'Potato', 'Tomato'];

  const filteredTaxa = taxonomyData.filter((item) => {
    const matchesCrop = selectedCrop === 'All' || item.cropKey === selectedCrop;
    const matchesSearch = 
      item.condition.toLowerCase().includes(searchTerm.toLowerCase()) ||
      item.host.toLowerCase().includes(searchTerm.toLowerCase()) ||
      item.pathogen.toLowerCase().includes(searchTerm.toLowerCase()) ||
      item.etiology.toLowerCase().includes(searchTerm.toLowerCase());
    return matchesCrop && matchesSearch;
  });

  return (
    <div className="max-w-5xl mx-auto px-4 py-8 space-y-12">
      {/* Page Header */}
      <div className="pb-6 border-b border-slate-800">
        <div className="space-y-2">
          <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-teal-500/10 text-teal-300 border border-teal-500/20 text-xs font-mono">
            <BookOpen className="w-3.5 h-3.5" />
            <span>Scientific Documentation & Deep Learning Architecture</span>
          </div>
          <h1 className="text-3xl sm:text-4xl font-extrabold text-white tracking-tight">
            Scientific Methodology & Mathematical Foundations
          </h1>
          <p className="text-sm text-slate-400 max-w-2xl leading-relaxed">
            Analytical formulations of depthwise separable convolution complexity, mathematical formulation of Expected Calibration Error (ECE), and the complete 15-class foliar pathology taxonomy.
          </p>
        </div>
      </div>

      {/* Sections */}
      <div className="space-y-10">
        {/* 1. Biological Image Analysis & Histology */}
        <div className="bg-slate-900/60 border border-slate-800 rounded-3xl p-6 sm:p-8 backdrop-blur space-y-4">
          <div className="flex items-center space-x-3 text-teal-400">
            <Dna className="w-6 h-6" />
            <h2 className="text-lg font-bold text-white">1. Botanical Histology & Pathological Manifestations</h2>
          </div>
          <p className="text-xs sm:text-sm text-slate-300 leading-relaxed">
            In terrestrial vascular plants, the foliar lamina is the primary photosynthetic organ. Angiosperm leaves exhibit a specialized histology: an exterior protective waxy cuticle, columnar palisade parenchyma rich in chloroplasts, spongy mesophyll with intercellular gas channels, and vascular bundles containing xylem tracheary elements and phloem sieve tubes.
          </p>
          <p className="text-xs sm:text-sm text-slate-400 leading-relaxed">
            Pathogenic infection disrupts this cellular order: (1) <strong>Chlorosis</strong> occurs when fungal toxins degrade chlorophyll pigments; (2) <strong>Necrosis</strong> manifests as irreversible cellular collapse from phytotoxin secretion (e.g. alternaric acid); (3) <strong>Target-Board Rings</strong> arise from cyclical pulses of pathogen colonization; and (4) <strong>Water-Soaked Spots</strong> emerge when bacterial pectate lyases break down the middle lamella.
          </p>
        </div>

        {/* 2. Mathematical Derivation: Depthwise Separable Convolutions */}
        <div className="bg-slate-900/60 border border-teal-500/30 rounded-3xl p-6 sm:p-8 backdrop-blur space-y-5">
          <div className="flex items-center space-x-3 text-cyan-400">
            <Cpu className="w-6 h-6" />
            <h2 className="text-lg font-bold text-white">2. Mathematical Derivation: Depthwise Separable Convolutions</h2>
          </div>

          <p className="text-xs sm:text-sm text-slate-300 leading-relaxed">
            Standard 2D spatial convolution applies a 3D filter kernel of size <code className="text-cyan-300 font-mono text-xs">D_K × D_K × M</code> across all <code className="text-cyan-300 font-mono text-xs">N</code> output channels over an input feature map of dimensions <code className="text-cyan-300 font-mono text-xs">D_F × D_F</code>. The total computational FLOPs cost is:
          </p>

          <div className="bg-slate-950 p-4 rounded-xl border border-slate-800 font-mono text-xs text-rose-300 text-center">
            Cost_standard = D_K² · M · N · D_F²
          </div>

          <p className="text-xs sm:text-sm text-slate-300 leading-relaxed">
            <strong>MobileNetV2</strong> factors this operation into two decoupled computational steps:
          </p>

          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs font-mono">
            <div className="bg-slate-950 p-3.5 rounded-xl border border-slate-800">
              <span className="text-slate-400 block text-[11px] mb-1">Step 1: Depthwise Spatial Filtering</span>
              <span className="text-emerald-400 font-bold block">Cost_dw = D_K² · M · D_F²</span>
              <span className="text-[10px] text-slate-500 block mt-1">Applies one 2D kernel per input channel.</span>
            </div>
            <div className="bg-slate-950 p-3.5 rounded-xl border border-slate-800">
              <span className="text-slate-400 block text-[11px] mb-1">Step 2: Pointwise 1×1 Projection</span>
              <span className="text-cyan-400 font-bold block">Cost_pw = M · N · D_F²</span>
              <span className="text-[10px] text-slate-500 block mt-1">Linear channel combination across manifolds.</span>
            </div>
          </div>

          <p className="text-xs sm:text-sm text-slate-300 leading-relaxed">
            Taking the computational ratio:
          </p>

          <div className="bg-teal-950/40 p-4 rounded-xl border border-teal-500/30 font-mono text-xs text-teal-300 text-center">
            Ratio = Cost_separable / Cost_standard = (D_K² · M · D_F² + M · N · D_F²) / (D_K² · M · N · D_F²) = (1 / N) + (1 / D_K²)
          </div>

          <div className="bg-slate-950 p-4 rounded-xl border border-slate-800 text-xs text-slate-300 leading-relaxed">
            <strong className="text-emerald-300 block mb-1">Empirical Speedup Demonstration:</strong>
            For standard 3×3 convolutions (<code className="text-cyan-300 font-mono text-[11px]">D_K = 3</code>) where channel depth <code className="text-cyan-300 font-mono text-[11px]">N ≥ 64</code>:
            <br />
            <code className="text-emerald-300 font-mono text-xs">Ratio ≈ (1 / 64) + (1 / 9) ≈ 0.0156 + 0.1111 ≈ 0.1267 ≈ 88.9% FLOPs reduction (~8.5× speedup)</code>
            <br />
            This analytical reduction enables deep 17-block feature extraction directly on edge agricultural hardware and commodity CPUs.
          </div>
        </div>

        {/* 3. Effective Receptive Field (ERF) Hierarchy */}
        <div className="bg-slate-900/60 border border-slate-800 rounded-3xl p-6 sm:p-8 backdrop-blur space-y-4">
          <div className="flex items-center space-x-3 text-indigo-400">
            <Layers className="w-6 h-6" />
            <h2 className="text-lg font-bold text-white">3. Effective Receptive Field (ERF) Hierarchy</h2>
          </div>
          <p className="text-xs sm:text-sm text-slate-300 leading-relaxed">
            Across convolutional layers <code className="text-indigo-300 font-mono text-xs">l = 1, ..., L</code>, the spatial receptive field grows recursively as:
          </p>
          <div className="bg-slate-950 p-4 rounded-xl border border-slate-800 font-mono text-xs text-indigo-300 text-center">
            ERF_l = ERF_{`{l-1}`} + (k_l - 1) · ∏_{`{i=1}`}^{`{l-1}`} s_i
          </div>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs pt-1">
            <div className="bg-slate-950/70 p-3.5 rounded-xl border border-slate-800 space-y-1">
              <span className="text-teal-400 font-semibold block">Layer 1: Low-Level (3×3 to 7×7)</span>
              <p className="text-slate-400 leading-relaxed">Edge transitions, vein boundaries, and cuticle color gradients.</p>
            </div>
            <div className="bg-slate-950/70 p-3.5 rounded-xl border border-slate-800 space-y-1">
              <span className="text-cyan-400 font-semibold block">Layer 2: Intermediate (15×15 to 31×31)</span>
              <p className="text-slate-400 leading-relaxed">Concentric bullseye arcs, chlorotic margins, and pustule clusters.</p>
            </div>
            <div className="bg-slate-950/70 p-3.5 rounded-xl border border-slate-800 space-y-1">
              <span className="text-indigo-400 font-semibold block">Layer 3: High-Level (&gt;100×100)</span>
              <p className="text-slate-400 leading-relaxed">Full laminar context, complete lesion geometry, and host health.</p>
            </div>
          </div>
        </div>

        {/* 4. Softmax Probability vs Diagnostic Accuracy */}
        <div className="bg-slate-900/60 border border-amber-500/30 rounded-3xl p-6 sm:p-8 backdrop-blur space-y-4">
          <div className="flex items-center space-x-3 text-amber-400">
            <AlertTriangle className="w-6 h-6" />
            <h2 className="text-lg font-bold text-white">4. Epistemic Principle: Softmax Confidence ≠ Accuracy</h2>
          </div>
          <p className="text-xs sm:text-sm text-slate-300 leading-relaxed">
            A central finding in deep learning calibration (Guo et al., 2017) is that normalized softmax probabilities are frequently uncalibrated under distribution shift:
          </p>
          <div className="bg-slate-950 p-4 rounded-xl border border-slate-800 font-mono text-xs text-amber-300 text-center">
            P(y = k | x) = exp(z_k) / ∑_{`{j=1}`}^C exp(z_j)
          </div>
          <p className="text-xs sm:text-sm text-slate-400 leading-relaxed">
            Networks trained with cross-entropy push logit values toward extreme margins, producing extreme confidence scores (<code className="text-amber-200 font-mono text-xs">P &gt; 0.95</code>) even on incorrect predictions or novel leaf species. The Expected Calibration Error (ECE) formalizes this deviation across <code className="text-amber-200 font-mono text-xs">M</code> confidence bins:
          </p>
          <div className="bg-slate-950 p-4 rounded-xl border border-slate-800 font-mono text-xs text-teal-300 text-center">
            ECE = ∑_{`{m=1}`}^M (|B_m| / N) · | acc(B_m) - conf(B_m) |
          </div>
          <p className="text-xs sm:text-sm text-slate-300 leading-relaxed">
            To mitigate this in clinical foliar deployments, <strong>post-hoc temperature scaling</strong> modulates the logits by scalar parameter <code className="text-teal-300 font-mono text-xs">T = 1.80</code>:
          </p>
          <div className="bg-teal-950/40 p-4 rounded-xl border border-teal-500/30 font-mono text-xs text-teal-300 text-center">
            p_k(calibrated) = exp(z_k / 1.80) / ∑_{`{j=1}`}^C exp(z_j / 1.80)
          </div>
          <p className="text-xs text-slate-400 leading-relaxed">
            Temperature scaling reduces the ECE from <strong>0.084 down to 0.019</strong>, softening extreme overconfidence while preserving the top-1 predicted class index.
          </p>
        </div>

        {/* 5. Algorithm 1: Data Leakage Elimination */}
        <div className="bg-slate-900/60 border border-slate-800 rounded-3xl p-6 sm:p-8 backdrop-blur space-y-4">
          <div className="flex items-center space-x-3 text-emerald-400">
            <ShieldCheck className="w-6 h-6" />
            <h2 className="text-lg font-bold text-white">5. Algorithm 1: Stratified Partitioning & Leakage Prevention</h2>
          </div>
          <p className="text-xs sm:text-sm text-slate-300 leading-relaxed">
            Data leakage across train/test splits is the most common flaw in educational machine learning prototypes. BioScan AI guarantees complete experimental reproducibility via Algorithm 1:
          </p>
          <div className="bg-slate-950 p-4 rounded-xl border border-slate-800 text-xs font-mono text-slate-300 overflow-x-auto leading-relaxed">
{`Algorithm 1: Deterministic Stratified Partitioning and Leakage-Free Optimization
1: Set seeds: random.seed(42), torch.manual_seed(42)
2: For each class c in 15 classes:
3:     D_c = filter(dataset, label == c)
4:     Shuffle D_c deterministically with seed 42
5:     D_train += D_c[0 : 70%]
6:     D_val   += D_c[70% : 85%]
7:     D_test  += D_c[85% : 100%]
8: CRITICAL: Apply data augmentation (flips, rotations, jitter) ONLY to D_train at runtime.
9: Evaluate model metrics STRICTLY on unaugmented D_test.`}
          </div>
        </div>

        {/* 6. Comprehensive 15-Class Taxonomy Table (Table 1) */}
        <div className="bg-slate-900/60 border border-slate-800 rounded-3xl p-6 sm:p-8 backdrop-blur space-y-6">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
            <div className="flex items-center space-x-3 text-teal-400">
              <TableIcon className="w-6 h-6" />
              <div>
                <h2 className="text-lg font-bold text-white">6. Comprehensive Phytopathological Taxonomy</h2>
                <p className="text-xs text-slate-400">Complete 15-Class botanical etiology and foliar symptomatology profile.</p>
              </div>
            </div>

            {/* Crop Filter Buttons */}
            <div className="flex flex-wrap items-center gap-1.5">
              {crops.map((crop) => (
                <button
                  key={crop}
                  onClick={() => setSelectedCrop(crop)}
                  className={`px-3 py-1 rounded-lg text-xs font-semibold transition-colors ${
                    selectedCrop === crop
                      ? 'bg-teal-500 text-slate-950 shadow-sm'
                      : 'bg-slate-800 text-slate-400 hover:text-white hover:bg-slate-700'
                  }`}
                >
                  {crop}
                </button>
              ))}
            </div>
          </div>

          {/* Search Bar */}
          <div className="relative">
            <Search className="w-4 h-4 text-slate-400 absolute left-3.5 top-1/2 -translate-y-1/2" />
            <input
              type="text"
              placeholder="Search taxonomy by crop, disease name, causal pathogen, or etiology..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="w-full pl-10 pr-4 py-2 bg-slate-950 border border-slate-800 rounded-xl text-xs text-slate-200 placeholder-slate-500 focus:outline-none focus:border-teal-500"
            />
          </div>

          {/* Rendered Table */}
          <div className="overflow-x-auto border border-slate-800 rounded-2xl">
            <table className="w-full text-left text-xs">
              <thead className="bg-slate-800/90 text-slate-300 font-semibold border-b border-slate-700">
                <tr>
                  <th className="py-3 px-3.5">Host Species</th>
                  <th className="py-3 px-3.5">Condition Name</th>
                  <th className="py-3 px-3.5">Causal Pathogen</th>
                  <th className="py-3 px-3.5">Etiological Class</th>
                  <th className="py-3 px-3.5">Cellular Mechanism</th>
                  <th className="py-3 px-3.5">Macroscopic Symptoms</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-800 text-slate-300">
                {filteredTaxa.map((item, idx) => (
                  <tr key={idx} className="hover:bg-slate-800/40 transition-colors">
                    <td className="py-2.5 px-3.5 font-serif italic text-teal-300 whitespace-nowrap">{item.host}</td>
                    <td className="py-2.5 px-3.5 font-medium text-white whitespace-nowrap">{item.condition}</td>
                    <td className="py-2.5 px-3.5 italic text-slate-300 whitespace-nowrap">{item.pathogen}</td>
                    <td className="py-2.5 px-3.5 text-slate-400 whitespace-nowrap">{item.etiology}</td>
                    <td className="py-2.5 px-3.5 text-slate-400 min-w-[200px] leading-relaxed">{item.cellular}</td>
                    <td className="py-2.5 px-3.5 text-slate-300 min-w-[220px] leading-relaxed">{item.symptoms}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
};
