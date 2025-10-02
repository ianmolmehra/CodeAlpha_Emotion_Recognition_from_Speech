from flask import Flask, render_template, request, jsonify
import os
from utils.audio_processing import extract_features_from_file
import random
import numpy as np
import joblib

app = Flask(__name__)
MODEL_PATH = os.path.join('models', 'model_placeholder.pkl')

# Try loading a trained model; fallback to dummy if unavailable
model = None
try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    print('Model not found or failed to load; using dummy predictor.', e)
    model = None

EMOTIONS = ['neutral', 'happy', 'sad', 'angry', 'fearful', 'surprised']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'audio' not in request.files:
        return jsonify({'error': 'no file provided'}), 400
    f = request.files['audio']
    temp_path = os.path.join('temp', f.filename)
    os.makedirs('temp', exist_ok=True)
    f.save(temp_path)
    # extract features
    try:
        features = extract_features_from_file(temp_path)
    except Exception as e:
        return jsonify({'error': 'failed to process audio', 'details': str(e)}), 500

    # If a real model is loaded, predict; else return a dummy random label (stable pseudo-random)
    if model is not None:
        pred = model.predict([features])[0]
    else:
        rng = np.sum(np.abs(features))  # deterministic-ish
        idx = int(rng) % len(EMOTIONS)
        pred = EMOTIONS[idx]

    return jsonify({'emotion': pred})

if __name__ == '__main__':
    app.run(debug=True)
