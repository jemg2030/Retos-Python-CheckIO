'''
How old are you in a number of days? It's easy to calculate - just subtract your birthday from today. We
could make this a real challenge though and count the difference between any dates.

You are given two dates as an tuple with three numbers - a year, month and day. For example: 19 April
1982 will be (1982, 4, 19). You should find the difference in days between the given dates. For example
between today and tomorrow = 1 day. The difference will always be either a positive number or zero, so don't
forget about the absolute value.

Input: Two dates as tuples of integers.

Output: The difference between the dates in days as an integer.

Examples:
assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238

How it is used: Python has batteries included, so in this mission you’ll need to learn how to use completed
modules so that you don't have to invent the bicycle all over again.

Preconditions:
dates between 1 january 1 and 31 december 9999;
dates are correct.

----------
----------

¿Cuántos días tienes? Es fácil de calcular: sólo tienes que restar tu cumpleaños al día de hoy. Pero podemos
convertirlo en un verdadero reto y contar la diferencia entre dos fechas cualesquiera.

Te damos dos fechas en forma de tupla con tres números: año, mes y día. Por ejemplo: 19 de abril de 1982 será
(1982, 4, 19). Debes encontrar la diferencia en días entre las fechas dadas. Por ejemplo, entre hoy y mañana = 1 día.
La diferencia siempre será un número positivo o cero, así que no te olvides del valor absoluto.

Entrada: Dos fechas como tuplas de enteros.

Salida: La diferencia entre las fechas en días como un entero.

Ejemplo:
assert diferencia_días((1982, 4, 19), (1982, 4, 22)) == 3
assert diferencia_días((2014, 1, 1), (2014, 8, 27)) == 238
assert diferencia_días((2014, 8, 27), (2014, 1, 1)) == 238

Cómo se utiliza: Python tiene pilas incluidas, así que en esta misión tendrás que aprender a usar módulos
completos para no tener que volver a inventar la bicicleta.

Condiciones previas:
fechas entre el 1 de enero y el 31 de diciembre de 9999;
las fechas son correctas.
'''


from datetime import datetime


def days_diff(a: tuple[int, int, int], b: tuple[int, int, int]) -> int:
    # your code here
    d1 = datetime(*a)
    d2 = datetime(*b)
    delta = abs(d1 - d2)
    return delta.days


print("Example:")
print(days_diff((1982, 4, 19), (1982, 4, 22)))

assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238

print("The mission is done! Click 'Check Solution' to earn rewards!")
