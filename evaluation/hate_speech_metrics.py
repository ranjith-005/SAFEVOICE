from sklearn.metrics import classification_report
from hate_speech.train import classify

def evaluate_hate_speech(texts, true_labels):
    preds = []

    for text in texts:
        severity, _ = classify(text)
        preds.append(severity)

    report = classification_report(true_labels, preds)
    return report


if __name__ == "__main__":
    texts = [
        "i want help",
        "this is stupid",
        "you are useless"
    ]
    labels = [
        "safe",
        "mild_abuse",
        "severe_hate"
    ]

    print(evaluate_hate_speech(texts, labels))
