from src.speech_to_text import speech_to_text
from src.text_preprocessing import clean_text, chunk_for_summarization
from src.summarizer import generate_notes
from src.quiz_generator import generate_quiz
from src.flashcard_generator import generate_flashcards

def lecture_to_study_material(audio_path: str):
    transcript = speech_to_text(audio_path)
    transcript = clean_text(transcript)

    # SAFE chunking for summarization
    chunks = chunk_for_summarization(transcript)

    summary_parts = []
    for chunk in chunks:
        summary_parts.append(generate_notes(chunk))

    full_notes = " ".join(summary_parts)

    quiz = generate_quiz(full_notes)
    flashcards = generate_flashcards(full_notes)

    return full_notes, quiz, flashcards
