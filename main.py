from pathlib import Path

REVIEW = (
    "Exceeds Expectations for delegation — he outsourced his own performance review to the employee being reviewed."
)


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(REVIEW + "\n", encoding="utf-8")

    print(REVIEW)
    print(f"Character count: {len(REVIEW)}")


if __name__ == "__main__":
    main()
