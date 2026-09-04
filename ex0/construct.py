import sys
import os
import site


def in_env() -> bool:
    return sys.prefix != sys.base_prefix


def get_site_path() -> str:
    return str(site.getsitepackages()[0])


def get_env_path() -> str:
    return str(sys.prefix)


def get_env_name() -> str:
    return str(os.path.basename(sys.prefix))


def get_current_python() -> str:
    return str(sys.executable)


def print_no_env_infos() -> None:
    print(f"Current Python: {get_current_python()}")
    print("Virtual Environment: None detected")
    print()
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print()
    print("To enter the construct, run: ")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\\Scripts\\activate # On Windows")
    print()
    print("Then run this program again.")


def print_env_infos() -> None:
    print(f"Current Python: {get_current_python()}")
    print(f"Virtual Environment: {get_env_name()}")
    print(f"Environment Path: {get_env_path()}")
    print()
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting "
          "the global system.")
    print()
    print("Package installation path:")
    print(get_site_path())


def main() -> None:
    is_env = in_env()
    print("MATRIX STATUS: ", end="", flush=True)
    if is_env:
        print("Welcome to the construct\n")
        print_env_infos()
    else:
        print("You're still plugged in\n")
        print_no_env_infos()


if __name__ == "__main__":
    main()
