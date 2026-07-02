def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int('abc')
    elif operation_number == 1:
        5 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        1 + "abc"
    else:
        return


def test_error_types() -> None:
    op = 0
    print("=== Garden Error Types Demo ===")

    while op < 5:
        print(f"Testing operation {op}...")
        try:
            garden_operations(op)
        except (ValueError, ZeroDivisionError, FileNotFoundError,
                TypeError) as e:
            print(f"Caught {e.__class__.__name__}: {e}")
        else:
            print("Operation completed successfully")
        op += 1


if __name__ == "__main__":
    test_error_types()
    print("\nAll error types tested successfully!")
