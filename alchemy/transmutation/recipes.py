import alchemy
from ..potions import strength_potion
from elements import create_fire


def lead_to_gold() -> str:
    return (
        "Recipe transmuting Lead to Gold: brew "
        f"'{alchemy.elements.create_air()}' and '{strength_potion()}' "
        f"mixed with '{create_fire()}'"
    )
