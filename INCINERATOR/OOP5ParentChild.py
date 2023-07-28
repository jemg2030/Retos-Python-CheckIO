"""
5.1. Create an ElectricCar class that inherits properties from the Car class.

5.2. Modify the __init__ method of the ElectricCar class so that it uses super() to call
the __init__ method of the Car class.

5.3. Add a new attribute battery_capacity of type int to the ElectricCar class __init__ method.
This attribute must be passing as argument. Put this argument before brand and model, because
arguments without default values must go before ones that have.

5.4. Create a my_electric_car instance of the ElectricCar class, passing battery_capacity, brand,
model with values 100, "Tesla", "Model 3" respectively

----------
----------

5.1. Crea una clase Cocheeléctrico que herede propiedades de la clase Coche.

5.2. Modifica el método __init__ de la clase ElectricCar para que utilice super() para
llamar al método __init__ de la clase Car.

5.3. Añade un nuevo atributo battery_capacity de tipo int al método __init__ de la clase ElectricCar.
Este atributo debe pasarse como argumento. Pon este argumento antes de marca y modelo, porque los
argumentos sin valores por defecto deben ir antes que los que sí los tienen.

5.4. Crea una instancia my_electric_car de la clase ElectricCar, pasando battery_capacity, brand,
model con los valores 100, "Tesla", "Model 3" respectivamente
"""


# Taken from mission OOP 4: Adding Methods

# Taken from mission OOP 3: Initializing
# Taken from mission OOP 2: Class Attributes
# Taken from mission OOP 1: First Look at Class and Object
# show me some OOP magic here
class Car:
    wheels = "four"
    doors = 4
    working_engine = False

    def __init__(self, brand="", model=""):
        self.brand = brand
        self.model = model

    def start_engine(self):
        print("Engine has started")
        self.working_engine = True

    def stop_engine(self):
        print("Engine has stopped")
        self.working_engine = False


# Creating a Car object without passing any additional arguments (using default values)
my_car = Car()
# Creating two new Car objects with specific arguments
some_car1 = Car(brand="Ford", model="Mustang")
some_car2 = Car(model="Camaro")
# Calling start_engine method for some_car1 and some_car2
some_car1.start_engine()  # Output: "Engine has started"
some_car2.start_engine()  # Output: "Engine has started"


class ElectricCar(Car):
    def __init__(self, battery_capacity, brand="", model=""):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity


my_electric_car = ElectricCar(battery_capacity=100, brand="Tesla", model="Model 3")
