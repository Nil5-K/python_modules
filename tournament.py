from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
)



Opponent = tuple[CreatureFactory, BattleStrategy]


def battle(opponents: list[Opponent]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    print()

    fighters = [
        (factory.create_base(), strategy) for factory, strategy in opponents
    ]

    for i in range(len(fighters)):
        for j in range(i + 1, len(fighters)):
            creature_one, strategy_one = fighters[i]
            creature_two, strategy_two = fighters[j]

            print("* Battle *")
            print(creature_one.describe())
            print(" vs.")
            print(creature_two.describe())
            print(" now fight!")

            try:
                print(strategy_one.act(creature_one))
                print(strategy_two.act(creature_two))
            except ValueError as error:
                print(f"Battle error, aborting tournament: {error}")
                return

            print()


def main() -> None:
    flame = FlameFactory()
    aqua = AquaFactory()
    healing = HealingCreatureFactory()
    transform = TransformCreatureFactory()

    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    battle([(flame, normal), (healing, defensive)])
    print()

    print("Tournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([(flame, aggressive), (healing, defensive)])
    print()

    print("Tournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle([(aqua, normal), (healing, defensive), (transform, aggressive)])


if __name__ == "__main__":
    main()