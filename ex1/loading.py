import importlib.metadata as metadata
import sys


required_packages: dict[str, str] = {
        "pandas": "Data manipulation ready",
        "numpy": "Numirical computation ready",
        "requests": "Network access ready",
        "matplotlib": "Visualization ready"
}


def load_packages(_packages: dict[str, str]) -> None:
    missing_packages: list[str] = []
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    for pkg, msg in _packages.items():
        try:
            metadata.import_module(pkg)
            version = metadata.version(pkg)
            print(f"[OK] {pkg} ({version}) - {msg}")
        except (ImportError, metadata.PackageNotFoundError):
            missing_packages.append(pkg)
    if missing_packages:
        for mis in missing_packages:
            print(f"[ERROR] Missing dependency detected: {mis}")
        print("\n--- Installation Instructions ---")
        print("Using pip:")
        print("$> pip install -r requirements.txt")
        print("$> python3 loading.py")
        print("\nUsing Poetry:")
        print("$> poetry install")
        print("$> poetry run python loading.py")
        sys.exit(1)


if __name__ == "__main__":
    load_packages(required_packages)
