class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._growth: float = 0.0
        if height < 0:
            print(f"{name}: Error, height can't be negative")
            self._height: float = 0.0
        else:
            self._height = height
        if age < 0:
            print(f"{name}: Error, age can't be negative")
            self._age: int = 0
        else:
            self._age = age

    def show(self) -> str:
        return (f"{self.name}: {round(self._height, 1)}cm,"
                f" {self._age} days old")

    def grow(self, n: float) -> None:
        self._height = self._height + n
        self._growth = self._growth + n

    def age(self, n: int) -> None:
        self._age = self._age + n

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = new_height

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age = new_age

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age


if __name__ == "__main__":
    print("=== Garden Security System ===")

    rose = Plant("Rose", 15.0, 10)
    print(f"Plant created: {rose.show()}\n")

    rose.set_height(25.0)
    rose.set_age(30)
    print(f"Height updated: {round(rose.get_height())}cm")
    print(f"Age updated: {rose.get_age()} days\n")

    rose.set_height(-12.0)
    rose.set_age(-42)

    print(f"\nCurrent state: {rose.show()}")
