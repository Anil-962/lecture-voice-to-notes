import streamlit as st
import tempfile
import os
from src.pipeline import lecture_to_study_material

@st.cache_data(show_spinner=False)
def cached_generation(audio_path: str):
    return lecture_to_study_material(audio_path)


st.set_page_config(
    page_title="Lecture Voice-to-Notes Generator",
    layout="centered"
)

st.title("Lecture Voice-to-Notes Generator")
st.write(
    "Upload a lecture audio file and generate structured study notes, quizzes, and flashcards."
)

audio_file = st.file_uploader(
    "Upload lecture audio (mp3 or wav)",
    type=["mp3", "wav"]
)

audio_path = None

if audio_file is not None:
    # Create a temp file that persists
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tmp.write(audio_file.read())
        audio_path = tmp.name

    st.success("Audio uploaded successfully.")

if audio_path and st.button("Generate Study Material"):
    try:
        with st.spinner("Processing lecture. Please wait..."):
            notes, quiz, flashcards = cached_generation(audio_path)


        st.subheader("Study Notes")
        st.text_area("Notes", notes, height=300)

        st.subheader("Quiz")
        st.text_area("Quiz", quiz, height=250)

        st.subheader("Flashcards")
        st.text_area("Flashcards", flashcards, height=250)

    except Exception as e:
        st.error(f"Error occurred: {e}")

    finally:
        # Cleanup temp file AFTER processing
        if os.path.exists(audio_path):
            os.remove(audio_path)
import streamlit as st
from src.pipeline import lecture_to_study_material

@st.cache_data(show_spinner=False)
def cached_generation(audio_path):
    return lecture_to_study_material(audio_path)
