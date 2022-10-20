from abc import ABC, abstractmethod

class Geometria(ABC):

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def comprimento(self) -> float:
        pass