from email.policy import default
from Circulo import Circulo
from Retangulo import Retangulo

if __name__ == "__main__":
    circles: list = []
    retangules: list = []

    hasInput = True
    while hasInput:
        choice : int = int(input("Select some choice: \n0 - Exit\n1 - Create circle\n2 - Create Retangule\n"))

        match choice:
            case 0:
                hasInput = False
            case 1:
                radius : float = float(input("Radius of circle:\n"))
                circles.append(Circulo(radius))
            case 2: 
                width : float = float(input("Width of retangule\n"))
                length : float = float(input("Length of retangule\n"))
                retangules.append(Retangulo(width, length))
            case default:
                pass

    for index, form in enumerate(circles):
        print(f"N: {index}, Attr: {form}, Area: {form.area()}, Comp: {form.comprimento()}")

    for index, form in enumerate(retangules):
        print(f"N: {index}, Attr: {form}, Area: {form.area()}, Comp: {form.comprimento()}")