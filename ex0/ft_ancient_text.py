import sys
import typing


def print_fragments(content: str) -> None:
    lines = content.splitlines()
    for line in lines:
        print(f"{line}")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{sys.argv[1]}'")

    try:
        file: typing.IO[str] = open(sys.argv[1])
    except (FileNotFoundError, PermissionError,
            IsADirectoryError, OSError) as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
        return

    print("---")
    content = file.read()
    print_fragments(content)
    print("---")
    file.close()
    print(f"File '{sys.argv[1]}' closed.")


if __name__ == "__main__":
    main()
