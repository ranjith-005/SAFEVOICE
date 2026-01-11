from TTS.api import TTS

# Telugu TTS model
tts = TTS(model_name="tts_models/te/css10/vits")

def speak(text, out_path="output_te.wav"):
    tts.tts_to_file(text=text, file_path=out_path)
