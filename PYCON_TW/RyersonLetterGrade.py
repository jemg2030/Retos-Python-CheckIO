"""
Given the grade percentage for the course, calculate and return the letter grade that would
appear in the Ryerson's grade transcript, as defined on the page Ryerson Grade Scales. The
letter grade should be returned as a string that consists of the uppercase letter followed
by the possible modifier "+" or "-".

Input: Grade percentage as an integer.

Output: The letter grade as a string.

Examples:
The initial code contains grade and percentage sequences. Feel free to change them in any way.

assert ryerson_letter_grade(45) == "F"
assert ryerson_letter_grade(62) == "C-"

Precondition: argument can be from 0 to 150.

The mission was taken from Python CCPS 109 Fall 2018. It is taught for Ryerson Chang School
of Continuing Education by Ilkka Kokkarinen

----------
----------

Dado el porcentaje de calificación del curso, calcule y devuelva la calificación en letras
que aparecería en el expediente académico de Ryerson, tal como se define en la página Escalas
de calificaciones de Ryerson. La calificación debe devolverse como una cadena formada por la
letra mayúscula seguida del posible modificador "+" o "-".

Entrada: Porcentaje de la calificación como un número entero.

Salida: La letra de la calificación como cadena.

Ejemplos:
El código inicial contiene secuencias de grado y porcentaje. Siéntete libre de cambiarlas como
quieras.

assert ryerson_letter_grade(45) == "F"
assert ryerson_letter_grade(62) == "C-"

Precondición: el argumento puede ser de 0 a 150.

La misión fue tomada de Python CCPS 109 Otoño 2018. Se imparte para la escuela de educación
continua Ryerson Chang por Ilkka Kokkarinen.

Links:
------
https://www.cs.ryerson.ca/~ikokkari/
"""


# feel free to change table structure in any way
LETTERS = [ch + sign for ch in "ABCD" for sign in ("+", "", "-")] + ["F"]
MIN_PERCENTAGES = 90, 85, 80, 77, 73, 70, 67, 63, 60, 57, 53, 50, 0


def ryerson_letter_grade(pct: int) -> str:
    # your code here
    grade_scale = [
        (0, 49, "F"),
        (50, 52, "D-"),
        (53, 56, "D"),
        (57, 59, "D+"),
        (60, 62, "C-"),
        (63, 66, "C"),
        (67, 69, "C+"),
        (70, 72, "B-"),
        (73, 76, "B"),
        (77, 79, "B+"),
        (80, 84, "A-"),
        (85, 89, "A"),
        (90, 150, "A+"),
    ]

    for lower, upper, grade in grade_scale:
        if lower <= pct <= upper:
            return grade


print("Example:")
print(ryerson_letter_grade(45))

assert ryerson_letter_grade(45) == "F"
assert ryerson_letter_grade(62) == "C-"

print("The mission is done! Click 'Check Solution' to earn rewards!")
