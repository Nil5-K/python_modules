import sys


def get_scores() -> list[int]:
    scores: list[int] = []
    i: int = 0

    for arg in sys.argv[1:]:
        try:
            scores.append(int(arg))
            i += 1
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    return scores


def print_scores(scores: list[int]) -> None:
    average: float = sum(scores) / len(scores)
    range: float = max(scores) - min(scores)

    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {average}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {range}")


def main() -> None:
    print("=== Player Score Analytics ===")

    scores: list[int] = get_scores()
    if len(scores) <= 0:
        print("No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...")
        return

    print_scores(scores)


if __name__ == "__main__":
    main()
