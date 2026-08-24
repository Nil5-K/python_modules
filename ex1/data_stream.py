from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    name: str

    def __init__(self) -> None:
        self._store: list[tuple[int, str]] = []
        self._ingest_rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        return self._store.pop(0)

    def stats(self) -> tuple[int, int]:
        return (self._ingest_rank, len(self._store))


class NumericProcessor(DataProcessor):
    name = "Numeric Processor"

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, (int | float)):
                    return False
            return True
        return isinstance(data, (int | float))

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            items = data
        else:
            items = [data]
        for item in items:
            self._store.append((self._ingest_rank, str(item)))
            self._ingest_rank += 1


class TextProcessor(DataProcessor):
    name = "Text Processor"

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, str):
                    return False
            return True
        return isinstance(data, str)

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            items = data
        else:
            items = [data]
        for item in items:
            self._store.append((self._ingest_rank, item))
            self._ingest_rank += 1


class LogProcessor(DataProcessor):
    name = "Log Processor"

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            items = data
        else:
            items = [data]
        for item in items:
            if not isinstance(item, dict):
                return False
            for key, value in item.items():
                if not isinstance(key, str) or not isinstance(value, str):
                    return False
        return True

    def ingest(
        self, data: dict[str, str] | list[dict[str, str]]
    ) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, list):
            items = data
        else:
            items = [data]
        for item in items:
            self._store.append((self._ingest_rank, ": ".join(item.values())))
            self._ingest_rank += 1


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            processed = False
            for proc in self._processors:
                if proc.validate(element):
                    proc.ingest(element)
                    processed = True
                    break
            if not processed:
                print(
                    "DataStream error - Can't process element "
                    f"in stream: {element}"
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for proc in self._processors:
            total, remaining = proc.stats()
            print(
                f"{proc.name}: total {total} items processed, "
                f"remaining {remaining} on processor"
            )


def main() -> None:
    print("=== Code Nexus - Data Stream ===")
    print("Initialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()

    print("Registering Numeric Processor")
    numeric = NumericProcessor()
    stream.register_processor(numeric)

    batch: list[Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected",
            },
        ],
        42,
        ["Hi", "five"],
    ]
    print(f"Send first batch of data on stream: {batch}")
    stream.process_stream(batch)
    stream.print_processors_stats()

    print("Registering other data processors")
    text = TextProcessor()
    log = LogProcessor()
    stream.register_processor(text)
    stream.register_processor(log)

    print("Send the same batch again")
    stream.process_stream(batch)
    stream.print_processors_stats()

    print(
        "Consume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )
    for _ in range(3):
        numeric.output()
    for _ in range(2):
        text.output()
    for _ in range(1):
        log.output()
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
