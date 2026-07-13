class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.growth: float = 0.0

    def show(self) -> str:
        return (f"{self.name}: {round(self.height, 1)}cm,"
                f" {self.age} days old")

    def grow(self, n: float) -> None:
        self.height = self.height + n
        self.growth = self.growth + n

    def age_up(self, n: int) -> None:
        self.age = self.age + n


if __name__ == "__main__":
    print("=== Plant Factory Output ===")

    rose = Plant("Rose", 25.0, 30)
    oak = Plant("Oak", 200.0, 365)
    cactus = Plant("Cactus", 5.0, 90)
    sunflower = Plant("Sunflower", 80.0, 45)
    fern = Plant("Fern", 15.0, 120)

    print(f"Created: {rose.show()}")
    print(f"Created: {oak.show()}")
    print(f"Created: {cactus.show()}")
    print(f"Created: {sunflower.show()}")
    print(f"Created: {fern.show()}")
