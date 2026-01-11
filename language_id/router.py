import soundfile as sf
import tempfile

from asr.english.asr import transcribe as asr_en
from asr.tamil.asr import transcribe as asr_ta
from asr.telugu.asr import transcribe as asr_te

def transcribe_segment(audio_segment, language, sr=16000):
    with tempfile.NamedTemporaryFile(suffix=".wav") as f:
        sf.write(f.name, audio_segment, sr)

        if language == "tamil":
            return asr_ta(f.name)
        elif language == "telugu":
            return asr_te(f.name)
        else:
            return asr_en(f.name)
