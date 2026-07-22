"""Rebuilt text utility exercises for Day 7 review."""


def clean_text(text: str) -> str:
    """Remove extra spaces and convert text to lowercase."""
    words: list[str] = text.strip().lower().split()

    return " ".join(words)


def count_words(text: str) -> int:
    """Return the number of words in the supplied text."""
    cleaned_text: str = clean_text(text)

    if not cleaned_text:
        return 0

    words: list[str] = cleaned_text.split()

    return len(words)


def main() -> None:
    sample_texts: list[str] = [
        "   Hello     WORLD   ",
        "  Python   Is   Great  ",
        "     ",
    ]

    for text in sample_texts:
        cleaned_text: str = clean_text(text)
        word_count: int = count_words(text)

        print(f"Original: {text!r}")
        print(f"Cleaned: {cleaned_text!r}")
        print(f"Word count: {word_count}")
        print()


if __name__ == "__main__":
    main()