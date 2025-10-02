# Emotion Recognition from Speech
**Task 2 — Internship Project**

## Overview
A simple prototype web application that accepts a short speech/audio clip, extracts audio features (MFCCs), and predicts the speaker emotion (e.g., happy, sad, angry, neutral). This package includes a Flask backend, a clean responsive UI, and utility scripts to train or run a model.

## Contents
- `app.py` - Flask server (serves UI and prediction endpoint)
- `models/train.py` - Training scaffold (placeholder)
- `models/model_placeholder.pkl` - Placeholder for a saved model (not included)
- `utils/audio_processing.py` - Feature extraction utilities (MFCCs using librosa)
- `templates/index.html` - Frontend HTML (file upload + result display)
- `static/css/style.css` - UI styling (responsive, modern)
- `static/js/main.js` - Frontend JS to upload audio and show results
- `requirements.txt` - Python dependencies
- `sample_audio/` - (empty) place to put example .wav files

## Quick start (local)
1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux / macOS
   venv\Scripts\activate    # Windows PowerShell
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   python app.py
   ```
4. Open http://127.0.0.1:5000 in your browser, upload a short WAV file, and press Predict.

## Notes
- This repo contains a placeholder predict function. Replace it with your trained model (e.g., a scikit-learn or TensorFlow model).
- To train a model, use `models/train.py` as a starting scaffold and store the trained model as `models/model.pkl`.
