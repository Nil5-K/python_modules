class Plant:
    name: str = ""
    height: float = 0.0
    _age: int = 0
    growth: float = 0.0

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm,"
              f" {self._age} days old")

    def grow(self, n: float) -> None:
        self.height = self.height + n
        self.growth = self.growth + n

    def age(self, n: int) -> None:
        self._age = self._age + n


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")

    rose = Plant()
    rose.name = "Rose"
    rose.height = 25.0
    rose._age = 30

    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.show()
        rose.grow(0.8)
        rose.age(1)

    print(f"Growth this week: {round(rose.growth)}cm")
