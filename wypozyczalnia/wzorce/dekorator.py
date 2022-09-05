

class AbstractCar(object):
    def __init__(self):
        self.name  = ""
        self.price = 0.00
        pass

    def GetName(self):
        return self.name
    
    def GetPrice(self):
        return self.price
            


class AbstractDecorator(AbstractCar):
    def __init__(self):
        pass


class Decorator(AbstractDecorator):
    def __init__(self, parent):
        self.car         = parent
        self.accessories = ""
        self.surcharge   = 0.00
    
    def GetName(self):
        return self.car.GetName() + " + " + self.accessories

    def GetPrice(self):
        return self.car.GetPrice() + self.surcharge

#-------------------------------------------------------------------------------

class Car(AbstractCar):
    def __init__(self):
        pass


class ConsoleApplication(object):

    def Run(self):

        #bez dekoracji

        car = Car()
        car.name  = "Audi 80"
        car.price = 20000.00


        print("Samochod bez dodatkow")
        print ("")
        print ("    Nazwa: %s"    % (car.GetName()))
        print ("    Cena:  %1.2f" % (car.GetPrice()))
        print ("")

        

        #dekoracja auta
        car = Decorator(car)
        car.accessories = "klimatyzacja"
        car.surcharge   = 5000.00

        print ("Samochod z klimatyzacja")
        print ("")
        print ("    Nazwa: %s"    % (car.GetName()))
        print ("    Cena:  %1.2f" % (car.GetPrice()))
        print ("")

        #kolejna dekoracja do auta
        car = Decorator(car)
        car.accessories = "alufelgi"
        car.surcharge   = 100.00

        print ("Samochod z klimatyzacja i alufelgami")
        print ("")
        print ("    Nazwa: %s"    % (car.GetName()))
        print ("    Cena:  %1.2f" % (car.GetPrice()))
        print ("")

#-------------------------------------------------------------------------------

def main():
    Application = ConsoleApplication()
    Application.Run()

#-------------------------------------------------------------------------------

if __name__ == "__main__":
    main()