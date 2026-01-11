import librosa

def segment_audio(audio_path, sr=16000, segment_duration=2.0):
    audio, _ = librosa.load(audio_path, sr=sr)
    segment_length = int(sr * segment_duration)

    segments = []
    for i in range(0, len(audio), segment_length):
        chunk = audio[i:i + segment_length]
        if len(chunk) > sr * 0.5:  # ignore very small chunks
            segments.append(chunk)

    return segments
