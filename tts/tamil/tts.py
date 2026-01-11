from TTS.api import TTS

# Tamil TTS model (Indic / community-trained)
tts = TTS(model_name="tts_models/ta/css10/vits")

def speak(text, out_path="output_ta.wav"):
    tts.tts_to_file(text=text, file_path=out_path)
