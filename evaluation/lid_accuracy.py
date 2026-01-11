from language_id.infer import predict_language

def evaluate_lid(audio_files, true_labels):
    correct = 0

    for audio, true_lang in zip(audio_files, true_labels):
        pred = predict_language(audio)["language"]
        if pred == true_lang:
            correct += 1

    accuracy = correct / len(audio_files)
    return round(accuracy, 4)


if __name__ == "__main__":
    audio_samples = [
        "demo/audio_samples/english.wav",
        "demo/audio_samples/tamil.wav"
    ]
    labels = ["english", "tamil"]

    print("LID Accuracy:", evaluate_lid(audio_samples, labels))
