class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def check_wilting(is_wilting: bool) -> None:
    if is_wilting:
        raise PlantError("The tomato plant is wilting!")


def check_water_level(water_level: int) -> None:
    if water_level < 10:
        raise WaterError("Not enough water in the tank!")


def test_exceptions() -> None:
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        check_wilting(True)
    except PlantError as e:
        print(f"Caught {e.__class__.__name__}: {e}")

    print("\nTesting WaterError...")
    try:
        check_water_level(9)
    except WaterError as e:
        print(f"Caught {e.__class__.__name__}: {e}")

    print("\nTesting catching all garden errors...")
    try:
        check_wilting(True)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        check_water_level(5)
    except GardenError as e:
        print(f"Caught GardenError: {e}")


if __name__ == "__main__":
    test_exceptions()
    print("\nAll custom error types work correctly!")
