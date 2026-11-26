# BioScan AI – AI-Based Biological Foliar Image Analysis

[![GitHub Repository](https://img.shields.io/badge/GitHub-HARSHA--18811%2FBioScan--AI-blue?logo=github)](https://github.com/HARSHA-18811/BioScan-AI)
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/HARSHA-18811/BioScan-AI)

- **Official GitHub Repository:** [https://github.com/HARSHA-18811/BioScan-AI](https://github.com/HARSHA-18811/BioScan-AI)
- **Live Vercel Web Deployment:** [https://rapid-birch-14hgmmc.tmp.now](https://rapid-birch-14hgmmc.tmp.now) (or connect directly via Vercel GitHub Integration)

An academic experiential-learning and research-oriented web application exploring the application of deep convolutional neural networks (CNNs) to biological foliar pathology and botanical disease classification.

---

## 1. Project Overview & Research Objective

**BioScan AI** is designed to explore how modern deep learning can be reliably applied to biological imagery without optimistic reporting bias or simulated outcomes. The system focuses on **Plant Leaf Disease Classification**, identifying both healthy vegetative foliage and specific disease classes across agricultural crops.

### Key Tenets:
- **No Fake Predictions:** BioScan AI strictly requires an actual trained model checkpoint to produce inference. If a model is not configured, the system transparently reports an unconfigured state.
- **Data Leakage Mitigation:** Stratified sampling with fixed random seeds (`seed=42`) guarantees zero specimen leakage between training, validation, and testing partitions.
- **Transparent Metrics:** Statistical softmax confidence is clearly differentiated from empirical test accuracy. Uncalculated metrics display an explicit "Not evaluated yet" state.
- **Modular Architecture:** Decoupled design allows future integration of cellular microscopy, stomatal analysis, or cloud datastores (Supabase).

---

## 2. Technology Stack

### Frontend:
- **Framework:** React 19 + TypeScript + Vite
- **Styling:** Tailwind CSS v4 (Dark navy laboratory scientific theme)
- **Icons:** Lucide React
- **Data Visualization:** Recharts (Class distributions, confidence histograms)

### Backend:
- **Language & Framework:** Python 3.12 + FastAPI + Uvicorn
- **Image Processing:** Pillow (PIL) + NumPy
- **Deep Learning:** PyTorch 2.x (CPU / CUDA compatible)
- **Evaluation:** Scikit-learn (Precision, Recall, F1, Confusion Matrix)
- **Database:** Local SQLite database (persisting analysis audit trails)

---

## 3. Project Directory Structure

```text
BioScan-AI/
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI app & CORS middleware
│   │   ├── config.py            # App settings & directory paths
│   │   ├── routes/              # Health, Predict, Classes, History, Metrics
│   │   ├── services/            # Preprocessing, Predictor, Plant Knowledge Base
│   │   ├── database/            # SQLite DAO operations
│   │   └── schemas/             # Pydantic v2 validation models
│   ├── ml/
│   │   ├── config.py            # Hyperparameters, random seed, class lists
│   │   ├── model.py             # MobileNetV2 and BioScanLiteCNN architectures
│   │   ├── dataset.py           # Stratified splitting and transforms
│   │   ├── train.py             # Reproducible training pipeline
│   │   ├── evaluate.py          # Test-set evaluation and confusion matrix
│   │   └── predict.py           # Production inference module
│   ├── data/                    # Raw leaf specimens and processed splits
│   ├── saved_models/            # Serialized weights, metadata, metrics
│   ├── tests/                   # Automated API and ML unit tests
│   └── requirements.txt         # Python dependencies
├── frontend/
│   ├── src/
│   │   ├── components/          # Navbar, Footer
│   │   ├── pages/               # Home, Analysis, Results, Dashboard, Methodology, About
│   │   ├── services/            # Centralized API service
│   │   ├── types/               # TypeScript contracts
│   │   └── utils/               # Instant test calibration leaves
│   ├── package.json
│   └── vite.config.ts
├── research/
│   ├── research_paper.md        # Academic research paper draft
│   ├── methodology.md           # Research methodology documentation
│   ├── experiment_log.md        # Experiment tracking logs
│   ├── results_table.md         # Quantitative results table
│   └── references.md            # Scientific bibliography
├── docs/
│   ├── architecture.md          # System architectural overview
│   └── api_spec.md              # REST API contract
├── README.md
└── .gitignore
```

---

## 4. Prerequisites (Checking Environment)

Before running the application, verify that **Python** and **Node.js** are installed on your Windows machine:

Open **Windows PowerShell** and run:

```powershell
python --version
node --version
npm --version
```

- **Python:** Recommended `3.10` to `3.12`. If not installed, download from [python.org](https://www.python.org/).
- **Node.js:** Recommended `18.x` or newer (tested on Node v24). If not installed, download from [nodejs.org](https://nodejs.org/).

---

## 5. Backend Installation & Execution

### Step 1: Navigate to the backend directory
```powershell
cd "d:\mydata\Documents\3rd sem\BIOLOGY\backend"
```

### Step 2: Create and activate a virtual environment (Optional but Recommended)
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### Step 3: Install Dependencies
```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```
*(PyTorch CPU can also be installed directly via: `pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu`)*

### Step 4: Run Automated Tests
Verify all 8 unit tests pass:
```powershell
python -m pytest tests/
```

### Step 5: Start the FastAPI Backend Server
```powershell
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```
The backend API will be live at:
- Root: `http://127.0.0.1:8000/`
- Interactive Swagger Documentation: `http://127.0.0.1:8000/docs`
- Health check: `http://127.0.0.1:8000/health`

---

## 6. Frontend Installation & Execution

Open a **separate Windows PowerShell terminal**:

### Step 1: Navigate to the frontend directory
```powershell
cd "d:\mydata\Documents\3rd sem\BIOLOGY\frontend"
```

### Step 2: Install Node Modules
```powershell
npm install
```

### Step 3: Start the Vite Development Server
```powershell
npm run dev
```

Open your browser to:
**`http://localhost:5173`**

---

## 7. How to Add Your Dataset & Train a Model

### 7.1 Obtaining the Dataset (PlantVillage)
The default classes conform to the **PlantVillage** dataset:
- **Source:** [PlantVillage on Mendeley Data / Kaggle](https://www.kaggle.com/datasets/emmarex/plantdisease)
- **Licence:** Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
- **Citation:** Hughes, D., & Salathé, M. (2015). An open access repository of images on plant health to enable the development of mobile disease diagnostics. *arXiv:1511.08060*.

### 7.2 Directory Layout for Your Dataset
Organize downloaded folders inside `backend/data/raw/` using class subfolders:

```text
backend/data/raw/
├── Apple___Apple_scab/
│   ├── image1.jpg
│   └── image2.jpg
├── Apple___Black_rot/
├── Apple___Cedar_apple_rust/
├── Apple___healthy/
├── Corn___Common_rust/
├── Corn___Northern_Leaf_Blight/
├── Corn___healthy/
├── Grape___Black_rot/
├── Grape___healthy/
├── Potato___Early_blight/
├── Potato___Late_blight/
├── Potato___healthy/
├── Tomato___Bacterial_spot/
├── Tomato___Early_blight/
└── Tomato___healthy/
```

### 7.3 Files to Edit when Adding New Classes
1. **`backend/ml/config.py`**: Add new class folder names to `DEFAULT_CLASSES`.
2. **`backend/app/services/plant_knowledge.py`**: Add botanical details (scientific name, pathogen type, symptoms, management) to `CLASS_KNOWLEDGE_BASE`.

### 7.4 Running Model Training
Execute the training pipeline from the project root or backend folder:
```powershell
# Quick CPU training using BioScan-LiteCNN:
python backend/ml/train.py --arch lite --epochs 10 --batch_size 16

# MobileNetV2 Transfer Learning:
python backend/ml/train.py --arch mobilenet_v2 --epochs 15 --batch_size 16
```
This automatically saves:
- Model weights: `backend/saved_models/bioscan_mobilenet.pth`
- Class labels: `backend/saved_models/classes.json`
- Model metadata: `backend/saved_models/model_metadata.json`

### 7.5 Running Model Evaluation
Compute real test accuracy, precision, recall, F1, and confusion matrix:
```powershell
python backend/ml/evaluate.py --arch lite
```
Metrics are recorded in `backend/saved_models/evaluation_metrics.json` and instantly appear in the **Research Dashboard** UI.

---

## 8. Academic Prototype Disclaimer

> **Important:** BioScan AI is an educational research prototype designed for experiential learning in biological image analysis. Its predictions are not a substitute for certified plant pathology assessment, professional agronomist field scouting, or laboratory microbial assays. Statistical confidence indicates mathematical softmax probability, not guaranteed real-world diagnosis.
