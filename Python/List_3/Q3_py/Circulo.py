from Geometria import Geometria
import math as math

class Circulo(Geometria):
    
    def __init__(self, raio) -> None:
        super().__init__()

        self.raio : float = raio
        self.pi = 3.1415

    
    def area(self) -> float:
        return (pow(self.raio, 2)) * self.pi

    def comprimento(self) -> float:
        return 2 * self.pi * self.raio

    def __str__(self):
        return f"{self.raio}"