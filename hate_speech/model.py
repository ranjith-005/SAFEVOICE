from transformers import AutoModelForSequenceClassification

def load_model():
    return AutoModelForSequenceClassification.from_pretrained(
        "cardiffnlp/twitter-xlm-roberta-base-offensive"
    )
