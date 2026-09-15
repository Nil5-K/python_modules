from ex0 import CreatureFactory, FlameFactory, AquaFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")

    base = factory.create_base()
    print(base.describe())
    print(base.attack())

    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print()


def battle(fac_one: CreatureFactory, fac_two: CreatureFactory) -> None:
    print("Testing battle")

    cre_one = fac_one.create_base()
    print(cre_one.describe())
    print(" vs.")
    cre_two = fac_two.create_base()
    print(cre_two.describe())
    print(" fight!")
    print(cre_one.attack())
    print(cre_two.attack())
    print()


def main() -> None:
    flaming = FlameFactory()
    aqua = AquaFactory()

    test_factory(flaming)
    test_factory(aqua)

    battle(flaming, aqua)


if __name__ == "__main__":
    main()
