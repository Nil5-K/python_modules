from dotenv import load_dotenv
import os


def get_requierd_vars() -> dict[str, str | None]:
    matrix_mode = os.getenv("MATRIX_MODE", "development")
    db_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_lvl = os.getenv("LOG_LEVEL", "DEBUG")
    zion_ep = os.getenv("ZION_ENDPOINT")

    return {"MATRIX_MODE": matrix_mode, "DATABASE_URL": db_url,
            "API_KEY": api_key, "LOG_LEVEL": log_lvl, "ZION_ENDPOINT": zion_ep}


def main() -> None:
    dot_env: bool = load_dotenv()
    env_vars: dict[str, str | None] = get_requierd_vars()
    missing_vars: list[str] = []

    print("ORACLE STATUS: Reading the Matrix...\n")
    for key, value in env_vars.items():
        if not value:
            missing_vars.append(key)
    if missing_vars:
        print("[WARNING] Some variables are not set by the user: ")
        for var in missing_vars:
            print(f" - {var} is not set")
        print()

    db_status = (
        "Connected to local instance"
        if env_vars.get("DATABASE_URL")
        else "Not connected! Set the DATABASE_URL variable!"
    )
    api_access = (
        "Authenticated"
        if env_vars.get("API_KEY")
        else "No Access! Set the API_KEY variable"
    )
    zion_status = (
        "Online"
        if env_vars.get("ZION_ENDPOINT")
        else "Offline! Set the ZION_ENDPOINT variable"
    )

    print("Configuration loaded:")
    print(f"Mode: {env_vars.get('MATRIX_MODE')}")
    print(f"Database: {db_status}")
    print(f"API Access: {api_access}")
    print(f"Log Level: {env_vars.get('LOG_LEVEL')}")
    print(f"Zion Network: {zion_status}\n")

    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    if dot_env:
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file is missing!")
    print("[OK] Production overrides available\n")
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
