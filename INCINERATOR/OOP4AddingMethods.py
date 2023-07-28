"""
4.1. Add the working_engine class attribute inside the Car class and assign it a value of False.

4.2. Add a start_engine method to the Car class, that displays the message "Engine has started"
and changes the working_engine value of the instance of class to True.

4.3. Add a stop_engine method to the Car class, that displays the message "Engine has stopped"
and changes the working_engine value of the instance of class to False.

4.4. Call the start_engine method for both instances some_car1, some_car2.

----------
----------

4.1. Añade el atributo de clase working_engine dentro de la clase Car y asígnale el valor False.

4.2. Añade un método start_engine a la clase Car, que muestre el mensaje "Engine has started" y
cambie el valor de working_engine de la instancia de la clase a True.

4.3. Añadir un método stop_engine a la clase Car, que muestre el mensaje "Engine has stopped" y
cambie el valor de working_engine de la instancia de la clase a False.

4.4. Llama al método arrancar_motor para ambas instancias algún_coche1, algún_coche2.
"""


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
