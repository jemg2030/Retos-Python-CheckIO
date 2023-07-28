"""
6.1. Rewrite start_engine and stop_engine methods of the ElectricCar class to display another
messages "Electric motor has started" and "Electric motor has stopped" respectively and change
attributes the same way.

6.2. Call the start_engine method for the my_electric_car instance.

6.3. Create my_electric_car2 (values 60, "Toyota", "Prius"), start and stop its engine.

----------
----------

6.1. Reescribe los métodos start_engine y stop_engine de la clase ElectricCar para mostrar
otros mensajes "El motor eléctrico ha arrancado" y "El motor eléctrico se ha parado" respectivamente
y cambia los atributos de la misma manera.

6.2. Llama al método start_engine para la instancia my_electric_car.

6.3. Crea mi_coche_eléctrico2 (valores 60, "Toyota", "Prius"), arranca y para su motor.
"""


# Taken from mission OOP 5: Parent - Child

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

    def start_engine(self):
        print("Electric motor has started")
        self.working_engine = True

    def stop_engine(self):
        print("Electric motor has stopped")
        self.working_engine = False


# Create my_electric_car instance with battery_capacity=100, brand="Tesla", model="Model 3"
my_electric_car = ElectricCar(battery_capacity=100, brand="Tesla", model="Model 3")

# Call start_engine method for my_electric_car
my_electric_car.start_engine()  # Output: "Electric motor has started"

# Create my_electric_car2 instance with battery_capacity=60, brand="Toyota", model="Prius"
my_electric_car2 = ElectricCar(battery_capacity=60, brand="Toyota", model="Prius")

# Call start_engine and stop_engine methods for my_electric_car2
my_electric_car2.start_engine()  # Output: "Electric motor has started"
my_electric_car2.stop_engine()  # Output: "Electric motor has stopped"
