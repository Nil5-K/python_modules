class Plant:
    class _Statistics:
        def __init__(self) -> None:
            self._grow_calls: int = 0
            self._age_calls: int = 0
            self._show_calls: int = 0

        def record_grow(self) -> None:
            self._grow_calls += 1

        def record_age(self) -> None:
            self._age_calls += 1

        def record_show(self) -> None:
            self._show_calls += 1

        def display(self) -> None:
            print(f"Stats: {self._grow_calls} grow,"
                  f" {self._age_calls} age,"
                  f" {self._show_calls} show")

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._growth: float = 0.0
        self._stats = self._Statistics()
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

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def show(self) -> str:
        self._stats.record_show()
        return (f"{self.name}: {round(self._height, 1)}cm,"
                f" {self._age} days old")

    def show_stats(self) -> None:
        self._stats.display()

    def grow(self, n: float) -> None:
        self._stats.record_grow()
        self._height = self._height + n
        self._growth = self._growth + n

    def age_up(self, n: int) -> None:
        self._stats.record_age()
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
    class _TreeStatistics(Plant._Statistics):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls: int = 0

        def record_shade(self) -> None:
            self._shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f"{self._shade_calls} shade")

    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self._tree_stats = self._TreeStatistics()
        self._stats = self._tree_stats

    def produce_shade(self) -> None:
        self._tree_stats.record_shade()
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

    def age_up(self, n: int) -> None:
        super().age_up(n)
        self.nutritional_value += n

    def show(self) -> str:
        return (f"{super().show()}\n"
                f" Harvest season: {self.harvest_season}\n"
                f" Nutritional value: {self.nutritional_value}")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int,
                 color: str) -> None:
        super().__init__(name, height, age, color)
        self.seeds: int = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42

    def show(self) -> str:
        return f"{super().show()}\nSeeds: {self.seeds}"


def display_statistics(plant: Plant) -> None:
    plant.show_stats()


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")

    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    print(rose.show())
    print(f"[statistics for {rose.name}]")
    display_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    print(rose.show())
    print(f"[statistics for {rose.name}]")
    display_statistics(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    print(oak.show())
    print(f"[statistics for {oak.name}]")
    display_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print(f"[statistics for {oak.name}]")
    display_statistics(oak)

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    print(sunflower.show())
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age_up(20)
    sunflower.bloom()
    print(sunflower.show())
    print(f"[statistics for {sunflower.name}]")
    display_statistics(sunflower)

    print("\n=== Anonymous")
    unknown = Plant.anonymous()
    print(unknown.show())
    print(f"[statistics for {unknown.name}]")
    display_statistics(unknown)
