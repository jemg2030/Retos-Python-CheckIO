"""
Stephan works with simple forms when constructing something, and he need some programming
tools to calculate his expenses. Let's take a trip back to our school days and pull out
some simple geometry for this.

You should write a function to calculate the area of simple figures: circles, rectangles
and triangles. You are give an arbitrary number of arguments and depending on this, the
function calculates area for the different figures.

One argument -- The diameter of a circle and you need calculate the area of the circle.
Two arguments -- The side lengths of a rectangle and you need calculate the area of the
rectangle.
Three arguments -- The lengths of each side on a triangle and you need calculate the area
of the triangle.

The result should be given with two digits precision as ±0.01.

Tips: Think about how to work with an arbitrary number of arguments .

Input: One, two or three arguments as floats or as integers.

Output: The area of the circle, the rectangle or the triangle as a float.

Example:
simple_areas(3) == 7.07
simple_areas(2, 2) == 4
simple_areas(2, 3) == 6
simple_areas(3, 5, 4) == 6
simple_areas(1.5, 2.5, 2) == 1.5

How it is used: Python can be an useful tool for mathematics and science. You can easily
implement any formulas or math algorithm with this simple and readable programming language.

Precondition:
0 < len(args) ≤ 3
all(0 < x ≤ 1000 for x in args)
For "triangle" cases the sum of the lengths of any two sides always exceeds the length of the third side.

----------
----------

Stephan trabaja con formas sencillas cuando construye algo, y necesita algunas herramientas
de programación para calcular sus gastos. Volvamos a nuestros días de colegio y saquemos
algo de geometría simple para esto.

Debes escribir una función para calcular el área de figuras sencillas: círculos, rectángulos
y triángulos. Se te da un número arbitrario de argumentos y, en función de ellos, la función
calcula el área de las distintas figuras.

Un argumento -- El diámetro de un círculo y necesita calcular el área del círculo.
Dos argumentos -- Las longitudes de los lados de un rectángulo y necesitas calcular el área
del rectángulo.
Tres argumentos -- Las longitudes de cada lado de un triángulo y necesitas calcular el área
del triángulo.

El resultado debe ser dado con dos dígitos de precisión como ±0.01.

Consejos: Piense en cómo trabajar con un número arbitrario de argumentos .

Entrada: Uno, dos o tres argumentos como flotantes o enteros.

Salida: El área del círculo, el rectángulo o el triángulo como float.

Ejemplo:
simple_areas(3) == 7.07
simple_areas(2, 2) == 4
simple_areas(2, 3) == 6
área_simple(3, 5, 4) == 6
área_simple(1,5, 2,5, 2) == 1,5

Cómo se utiliza: Python puede ser una herramienta útil para las matemáticas y la ciencia.
Puedes implementar fácilmente cualquier fórmula o algoritmo matemático con este lenguaje de
programación sencillo y legible.

Precondición:
0 < len(args) ≤ 3
all(0 < x ≤ 1000 para x en args)
Para los casos de "triángulo" la suma de las longitudes de dos lados cualesquiera siempre
supera la longitud del tercer lado.
"""


import math


def simple_areas(*args):
    if len(args) == 1:
        # Calculate area of a circle: A = π * r^2
        radius = args[0] / 2
        area = math.pi * radius**2
    elif len(args) == 2:
        # Calculate area of a rectangle: A = width * height
        area = args[0] * args[1]
    elif len(args) == 3:
        # Calculate area of a triangle using Heron's formula
        a, b, c = args
        s = (a + b + c) / 2  # Semi-perimeter of the triangle
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    else:
        raise ValueError("Invalid number of arguments")

    return round(area, 2)


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1**significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(simple_areas(3), 7.07), "Circle"
    assert almost_equal(simple_areas(2, 2), 4), "Square"
    assert almost_equal(simple_areas(2, 3), 6), "Rectangle"
    assert almost_equal(simple_areas(3, 5, 4), 6), "Triangle"
    assert almost_equal(simple_areas(1.5, 2.5, 2), 1.5), "Small triangle"
