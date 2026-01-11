import librosa
import numpy as np

def extract_mfcc(audio_path, sr=16000, n_mfcc=40):
    audio, _ = librosa.load(audio_path, sr=sr, mono=True)
    mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=n_mfcc)
    mfcc = (mfcc - mfcc.mean()) / (mfcc.std() + 1e-6)
    return mfcc
