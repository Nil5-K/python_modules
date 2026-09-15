from ex1 import HealingCreatureFactory, TransformCreatureFactory


def main() -> None:
    healing = HealingCreatureFactory()
    transform = TransformCreatureFactory()

    print("Testing Creature with healing capability")
    print(" base:")
    base = healing.create_base()
    print(base.describe())
    print(base.attack())
    print(base.heal())
    print(" evolved:")
    evolved = healing.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())
    print()

    print("Testing Creature with transform capability")
    print(" base:")
    base_two = transform.create_base()
    print(base_two.describe())
    print(base_two.attack())
    print(base_two.transform())
    print(base_two.attack())
    print(base_two.revert())
    print(" evolved:")
    evolved_two = transform.create_evolved()
    print(evolved_two.describe())
    print(evolved_two.attack())
    print(evolved_two.transform())
    print(evolved_two.attack())
    print(evolved_two.revert())


if __name__ == "__main__":
    main()
