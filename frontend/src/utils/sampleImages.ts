/**
 * Synthetic and sample plant leaf images for instant UI validation.
 * Encoded as SVG Data URIs representing biological foliar morphologies.
 */

export interface SampleLeaf {
  id: string;
  name: string;
  plant: string;
  condition: string;
  isHealthy: boolean;
  filename: string;
  dataUri: string;
}

// Generates high quality botanical SVG data URIs
function createLeafSvgUri(leafColor: string, spotsColor: string | null, _type: 'compound' | 'simple' | 'ovate'): string {
  const spots = spotsColor ? `
    <circle cx="85" cy="85" r="9" fill="${spotsColor}" opacity="0.9" />
    <circle cx="130" cy="120" r="14" fill="${spotsColor}" opacity="0.85" />
    <circle cx="95" cy="155" r="8" fill="${spotsColor}" opacity="0.9" />
    <circle cx="115" cy="140" r="6" fill="#f59e0b" opacity="0.8" />
    <circle cx="75" cy="110" r="7" fill="${spotsColor}" opacity="0.85" />
  ` : '';

  const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="224" height="224">
    <rect width="200" height="200" fill="#f8fafc" />
    <g transform="translate(10, 10)">
      <!-- Leaf blade -->
      <path d="M90 10 C140 40 160 110 90 170 C20 110 40 40 90 10 Z" fill="${leafColor}" stroke="#15803d" stroke-width="2.5" />
      <!-- Midrib -->
      <path d="M90 15 L90 175" stroke="#166534" stroke-width="2.5" stroke-linecap="round" />
      <!-- Veins -->
      <path d="M90 45 L50 65 M90 45 L130 65" stroke="#166534" stroke-width="1.8" stroke-linecap="round" />
      <path d="M90 75 L45 100 M90 75 L135 100" stroke="#166534" stroke-width="1.8" stroke-linecap="round" />
      <path d="M90 105 L45 130 M90 105 L135 130" stroke="#166534" stroke-width="1.8" stroke-linecap="round" />
      <path d="M90 135 L55 155 M90 135 L125 155" stroke="#166534" stroke-width="1.8" stroke-linecap="round" />
      ${spots}
    </g>
  </svg>`;

  return `data:image/svg+xml;utf8,${encodeURIComponent(svg)}`;
}

export const SAMPLE_LEAVES: SampleLeaf[] = [
  {
    id: 'sample-apple-healthy',
    name: 'Apple Foliage (Healthy)',
    plant: 'Apple',
    condition: 'Healthy Leaf',
    isHealthy: true,
    filename: 'sample_apple_healthy.png',
    dataUri: createLeafSvgUri('#16a34a', null, 'ovate')
  },
  {
    id: 'sample-apple-scab',
    name: 'Apple Scab Lesion',
    plant: 'Apple',
    condition: 'Apple Scab (Venturia inaequalis)',
    isHealthy: false,
    filename: 'sample_apple_scab.png',
    dataUri: createLeafSvgUri('#4d7c0f', '#3f3f46', 'ovate')
  },
  {
    id: 'sample-tomato-healthy',
    name: 'Tomato Foliage (Healthy)',
    plant: 'Tomato',
    condition: 'Healthy Foliage',
    isHealthy: true,
    filename: 'sample_tomato_healthy.png',
    dataUri: createLeafSvgUri('#22c55e', null, 'compound')
  },
  {
    id: 'sample-tomato-blight',
    name: 'Tomato Early Blight',
    plant: 'Tomato',
    condition: 'Early Blight (Alternaria solani)',
    isHealthy: false,
    filename: 'sample_tomato_early_blight.png',
    dataUri: createLeafSvgUri('#65a30d', '#713f12', 'compound')
  },
  {
    id: 'sample-corn-rust',
    name: 'Corn Rust Pustules',
    plant: 'Corn',
    condition: 'Common Rust (Puccinia sorghi)',
    isHealthy: false,
    filename: 'sample_corn_common_rust.png',
    dataUri: createLeafSvgUri('#84cc16', '#b45309', 'simple')
  },
  {
    id: 'sample-carrot-healthy',
    name: 'Carrot Lace Leaf',
    plant: 'Carrot',
    condition: 'Healthy Leaf (Daucus carota)',
    isHealthy: true,
    filename: 'sample_carrot_healthy.jpg',
    dataUri: createLeafSvgUri('#15803d', null, 'compound')
  },
  {
    id: 'sample-neem-healthy',
    name: 'Neem Medicinal Leaf',
    plant: 'Neem',
    condition: 'Healthy Leaf (Azadirachta indica)',
    isHealthy: true,
    filename: 'sample_neem_healthy.jpg',
    dataUri: createLeafSvgUri('#166534', null, 'compound')
  },
  {
    id: 'sample-tulsi-healthy',
    name: 'Tulsi Holy Basil',
    plant: 'Tulsi',
    condition: 'Healthy Leaf (Ocimum sanctum)',
    isHealthy: true,
    filename: 'sample_tulsi_healthy.jpg',
    dataUri: createLeafSvgUri('#15803d', null, 'ovate')
  },
  {
    id: 'sample-papaya-healthy',
    name: 'Papaya Palmate Leaf',
    plant: 'Papaya',
    condition: 'Healthy Leaf (Carica papaya)',
    isHealthy: true,
    filename: 'sample_papaya_healthy.jpg',
    dataUri: createLeafSvgUri('#16a34a', null, 'compound')
  },
  {
    id: 'sample-mango-healthy',
    name: 'Mango Waxy Leaf',
    plant: 'Mango',
    condition: 'Healthy Leaf (Mangifera indica)',
    isHealthy: true,
    filename: 'sample_mango_healthy.jpg',
    dataUri: createLeafSvgUri('#14532d', null, 'simple')
  },
  {
    id: 'sample-money-plant-healthy',
    name: 'Money Plant (Pothos)',
    plant: 'Money_Plant',
    condition: 'Healthy Leaf (Epipremnum aureum)',
    isHealthy: true,
    filename: 'sample_money_plant.jpg',
    dataUri: createLeafSvgUri('#15803d', null, 'ovate')
  }
];

export async function dataUriToFile(dataUri: string, filename: string): Promise<File> {
  // Convert SVG data URI to a real PNG/JPEG File via canvas for model ingestion
  return new Promise((resolve) => {
    const img = new Image();
    img.crossOrigin = 'anonymous';
    img.onload = () => {
      const canvas = document.createElement('canvas');
      canvas.width = 224;
      canvas.height = 224;
      const ctx = canvas.getContext('2d');
      if (ctx) {
        ctx.fillStyle = '#ffffff';
        ctx.fillRect(0, 0, 224, 224);
        ctx.drawImage(img, 0, 0, 224, 224);
      }
      canvas.toBlob((blob) => {
        if (blob) {
          const file = new File([blob], filename, { type: 'image/jpeg' });
          resolve(file);
        }
      }, 'image/jpeg', 0.95);
    };
    img.src = dataUri;
  });
}
