from TTS.api import TTS

tts = TTS(model_name="tts_models/ml/css10/vits")

def speak(text, out_path="output_ml.wav"):
    tts.tts_to_file(text=text, file_path=out_path)
