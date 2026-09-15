import sys
import typing


def print_fragments(content: str) -> None:
    lines = content.splitlines()
    for line in lines:
        print(f"{line}")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    print("=== Cyber Archives Recovery & Preservation ===")
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

    new_lines: list[str] = []
    print("Transform data:")
    for line in content.splitlines():
        new_lines.append(line + "#")

    new_content: str = "\n".join(new_lines)
    print("---")
    print_fragments(new_content)
    print("---")

    new_filename = input("Enter new file name (or empty): ")
    if new_filename == "":
        print("Not saving data.")
    else:
        try:
            print(f"Saving data to '{new_filename}'")
            out = open(new_filename, "w")
            try:
                out.write(new_content)
            finally:
                out.close()
            print(f"Data saved in file '{new_filename}'.")
        except (FileNotFoundError, PermissionError,
                IsADirectoryError, OSError) as e:
            print(f"Error opening file '{new_filename}': {e}")


if __name__ == "__main__":
    main()
