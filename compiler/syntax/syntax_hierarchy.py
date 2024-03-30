from enum import Enum, auto


class Hierarchy(Enum):
    ADDITION = auto()
    MULTIPLICATION = auto()
    BRACKETS = auto()
    NUMBER = auto()

    def __lt__(self, other):
        if self.__class__ != other.__class__:
            raise TypeError(f"< not supported for class {other.__class__}")
        
        return self.value < other.value
