def secure_archive(filename: str, action: str = "r",
                   content: str = "") -> tuple[bool, str]:
    if action not in ("r", "w"):
        return (False, f"Wrong action provided: {action}. Select 'r' or 'w'")

    try:
        with open(filename, action) as f:
            if action == "r":
                file_content = f.read()
                return (True, file_content)
            else:
                f.write(content)
                return (True, "Content successfully written to file")

    except (FileNotFoundError, PermissionError,
            IsADirectoryError, OSError) as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===")

    res = secure_archive("/not/existing/file")
    print("\nUsing 'secure_archive' to read from a nonexistent file: ")
    print(f"{res}\n")

    res = secure_archive("/etc/master.passwd")
    print("\nUsing 'secure_archive' to read from an inaccessible file: ")
    print(f"{res}\n")

    res = secure_archive("test.txt")
    print("\nUsing 'secure_archive' to read from a regular file: ")
    print(f"{res}\n")

    res = secure_archive("test.txt", "w", "This is content")
    print("\nUsing 'secure_archive' to write previous content to a new file: ")
    print(f"{res}")


if __name__ == "__main__":
    main()
