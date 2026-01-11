import torch
import numpy as np
from language_id.model import LanguageIDModel
from language_id.features import extract_mfcc

LANG_MAP = {
    0: "english",
    1: "tamil",
    2: "telugu",
    3: "kannada",
    4: "malayalam"
}

device = "cuda" if torch.cuda.is_available() else "cpu"

model = LanguageIDModel(num_classes=5).to(device)
model.eval()

# NOTE: load trained weights when available
# model.load_state_dict(torch.load("language_id/lid_model.pth", map_location=device))

def predict_language(audio_path):
    mfcc = extract_mfcc(audio_path)
    mfcc = torch.tensor(mfcc).unsqueeze(0).unsqueeze(0).float().to(device)

    with torch.no_grad():
        logits = model(mfcc)
        probs = torch.softmax(logits, dim=1)
        idx = torch.argmax(probs).item()

    return {
        "language": LANG_MAP[idx],
        "confidence": round(probs[0][idx].item(), 3)
    }
