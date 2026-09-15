import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        try:
            raw = input(
                "Enter new coordinates as floats in format 'x,y,z': "
            )
            x, y, z = raw.split(",")
        except (ValueError, TypeError):
            print("Invalid syntax")
            continue

        try:
            coords = (
                round(float(x), 1),
                round(float(y), 1),
                round(float(z), 1),
            )
        except (ValueError, TypeError) as e:
            bad_param = str(e).split("'")[-2]
            print(f"Error on parameter '{bad_param}': {e}")
            continue

        return coords


def get_center(coords: tuple[float, float, float]) -> float:
    return math.sqrt(coords[0] ** 2 + coords[1] ** 2 + coords[2] ** 2)


def get_distance(
    coords_x: tuple[float, float, float],
    coords_y: tuple[float, float, float],
) -> float:
    return math.sqrt(
        (coords_y[0] - coords_x[0]) ** 2
        + (coords_y[1] - coords_x[1]) ** 2
        + (coords_y[2] - coords_x[2]) ** 2
    )


def main() -> None:
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    coords_one = get_player_pos()
    print(f"Got a first tuple: {coords_one}")
    print(
        f"It includes: X={coords_one[0]}, "
        f"Y={coords_one[1]}, Z={coords_one[2]}"
    )
    print(f"Distance to center: {round(get_center(coords_one), 4)}")

    print("Get a second set of coordinates")
    coords_two = get_player_pos()
    distance = round(get_distance(coords_one, coords_two), 4)
    print(f"Distance between the 2 sets of coordinates: {distance}")


if __name__ == "__main__":
    main()
