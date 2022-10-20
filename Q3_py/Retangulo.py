from Geometria import Geometria

class Retangulo(Geometria):

    def __init__(self, largura, comp) -> None:
        super().__init__()

        self.largura = largura
        self.comp = comp


    def area(self) -> float:
        return self.largura * self.comp

    def comprimento(self) -> float:
        return self.comp

    def __str__(self):
        return f"{self.largura}, {self.comp}"