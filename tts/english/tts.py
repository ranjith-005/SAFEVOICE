from TTS.api import TTS

tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC")

def speak(text, out="output.wav"):
    tts.tts_to_file(text=text, file_path=out)
