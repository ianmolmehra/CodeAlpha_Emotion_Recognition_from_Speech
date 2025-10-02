import librosa
import numpy as np

def extract_features_from_file(path, sr=22050, n_mfcc=13):
    """Load an audio file and extract a fixed-size MFCC feature vector (mean + std of MFCCs).

    Returns a 1-D numpy array of length n_mfcc*2 (mean & std for each coefficient).
    """
    y, _ = librosa.load(path, sr=sr, mono=True)
    # ensure at least 0.5s
    if len(y) < 0.1*sr:
        raise ValueError('Audio too short; please provide at least 0.1s')
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)
    mfcc_mean = mfcc.mean(axis=1)
    mfcc_std = mfcc.std(axis=1)
    features = np.concatenate([mfcc_mean, mfcc_std])
    return features
