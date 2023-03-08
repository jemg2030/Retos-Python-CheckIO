'''
"Sometimes, zeros resemble very tasty donut. And every time we finish a donut, we want another, and then another, and
then another..."
You are given a list of integers. Your task in this mission is to duplicate (..., 🍩, ... --> ..., 🍩, 🍩, ...) all
zeros (think about donuts ;-P) and return the result as any Iterable. Let's look on the example:
[1, 0, 2, 0] -> [1, 0, 0, 2, 0, 0]

Input: A list of integers.

Output: A list on another Iterable (tuple, generator, iterator) of integers.

Examples:
assert list(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0])) == [
    1,
    0,
    0,
    2,
    3,
    0,
    0,
    4,
    5,
    0,
    0,
]
assert list(duplicate_zeros([0, 0, 0, 0])) == [0, 0, 0, 0, 0, 0, 0, 0]
assert list(duplicate_zeros([100, 10, 0, 101, 1000])) == [100, 10, 0, 0, 101, 1000]

If you have solved this mission, you can enjoy a 🍩 with peace of mind!=)

---------
---------

"A veces, los ceros parecen rosquillas muy sabrosas. Y cada vez que nos acabamos un donut, queremos otro, y luego otro,
y luego otro..."

Se te da una lista de números enteros. Tu tarea en esta misión es duplicar (..., 🍩, ... --> ..., 🍩, 🍩, ...) todos
los ceros (piensa en donuts ;-P) y devolver el resultado como un Iterable cualquiera. Veamos el ejemplo:
[1, 0, 2, 0] -> [1, 0, 0, 2, 0, 0]

Entrada: Una lista de enteros.

Salida: Una lista en otro Iterable (tupla, generador, iterador) de enteros.

Ejemplos:

assert lista(duplicar_zeros([1, 0, 2, 3, 0, 4, 5, 0])) == [
    1,
    0,
    0,
    2,
    3,
    0,
    0,
    4,
    5,
    0,
    0,
]
assert list(duplicate_zeros([0, 0, 0, 0])) == [0, 0, 0, 0, 0, 0, 0, 0]
assert list(duplicate_zeros([100, 10, 0, 101, 1000])) == [100, 10, 0, 0, 101, 1000]

Si has resuelto esta misión, podrás disfrutar de un 🍩 con tranquilidad!=)
'''


from collections.abc import Iterable


def duplicate_zeros(donuts: list[int]) -> Iterable[int]:
    # your code here
    new_donuts = []
    for num in donuts:
        new_donuts.append(num)
        if num == 0:
            new_donuts.append(0)
    return new_donuts


print("Example:")
print(list(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0])))

# These "asserts" are used for self-checking
assert list(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0])) == [
    1,
    0,
    0,
    2,
    3,
    0,
    0,
    4,
    5,
    0,
    0,
]
assert list(duplicate_zeros([0, 0, 0, 0])) == [0, 0, 0, 0, 0, 0, 0, 0]
assert list(duplicate_zeros([100, 10, 0, 101, 1000])) == [100, 10, 0, 0, 101, 1000]

print("The mission is done! Click 'Check Solution' to earn rewards!")