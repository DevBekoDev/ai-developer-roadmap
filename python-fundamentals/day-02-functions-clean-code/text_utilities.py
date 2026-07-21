"""Utility functions for processing text."""


def clean_text(text: str) -> str:
    """Clean text by removing extra spaces and converting it to lowercase."""
    words: list[str] = text.strip().lower().split()
    cleaned_text: str = " ".join(words)

    return cleaned_text


def count_words(text: str) -> int:
    """Count the number of words in a piece of text."""
    cleaned_text: str = clean_text(text)

    if not cleaned_text:
        return 0

    words: list[str] = cleaned_text.split()

    return len(words)


def main() -> None:
    original_text: str = input("Enter some text: ")

    cleaned_text: str = clean_text(original_text)
    word_count: int = count_words(original_text)

    print(f"Original text: {original_text}")
    print(f"Cleaned text: {cleaned_text}")
    print(f"Word count: {word_count}")


if __name__ == "__main__":
    main()