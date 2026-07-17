import random


def get_all_achievements() -> list[str]:
    return [
        'Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner',
        'Survivor', 'Master Explorer', 'Treasure Hunter', 'Unstoppable',
        'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind',
        'Boss Slayer', 'God Like', 'Cave Diver', 'Golden Gooner',
        'Fent Fighter', 'Secret Saucer', 'Minor Miner', 'Track Cracker',
        'Street Sigger', 'Dough Baker',
    ]


def gen_player_achievements() -> set[str]:
    MASTER_LIST: list[str] = get_all_achievements()
    rand_nb: int = random.randint(4, 9)
    return set(random.sample(MASTER_LIST, rand_nb))


def main() -> None:
    print("=== Achievement Tracker System ===")

    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    all_player_achievements = alice.union(bob, charlie, dylan)
    common = alice.intersection(bob, charlie, dylan)
    print(f"\nAll distinct achievements: {all_player_achievements}")
    print(f"\nCommon achievements: {common}")

    only_alice = alice - bob.union(charlie, dylan)
    only_bob = bob - alice.union(charlie, dylan)
    only_charlie = charlie - bob.union(alice, dylan)
    only_dylan = dylan - bob.union(charlie, alice)

    print(f"\nOnly Alice: {only_alice}")
    print(f"Only Bob: {only_bob}")
    print(f"Only Charlie: {only_charlie}")
    print(f"Only Dylan: {only_dylan}")

    missing_alice = all_player_achievements - alice
    missing_bob = all_player_achievements - bob
    missing_charlie = all_player_achievements - charlie
    missing_dylan = all_player_achievements - dylan

    print(f"\nAlice is missing: {missing_alice}")
    print(f"Bob is missing: {missing_bob}")
    print(f"Charlie is missing: {missing_charlie}")
    print(f"Dylan is missing: {missing_dylan}")


if __name__ == "__main__":
    main()
