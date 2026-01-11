import time
from pipeline.safe_voice_pipeline import run_pipeline

def measure_latency(audio_path):
    start = time.time()
    run_pipeline(audio_path)
    end = time.time()

    return round(end - start, 2)


if __name__ == "__main__":
    print(
        "End-to-End Latency (sec):",
        measure_latency("demo/audio_samples/sample.wav")
    )
