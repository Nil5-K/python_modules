from ex0.creatures import Creature
from .capabilities import HealCapability, TransformCapability


class Sproutling(HealCapability, Creature):
    name = "Sproutling"
    creature_type = "Grass"

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"

    def heal(self) -> str:
        return f"{self.name} heals itself for a small amount"


class Bloomelle(HealCapability, Creature):
    name = "Bloomelle"
    creature_type = "Grass/Fairy"

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def heal(self) -> str:
        return f"{self.name} heals itself and others for a large amount"


class Shiftling(TransformCapability, Creature):
    name = "Shiftling"
    creature_type = "Normal"
    state: bool = False

    def attack(self) -> str:
        if self.state:
            return f"{self.name} performs a boosted strike!"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        self.state = True
        return f"{self.name} shifts into a sharper form!"


    def revert(self) -> str:
        self.state = False
        return f"{self.name} returns to normal."


class Morphagon(TransformCapability, Creature):
    name = "Morphagon"
    creature_type = "Normal/Dragon"
    state: bool = False

    def attack(self) -> str:
        if self.state:
            return f"{self.name} unleashes a devastating morph strike!"         
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        self.state = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self.state = False
        return f"{self.name} stabilizes its form."
