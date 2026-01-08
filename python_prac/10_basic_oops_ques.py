#Question 1: Create a Car class with attributes like brand and model. Then create an instance of this class.
'''
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

my_Car=Car("Tata","Safari")
print(my_Car.brand)
print(my_Car.model)
'''

#Question 2: Add a method to the Car class that displays the full name of the car(brand and model).
'''
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def full_name(self):
        return f"{self.brand} {self.model}"

my_Car=Car("Tata","Safari")
print(my_Car.full_name())
'''

#Question 3:Create an ElectricCar Class that inherits from the Car class and has an additional attribute battery_size.(Inheritance)
'''
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size
    
tesla_car=ElectricCar("Tesla","Model S","85kWh")
print(tesla_car.battery_size)
print(tesla_car.full_name())
'''

#Question 4: Modify the Car class to encapsulation the brand attribute, making it privat, and provide a geeter method for it.(Encapsulation)

#Making the attribute private or make it accessible inside class only and create a getter to access outside the class 
'''
class Car:
    def __init__(self,brand,model):
        self.__brand=brand
        self.model=model

    def get_brand(self):
        return self.__brand
    
my_Car=Car("Tata","Safari")
print(my_Car.get_brand())  
'''
