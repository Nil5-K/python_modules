import random


def main() -> None:
    print("=== Game Data Alchemist ===\n")

    players = ['Alice', 'bob', 'Charlie',
               'dylan', 'Emma', 'Gregory', 'john', 'kevin', 'Liam']
    print(f"Initial list of players: {players}")

    players_cap = [player.capitalize() for player in players]
    print(f"New list with all names capitalized: {players_cap}")

    players_only_cap = [player for player
                        in players if player == player.capitalize()]
    print(f"New list of capitalized names only: {players_only_cap}")

    scores = {player: random.randint(100, 1000) for player in players_cap}
    print(f"Score dict: {scores}")
    score_average = round(sum(scores.values()) / len(scores.values()), 2)
    print(f"Score average is {score_average}")
    scores_above_average = {player: score for player, score
                            in scores.items() if score > score_average}
    print(f"High scores: {scores_above_average}")


if __name__ == "__main__":
    main()
