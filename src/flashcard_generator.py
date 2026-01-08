def generate_flashcards(notes: str) -> str:
    sentences = [s.strip() for s in notes.split(".") if len(s.strip()) > 30]

    flashcards = []
    for s in sentences[:5]:
        flashcards.append(f"Q: What does this mean?\nA: {s}\n")

    if not flashcards:
        return "Unable to generate flashcards."

    return "\n".join(flashcards)
