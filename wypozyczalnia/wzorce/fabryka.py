from abc import ABCMeta, abstractmethod
class Samochod(metaclass=ABCMeta):
    "Abstrakcyjne stworzenie klasy"
    @staticmethod
    @abstractmethod
    def create_object():
        "Abstrakcyjna metoda interfejsu"


        
class Sportowy(Samochod):
    "Klasa abstrakcyjna dziedzicząca"
    def __init__(self):
        self.name = "Sportowy"
    def create_object(self):
        return self

class Terenowy(Samochod):
    def __init__(self):
        self.name = "Terenowy"
    def create_object(self):
        return self

class Kabriolet(Samochod):
    def __init__(self):
        self.name = "Kabriolet"
    def create_object(self):
        return self


class Kreator:
    "Klasa wybierająca konkretny rodzaj pojazdu"
    @staticmethod
    def create_object(some_property):
        "Metoda statyczna uzyskująca konkretny pojazd"
        if some_property == 'a':
            return Sportowy()
        if some_property == 'b':
            return Terenowy()
        if some_property == 'c':
            return Kabriolet()
        return None



PRODUCT = Kreator().create_object('b')
print(PRODUCT.name)