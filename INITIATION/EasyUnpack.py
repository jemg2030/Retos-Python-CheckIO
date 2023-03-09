'''
Your mission here is to create a function that gets a tuple and returns a tuple with only 3 elements -
the first, third and second element from the last for the given tuple.

example

One important thing worth pointing out is that you need to use index in order to extract elements from the
tuple. Pay attention, index counting starts from 0, not from 1. Which means that if you need to get the first
element from the tuple elements, you should do elements[0], and the second element is elements[1].

Input: A tuple, at least 3 elements long.

Output: A tuple.

Examples:
assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
assert easy_unpack((6, 3, 7)) == (6, 7, 3)

----------
----------

Tu misión aquí es crear una función que obtenga una tupla y devuelva una tupla con sólo 3 elementos -
el primer, tercer y segundo elemento desde el último para la tupla dada.

Una cosa importante que vale la pena señalar es que es necesario utilizar el índice con el fin de extraer
los elementos de la tupla. Presta atención, el conteo de índices comienza desde 0, no desde 1. Lo que significa
que si necesitas obtener el primer elemento de la tupla elements, debes hacer elements[0], y el segundo elemento
es elements[1].

Entrada: Una tupla de al menos 3 elementos.

Salida: Una tupla.

Ejemplos:
assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
assert easy_unpack((6, 3, 7)) == (6, 7, 3)
'''


def easy_unpack(elements: tuple) -> tuple:
    # your code here
    return elements[0], elements[2], elements[-2]


print("Example:")
print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))

# These "asserts" are used for self-checking
assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
assert easy_unpack((6, 3, 7)) == (6, 7, 3)

print("The mission is done! Click 'Check Solution' to earn rewards!")
