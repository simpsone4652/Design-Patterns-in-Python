class car():
    def __init__(self,brand, model,technical,power,consumption,fuel,transsmision,category,price):
        self.brand = brand
        self.technical = technical
        self.power = power
        self.consumption = consumption
        self.fuel = fuel
        self.transsmision = transsmision
        self.category = category
        self.price = price
        
     # tutaj wymuszamy implementację tej metody w klasach pochodnych
    def nazwa_caru(self): 
        pass
    def model_auta(self):
        print(f" {self.modelyear}, {self.brand},{self.model },{self.power} ")
        
    def numer(self):
        self.ID += 1
class Audi(car):
    def nazwa_gatunku(self):
        return 1 + "txt"
    
        
    def __init__(self,brand, model,year,power,consumption,fuel,transsmision,category,price):
        super().__init__(fuel,consumption,power,transsmision)
        self.fuel = fuel
        
    def check(self):
        super().check()
        
def main():
    Audi = 1("R8", 620,2019,620,16,"petrol","automatic","sport","950k")
    Porsche = 2("911 Tyrbi S",2020,650,14,"petrol","automatic","sport","950k")
    BMW = 3("M8",2019,600,16,"gas","automatic","luxury","950k")
    Lamborghini = 4("Urus",2017,650,14,"petrol","automatic","SUV","110kk")
    Bugatti = 5("Veyron",2005,1001,35,"petrol","automatic","sport","950k")
    Ferrari = 6("458 Italia",2009,570,27,"petrol","automatic","sport","125kk")
    Audi2 =7("SQ7",2016,435,9,"diesel","automatic","SUV","350k")
    Mercedes = 8("365 AMG",2016,630,5,"petrol","automatic","cabrio","950k")
    Tesla = 9("S",2017,422,0,"electric","automatic","coupe","400k")
    
    Audi.check()
 
if __name__ == "__main__":
    main()