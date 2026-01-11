import streamlit as st
import tempfile
import os

from pipeline.safe_voice_pipeline import run_pipeline
from language_id.infer import predict_language
from hate_speech.train import classify


st.set_page_config(
    page_title="SAFE-VOICE",
    page_icon="🎙️",
    layout="centered"
)

st.title("🎙️ SAFE-VOICE")
st.subheader("Multilingual Speech Moderation & Safe TTS System")

st.markdown(
    """
    SAFE-VOICE processes spoken audio in Indian languages,
    detects abusive or hate speech, and generates safe speech output.
    """
)

uploaded_file = st.file_uploader(
    "Upload an audio file (.wav)",
    type=["wav"]
)

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(uploaded_file.read())
        audio_path = tmp.name

    st.audio(audio_path)

    if st.button("Run SAFE-VOICE"):
        with st.spinner("Processing audio..."):
            # Language Detection
            lid = predict_language(audio_path)
            st.markdown(f"**Detected Language:** `{lid['language']}`")
            st.markdown(f"**Language Confidence:** `{lid['confidence']}`")

            # Run full pipeline
            result = run_pipeline(audio_path)

        st.success("Processing complete")

        # Display outputs if returned
        if isinstance(result, dict):
            st.markdown("### 📝 Transcription")
            st.write(result.get("text", ""))

            st.markdown("### 🚨 Abuse Severity")
            st.write(
                f"{result.get('severity')} "
                f"(confidence={round(result.get('confidence', 0), 2)})"
            )

            output_audio = result.get("output_audio")
            if output_audio and os.path.exists(output_audio):
                st.markdown("### 🔊 TTS Output")
                st.audio(output_audio)

    st.markdown("---")
    st.caption("SAFE-VOICE | Responsible AI for Indian Speech Systems")
