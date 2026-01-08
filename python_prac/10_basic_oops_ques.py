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

#Question 3:Create an ElectricCar Class that inherits from the Car class and has an additional attribute battery_size.(Inheritance).
'''
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size
    
tesla_car=ElectricCar("Tesla","Model S","85kWh")
print(tesla_car.battery_size)
print(tesla_car.full_name())
'''

#Question 4: Modify the Car class to encapsulation the brand attribute, making it privat, and provide a geeter method for it.(Encapsulation).

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
#Question 5: Demonstrate polymorphism  by defining a method fuel_type in both Car and ElectricCar classes, but with different behaivors.

# Here we can see that same name method used for different Car and give different result
'''
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def fuel_type(self):
        return "Petrol or Disel"

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size
        
    def fuel_type(self):
        return "Electric charge"
    
my_car=Car("Tata","Safari")
print(my_car.fuel_type())
tesla_car=ElectricCar("Tesla","Model S","85kWh")
print(tesla_car.fuel_type())
'''
#Question 6: Add a class variable to Car that keeps track of the number of cars created.
'''
class Car:
    total_car=0
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        Car.total_car+=1

my_car=Car("Tata","Safari")
my_car1=Car("Tata","Punch")
my_car2=Car("Tata","Nexon")
print(Car.total_car)
'''

#Question 7: Add a static method to the Car class that returns a general description of a car.
'''
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    @staticmethod
    def general_description():
        return "it is a mode of transportation"

my_car=Car("Tata","Safari")
print(Car.general_description())
'''

#Question 8: Use a property decorator in the Car class to make the model attribute read-only.
'''
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.__model=model

    @property
    def model(self):
        return self.__model

my_car=Car("Tata","Safari")

print(my_car.model)
'''

#Question 9: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.
'''
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    
class ElectricCar(Car):
    def __init__(self,brand,model):
        super().__init__(brand,model)
        
class ElectricCa():
    def __init__(self,brand,model):
        pass

my_tesla=ElectricCar("Tesla","Model S")

print(isinstance(my_tesla,Car))
print(isinstance(my_tesla,ElectricCar))
print(isinstance(my_tesla,ElectricCa))
'''

#Question 10: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.
'''
class Battery:
    def battery_info(self):
        return "This is a battery"
class Engine:
    def engine_info(self):
        return "This is engine"
    
class ElectricCarTwo(Battery,Engine,Car):
    pass

my_new_tesla=ElectricCarTwo("Tesla","Model S")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())
'''

