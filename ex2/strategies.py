from abc import ABC, abstractmethod
from ex0.creatures import Creature
from ex1.capabilities import TransformCapability, HealCapability

class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> str:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> str:
        return creature.attack()


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise ValueError(
                f"Invalid Creature '{creature.name}' for this aggressive strategy"
            )
        assert isinstance(creature, TransformCapability)
        result = creature.transform() + "\n"
        result += creature.attack() + "\n"
        result += creature.revert()
        return result


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise ValueError(
                f"Invalid Creature '{creature.name}' for this defensive strategy"
            )
        assert isinstance(creature, HealCapability)
        result = creature.attack() + "\n"
        result += creature.heal()
        return result