# BioScan AI – Architecture Overview

## System Hierarchy
```
BioScan-AI/
├── backend/                  # Python FastAPI Server + PyTorch Engine
│   ├── app/
│   │   ├── main.py           # FastAPI application entrypoint & CORS
│   │   ├── config.py         # App configuration & runtime path resolution
│   │   ├── routes/           # REST endpoints (/health, /classes, /predict, /history, /metrics)
│   │   ├── services/         # Preprocessing, inference logic, botanical knowledge base
│   │   ├── database/         # SQLite persistence DAO
│   │   ├── models/           # Data definitions
│   │   └── schemas/          # Pydantic validation schemas
│   ├── ml/
│   │   ├── config.py         # ML hyperparameters, seeds, paths
│   │   ├── model.py          # MobileNetV2 & BioScanLiteCNN PyTorch modules
│   │   ├── dataset.py        # Stratified splitting & transform pipelines
│   │   ├── train.py          # Repeatable training script
│   │   ├── evaluate.py       # Test set evaluation & confusion matrix
│   │   └── predict.py        # Service-level PyTorch predictor
│   ├── data/                 # Raw leaf specimens and processed partitions
│   ├── saved_models/         # Checkpoints (.pth), classes (.json), metrics (.json)
│   ├── tests/                # Automated API and ML unit tests
│   └── requirements.txt      # Python dependencies
│
├── frontend/                 # React + Vite + TypeScript Client
│   ├── src/
│   │   ├── components/       # Navbar, Footer, UI components
│   │   ├── pages/            # Home, Analysis, Results, Dashboard, Methodology, About
│   │   ├── services/         # Centralized API fetch service
│   │   ├── types/            # TypeScript data contracts
│   │   ├── utils/            # Botanical sample leaves and canvas converters
│   │   ├── App.tsx           # Main application state and routing
│   │   └── index.css         # Tailwind CSS v4 styling
│   └── package.json
│
├── research/                 # Academic Research Deliverables
│   ├── research_paper.md     # Full academic paper draft
│   ├── methodology.md        # Technical methodology specification
│   ├── experiment_log.md     # Experiment logs and hardware records
│   ├── results_table.md      # Quantitative metrics table
│   └── references.md         # Academic bibliography
│
├── docs/                     # Technical specifications
│   ├── architecture.md
│   └── api_spec.md
│
├── README.md                 # Complete setup, execution, and training manual
└── .gitignore                # Production ignore patterns
```

## Security & Reliability Design
- **Path Isolation:** No internal server paths or local disk hierarchies are exposed in API payloads. All filenames returned to client are stripped via `Path(filename).name`.
- **Payload Verification:** Every uploaded file is verified via Pillow header checking before any tensor operations take place.
- **Fail-Safe Inference:** When weights are absent, an explicit HTTP 503 is returned explaining that real model weights must be trained, preventing misleading results.
