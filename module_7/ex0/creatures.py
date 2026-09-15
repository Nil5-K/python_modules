from abc import ABC, abstractmethod


class Creature(ABC):
    name: str
    creature_type: str

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.creature_type} type Creature"


class Flameling(Creature):
    name = "Flameling"
    creature_type = "Fire"

    def attack(self) -> str:
        return f"{self.name} uses Ember!"


class Pyrodon(Creature):
    name = "Pyrodon"
    creature_type = "Fire/Flying"

    def attack(self) -> str:
        return f"{self.name} uses Flamethrower!"


class Aquabub(Creature):
    name = "Aquabub"
    creature_type = "Water"

    def attack(self) -> str:
        return f"{self.name} uses Water Gun!"


class Torragon(Creature):
    name = "Torragon"
    creature_type = "Water"

    def attack(self) -> str:
        return f"{self.name} uses Hydro Pump!"
