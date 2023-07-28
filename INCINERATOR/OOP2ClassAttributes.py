"""
2.1. Add the wheels class attribute inside the Car class and assign it a value of "four".

2.2. Add the doors class attribute inside the Car class and assign it a value of 4.

----------
----------

2.1. Añade el atributo de clase wheels dentro de la clase Car y asígnale el valor "four".

2.2. Añade el atributo de clase doors dentro de la clase Car y asígnale el valor 4.
"""


# Taken from mission OOP 1: First Look at Class and Object

# show me some OOP magic here
class Car:
    wheels = "four"
    doors = 4


my_car = Car()

# show me some OOP magic here
print(my_car.wheels)  # Output: "four"
print(my_car.doors)  # Output: 4
