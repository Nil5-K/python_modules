from abc import ABC, abstractmethod


class HealCapability(ABC):
    state: bool

    @abstractmethod
    def heal(self) -> str:
        pass


class TransformCapability(ABC):
    state: bool

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass
