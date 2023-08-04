"""
7.1. Add the fuel_used attribute inside __init__ method of Car class without changing its
arguments and assign it a value of 0 liters.

7.2. Add the fuel_consumption attribute inside __init__ method of Car class, passing it as a
method argument with default value of 7 (liters/100 km).

7.3. Add a drive method to the Car class that takes the distance argument of type int (km).
If an instance of class had started - increment fuel_used with the proper value and display
the message "Currently driven {distance} km, total fuel used - {fuel_used} l". If the instance
had not started, display "Start the car before driving!".

7.4. Rewrite the method for the ElectricCar class, do not increment fuel_used (since electric
car doesn't used fuel), change the successful message to "Currently driven {distance} km on
electric motor", keep the unsuccessful message unchanged.

----------
----------

7.1. Añade el atributo fuel_used dentro del método __init__ de la clase Car sin cambiar
sus argumentos y asígnale un valor de 0 litros.

7.2. Añade el atributo consumo_combustible dentro del método __init__ de la clase Coche,
pasándolo como argumento del método con valor por defecto de 7 (litros/100 km).

7.3. Añadir un método drive a la clase Car que tome el argumento distance de tipo int (km).
Si una instancia de la clase ha arrancado - incrementa fuel_used con el valor apropiado y
muestra el mensaje "Actualmente conducido {distancia} km, combustible total usado - {fuel_used} l".
Si la instancia no ha arrancado, muestre el mensaje "Arranque el coche antes de conducir".

7.4. Reescribe el método para la clase ElectricCar, no incrementes fuel_used (ya que el coche
eléctrico no usa combustible), cambia el mensaje de éxito a "Actualmente conducido {distancia}
km con motor eléctrico", mantén el mensaje de fracaso sin cambios.
"""

# show me some OOP magic here
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.fuel_used = 0  # Added fuel_used attribute with initial value of 0 liters


class Car:
    def __init__(self, make, model, year, fuel_consumption=7):
        self.make = make
        self.model = model
        self.year = year
        self.fuel_used = 0
        self.fuel_consumption = fuel_consumption  # Added fuel_consumption attribute with default value of 7 liters/100 km

    def drive(self, distance):
        if self.fuel_used == 0:
            print("Start the car before driving!")
        else:
            fuel_used_for_trip = distance * self.fuel_consumption / 100
            self.fuel_used += fuel_used_for_trip
            print(
                f"Currently driven {distance} km, total fuel used - {self.fuel_used:.2f} l"
            )


class ElectricCar(Car):
    def drive(self, distance):
        if self.fuel_used == 0:
            print("Start the car before driving!")
        else:
            print(f"Currently driven {distance} km on electric motor")


# test_car = Car()
my_car = Car()
# Creating 'my_car' instance of the Car class with the required arguments
my_car = Car(name="Toyota Corolla", color="Blue", price=25000)
# Creating 'my_car' instance of the Car class with the required arguments
my_car = Car(name="Toyota Corolla", color="Blue", price=25000)

# Create instances of Car and ElectricCar
car = Car("Toyota", "Corolla", 25000)
car.start_engine()
car.drive(100)  # Output: "Currently driven 100 km, total fuel used - 7.00 l"

electric_car = ElectricCar("Nissan Leaf", "Blue", 30000)
electric_car.start_engine()
electric_car.drive(150)  # Output: "Currently driven 150 km on electric motor"
