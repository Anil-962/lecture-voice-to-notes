from transformers import pipeline

# Load once (important for performance)
_summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

def generate_notes(text: str) -> str:
    if len(text.strip()) < 50:
        return "Not enough content to summarize."

    summary = _summarizer(
        text,
        max_length=180,
        min_length=80,
        do_sample=False
    )

    return summary[0]["summary_text"]
from transformers import pipeline

_summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6"
)

def generate_notes(text: str) -> str:
    if len(text) < 200:
        return "Content too short to summarize."

    result = _summarizer(
        text,
        max_length=150,
        min_length=60,
        do_sample=False
    )

    return result[0]["summary_text"]
