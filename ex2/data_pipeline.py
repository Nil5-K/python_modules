from abc import ABC, abstractmethod
from typing import Any, Protocol


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


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        fields: list[str] = []
        for _, value in data:
            if "," in value or '"' in value:
                value = '"' + value.replace('"', '""') + '"'
            fields.append(value)
        print("CSV Output:")
        print(",".join(fields))


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        entries: list[str] = []
        for rank, value in data:
            escaped = value.replace("\\", "\\\\").replace('"', '\\"')
            entries.append(f'"item_{rank}": "{escaped}"')
        print("JSON Output:")
        print("{" + ", ".join(entries) + "}")


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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._processors:
            _, remaining = proc.stats()
            data: list[tuple[int, str]] = []
            for _ in range(min(nb, remaining)):
                data.append(proc.output())
            plugin.process_output(data)

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
    print("=== Code Nexus - Data Pipeline ===")
    print("Initialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()

    print("Registering Processors")
    stream.register_processor(NumericProcessor())
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())

    first_batch: list[Any] = [
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
    print(f"Send first batch of data on stream: {first_batch}")
    stream.process_stream(first_batch)
    stream.print_processors_stats()

    print("Send 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, CSVExportPlugin())
    stream.print_processors_stats()

    second_batch: list[Any] = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {
                "log_level": "ERROR",
                "log_message": "500 server crash",
            },
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days",
            },
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]
    print(f"Send another batch of data: {second_batch}")
    stream.process_stream(second_batch)
    stream.print_processors_stats()

    print("Send 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, JSONExportPlugin())
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
