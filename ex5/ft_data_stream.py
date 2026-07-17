import random
import typing


def gen_event() -> typing.Generator[tuple[str, str]]:
    players = ["Bob", "Martin", "Alice", "Kendrick", "Dylan", "Charlie"]
    actions = ["run", "sleep", "eat", "fight", "speak", "walk", "cook"]
    res: tuple[str, str]

    while True:
        random_player = random.choice(players)
        random_action = random.choice(actions)

        res = (random_player, random_action)
        yield res


def consume_event(
        event_list: list[tuple[str, str]]
        ) -> typing.Generator[tuple[str, str]]:
    while event_list:
        random_event = random.choice(event_list)
        event_list.remove(random_event)
        yield random_event


def main() -> None:
    print("=== Game Data Stream Processor ===")

    events = gen_event()
    for i in range(0, 1000):
        player, action = next(events)
        print(f"Event {i}: Player {player} did action {action}")

    ten_events = [next(events) for _ in range(10)]
    print(f"Built list of 10 events: {ten_events}")

    for event in consume_event(ten_events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {ten_events}")


if __name__ == "__main__":
    main()
