def generate_quiz(notes: str) -> str:
    lines = [line.strip() for line in notes.split(".") if len(line.strip()) > 40]

    quiz = []
    for i, line in enumerate(lines[:5], start=1):
        quiz.append(f"Q{i}. Explain: {line}?")

    if not quiz:
        return "Unable to generate quiz."

    return "\n".join(quiz)
