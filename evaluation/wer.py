import jiwer

def compute_wer(reference_texts, predicted_texts):
    """
    reference_texts: list of ground truth strings
    predicted_texts: list of ASR output strings
    """
    wer = jiwer.wer(reference_texts, predicted_texts)
    return round(wer, 4)


if __name__ == "__main__":
    refs = [
        "i want to apply for internship",
        "this service is very slow"
    ]
    preds = [
        "i want apply for internship",
        "this service is very slow"
    ]

    print("WER:", compute_wer(refs, preds))
