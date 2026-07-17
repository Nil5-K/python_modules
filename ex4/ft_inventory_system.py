import sys


def verify_input(inventory: dict[str, str]) -> dict[str, int]:
    verified: dict[str, int] = {}
    for key in inventory.keys():
        value = inventory[key]
        try:
            verified[key] = int(value)
        except ValueError as e:
            print(f"Quantity error for '{key}': {e}")
    return verified


def parse_input() -> dict[str, int]:
    inventory: dict[str, str] = {}

    for arg in sys.argv[1:]:
        split_arg = arg.split(":")
        if (len(split_arg) != 2):
            print(f"Invalid Parameter: '{arg}'")
            continue
        key, value = split_arg
        if key in inventory:
            print(f"Redundant item '{key}' - discarding")
            continue
        inventory[key] = value

    verified_inventory = verify_input(inventory)
    return verified_inventory


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory = parse_input()
    inventory_values = inventory.values()
    inventory_keys = inventory.keys()
    total = sum(inventory_values)

    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory_keys)}")
    print(f"Total quantity of the {len(inventory)} items: {total}")

    for key in inventory_keys:
        value = inventory[key]
        print(f"Item {key} represents {round(value / total * 100, 1)}%")

    most_key, most_value = None, None
    least_key, least_value = None, None
    for key in inventory.keys():
        value = inventory[key]

        if most_value is None or value > most_value:
            most_key = key
            most_value = value

        if least_value is None or value < least_value:
            least_key = key
            least_value = value

    print(f"Item most abundant: {most_key} with quantity {most_value}")
    print(f"Item least abundant: {least_key} with quantity {least_value}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
