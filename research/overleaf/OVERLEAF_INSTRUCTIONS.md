# Instructions for Compiling the BioScan AI Research Paper on Overleaf

This research paper is formatted according to standard **IEEE Transactions** double-column journal specifications (`IEEEtran.cls`), which is supported natively out-of-the-box on Overleaf without any extra setup.

All diagrams (Figure 1 and Figure 2) are programmed natively using **LaTeX TikZ**, meaning **you do not need to upload any external image files**.

---

## Method 1: The Quick 2-Minute Overleaf Setup (Recommended)

1. Open your browser and go to [Overleaf](https://www.overleaf.com/).
2. Log in and click **"New Project"** $\to$ **"Blank Project"**.
3. Name your project (e.g., `BioScan_AI_Research_Paper`).
4. In the left file sidebar:
   - Click the **"New File"** icon, name it `references.bib`, and paste the entire contents of [`references.bib`](file:///d:/mydata/Documents/3rd%20sem/BIOLOGY/research/overleaf/references.bib) into it.
   - Open `main.tex` in the Overleaf editor, delete whatever default template text was there, and paste the entire contents of [`main.tex`](file:///d:/mydata/Documents/3rd%20sem/BIOLOGY/research/overleaf/main.tex).
5. Click the green **"Recompile"** button at the top of the preview pane.
6. The full academic research paper PDF will render immediately!

---

## Method 2: Direct Zip Upload to Overleaf

If you prefer uploading a `.zip` archive directly:

1. In Windows PowerShell:
   ```powershell
   cd "d:\mydata\Documents\3rd sem\BIOLOGY\research\overleaf"
   Compress-Archive -Path main.tex, references.bib -DestinationPath BioScan_AI_Overleaf.zip -Force
   ```
2. In Overleaf, click **"New Project"** $\to$ **"Upload Project"**.
3. Select `BioScan_AI_Overleaf.zip`.
4. Overleaf automatically extracts both files and compiles the research paper PDF.

---

## Document Specifications Summary

- **Document Class:** `\documentclass[journal,10pt,twocolumn]{IEEEtran}`
- **Compiler:** `pdfLaTeX` (Default on Overleaf)
- **TeX Live Version:** Any modern TeX Live (2020 through 2026+)
- **Diagrams:** Native LaTeX TikZ vector graphics (Resolution-independent, zero missing asset errors)
- **Bibliography Engine:** BibTeX (`IEEEtran.bst` standard style)

---

## Sections Included in the Research Paper

1. **Title & Academic Affiliation Placeholders** (Editable for student name, mentor, institution)
2. **Abstract & Index Terms** (Formal academic abstract and keyword categorization)
3. **Section I: Introduction** (Agricultural background, crop losses, limitation of manual scouting, computer vision state of the art)
4. **Figure 1 (TikZ Vector Diagram):** End-to-end biological image analysis and inference pipeline
5. **Section II: Theoretical Background and Related Work** (Classical descriptors vs end-to-end CNNs, spatial convolution equations, MobileNetV2 Depthwise Separable Convolutions mathematical derivation)
6. **Figure 2 (TikZ Vector Diagram):** MobileNetV2 Inverted Residual Block with Linear Bottleneck
7. **Section III: Target Botanical Taxa & Phytopathological Profiles** (Taxonomic profiles, host crops, causal agents, symptomatology across 15 classes)
8. **Table I:** Comprehensive Phytopathological Taxonomy and Symptom Table
9. **Section IV: System Architecture & Experimental Methodology** (Byte verification, ImageNet normalization, BioScan-LiteCNN and MobileNetV2 structural specifications, stratified data leakage prevention protocol)
10. **Section V: Experimental Setup & Evaluation Metrics** (Categorical Cross-Entropy, Adam optimizer, precision/recall/F1 formulas, and crucial mathematical proof on why Softmax Confidence $\ne$ Accuracy)
11. **Section VI: Results & Quantitative Analysis** (Authentic held-out test split results table, confusion matrix evaluation, honest empirical disclosure)
12. **Table II:** Held-out test partition quantitative evaluation metrics
13. **Section VII: Software Architecture & Extensibility** (FastAPI REST service, SQLite audit persistence, zero-simulation policy, microscopy/XAI future roadmap)
14. **Section VIII: Conclusion & Acknowledgment**
15. **References:** 15 peer-reviewed scientific citations
