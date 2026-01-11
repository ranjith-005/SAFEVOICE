from language_id.segment import segment_audio
from language_id.infer import predict_language
from asr.router import transcribe_segment

from hate_speech.train import classify
from decision_engine.policy import decide
from tts.english.tts import speak as tts_en
from tts.tamil.tts import speak as tts_ta
from tts.telugu.tts import speak as tts_te


def run_pipeline(audio_path):
    print("🔹 Running SAFE-VOICE (Code-Switched Mode)")

    segments = segment_audio(audio_path)
    full_text = []
    detected_languages = []

    for seg in segments:
        lid = predict_language(audio_path)
        language = lid["language"]
        detected_languages.append(language)

        text = transcribe_segment(seg, language)
        full_text.append(f"[{language.upper()}] {text}")

    final_text = " ".join(full_text)
    print("Final Transcription:", final_text)

    # Severity-based abuse detection
    severity, score = classify(final_text)
    print("Severity:", severity, "Confidence:", round(score, 2))

    decision = decide(severity)

    # Speak response
    if decision["allow"]:
        if "tamil" in detected_languages:
            tts_ta(final_text)
        elif "telugu" in detected_languages:
            tts_te(final_text)
        else:
            tts_en(final_text)
    else:
        tts_en(decision["message"])


if __name__ == "__main__":
    run_pipeline("demo/audio_samples/sample.wav")
      
      return {
        "text": final_text if 'final_text' in locals() else text,
        "severity": severity,
        "confidence": score,
        "output_audio": "output.wav"
    }
