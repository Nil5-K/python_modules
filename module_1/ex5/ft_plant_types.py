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


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int,
                 color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.blooms = False

    def bloom(self) -> None:
        self.blooms = True

    def show(self) -> str:
        if self.blooms:
            bloom_str = f"{self.name} is blooming beautifully!"
        else:
            bloom_str = f"{self.name} has not bloomed yet"
        return f"{super().show()}\n Color: {self.color}\n {bloom_str}"


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of "
              f"{self._height}cm long and {self.trunk_diameter}cm wide.")

    def show(self) -> str:
        return f"{super().show()}\n Trunk diameter: {self.trunk_diameter}cm"


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value: int = 0

    def age(self, n: int) -> None:
        super().age(n)
        self.nutritional_value += n

    def show(self) -> str:
        return (f"{super().show()}\n"
                f" Harvest season: {self.harvest_season}\n"
                f" Nutritional value: {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    print(rose.show())
    print("[asking the rose to bloom]")
    rose.bloom()
    print(rose.show())

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    print(oak.show())
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("\n=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    print(tomato.show())
    print("[make tomato grow and age for 20 days]")
    tomato.grow(42.0)
    tomato.age(20)
    print(tomato.show())
