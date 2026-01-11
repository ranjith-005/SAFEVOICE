from transformers import pipeline
from hate_speech.labels import SAFE, MILD, SEVERE

classifier = pipeline(
    "text-classification",
    model="cardiffnlp/twitter-xlm-roberta-base-offensive",
    return_all_scores=True
)

def classify(text):
    scores = classifier(text)[0]

    offensive_score = 0.0
    for s in scores:
        if "offensive" in s["label"].lower():
            offensive_score = s["score"]

    # Severity thresholds (tunable)
    if offensive_score < 0.30:
        return SAFE, offensive_score
    elif offensive_score < 0.70:
        return MILD, offensive_score
    else:
        return SEVERE, offensive_score
