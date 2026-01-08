# 🎙️ Lecture Voice-to-Notes Generator

An offline AI-based system that converts lecture audio into structured study material including notes, quizzes, and flashcards.  
Designed for students who miss key points during lectures due to the difficulty of listening and writing simultaneously.

This project uses **Speech-to-Text (Whisper)** and **offline NLP models** to ensure zero API cost and reliable execution.

---

## 📌 Problem Statement

Students often fail to capture complete lecture notes because real-time listening and note-taking is difficult.  
There is a need for an automated system that can:
- Convert spoken lectures into text
- Summarize content into study notes
- Generate quizzes and flashcards for revision

---

## 💡 Proposed Solution

The system accepts a recorded lecture audio file and performs:
1. Speech-to-text transcription
2. Text preprocessing and cleaning
3. Chunk-based hierarchical summarization
4. Automatic quiz and flashcard generation
5. Export of outputs as downloadable PDFs

All processing is performed **offline**, eliminating dependency on paid APIs.

---

## 🏗️ System Architecture
Audio File
↓
Whisper (Speech-to-Text)
↓
Text Cleaning & Chunking
↓
Offline Summarization Model
↓
Notes | Quiz | Flashcards
↓
PDF Export + Streamlit UI


---

## 🧠 Technologies Used

- Python 3.10+
- OpenAI Whisper (offline speech recognition)
- Hugging Face Transformers (offline summarization)
- Streamlit (web UI)
- ReportLab (PDF generation)
- FFmpeg (audio decoding)

---

## 📁 Project Structure

lecture-voice-to-notes/
│
├── src/
│ ├── speech_to_text.py
│ ├── text_preprocessing.py
│ ├── summarizer.py
│ ├── quiz_generator.py
│ ├── flashcard_generator.py
│ ├── pipeline.py
│ └── pdf_utils.py
│
├── ui/
│ └── app.py
│
├── requirements.txt
└── README.md


---

## ▶️ How to Run the Project

### 1️⃣ Create Virtual Environment
```bash
python -m venv .venv
.venv\Scripts\activate

