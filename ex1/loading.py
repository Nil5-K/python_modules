import importlib.metadata as metadata
import importlib
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
            importlib.import_module(pkg)
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

def fake_data() -> None:
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data...")

    n_points = 1000
    print(f"Processing {n_points} data points...")

    rng = np.random.default_rng(42)
    timestamps = np.arange(n_points)
    values = rng.normal(loc=50, scale=15, size=n_points)

    df = pd.DataFrame({"timestamp": timestamps, "value": values})

    print("\nGenerating visualization...")

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df["timestamp"], df["value"], color="green", linewidth=0.8)
    ax.set_title("Matrix Analysis")
    ax.set_xlabel("Timestamp")
    ax.set_ylabel("Value")

    output_file = "matrix_analysis.png"
    fig.savefig(output_file)
    plt.close(fig)

    print("\nAnalysis complete!")
    print(f"Results saved to: {output_file}")


if __name__ == "__main__":
    load_packages(required_packages)
    fake_data()
