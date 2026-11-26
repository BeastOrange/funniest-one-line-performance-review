import sys
from pathlib import Path

REVIEW = (
    "Exceeds Expectations for delegation — he outsourced his own performance review to the employee being reviewed."
)


def validate(text: str) -> None:
    if not text or not text.strip():
        raise SystemExit("Review must not be empty or whitespace only.")
    if "\n" in text or "\r" in text:
        raise SystemExit("Review must be a single line without newline characters.")
    if not (1 <= len(text) <= 140):
        raise SystemExit(
            f"Review must be between 1 and 140 characters long (got {len(text)})."
        )


def main() -> None:
    validate(REVIEW)

    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(REVIEW + "\n", encoding="utf-8")

    print(REVIEW)
    print(f"Character count: {len(REVIEW)}")


if __name__ == "__main__":
    main()
