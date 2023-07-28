"""
3.1. Add an __init__() function to the Car class that takes the brand and model arguments
and assigns them to the appropriate object attributes.

3.2. You already have an object my_car that was created without passing additional arguments.
So, in order not to cause errors when creating an object in this way, let's add a default value
for the arguments of the __init__() function They mast have values of empty string "".

3.3. Create two new Car objects by passing the following string values as arguments. some_car1:
brand - Ford, model - Mustang; some_car2: model - Camaro. Notice, that the second car has only model,
it's brand must remains default.

----------
----------

3.1. Añadir una función __init__() a la clase Coche que tome los argumentos de marca y modelo
y los asigne a los atributos apropiados del objeto.

3.2. Ya tienes un objeto mi_coche que fue creado sin pasar argumentos adicionales. Así que, para
no causar errores al crear un objeto de esta manera, vamos a añadir un valor por defecto para los
argumentos de la función __init__() Ellos mástil tener valores de cadena vacía "".

3.3. Cree dos nuevos objetos Car pasando los siguientes valores de cadena como argumentos.
some_car1: marca - Ford, modelo - Mustang; some_car2: modelo - Camaro. Tenga en cuenta, que el
segundo coche sólo tiene modelo, su marca debe permanecer por defecto.
"""


# Taken from mission OOP 2: Class Attributes

# Taken from mission OOP 1: First Look at Class and Object
# show me some OOP magic here
class Car:
    wheels = "four"
    doors = 4

    def __init__(self, brand="", model=""):
        self.brand = brand
        self.model = model


# Creating a Car object without passing any additional arguments (using default values)
my_car = Car()
print(my_car.brand)  # Output: ""
print(my_car.model)  # Output: ""

# Creating two new Car objects with specific arguments
some_car1 = Car(brand="Ford", model="Mustang")
some_car2 = Car(model="Camaro")

print(some_car1.brand)  # Output: "Ford"
print(some_car1.model)  # Output: "Mustang"

print(some_car2.brand)  # Output: "" (default value)
print(some_car2.model)  # Output: "Camaro"
