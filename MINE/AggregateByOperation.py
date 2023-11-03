"""
This is a further development of Convert and Aggregate mission. You are given a list of
tuples. Each tuple consists of two values: a string and an integer. You need to create
and return a dictionary, where keys are string values (except the first character) from
input tuples. Values are aggregated integer values from input tuples for each specific
key. Each aggregating operation must be done according to the operation sign - the first
character of string key. Division by zero should be ignored. The resulted dictionary
should not include items with empty key or zero value.

Input: List of tuples.

Output: Dictionary.

Examples:
assert aggr_operation([("+a", 7), ("-b", 8), ("*a", 10)]) == {"a": 70, "b": -8}
assert aggr_operation([]) == {}
assert aggr_operation([("+a", 5), ("+a", -5), ("-a", 5), ("-a", -5)]) == {}
assert aggr_operation([("*a", 0), ("=a", 0), ("/a", 0), ("-a", -5)]) == {"a": 5}

----------
----------

Se trata de un desarrollo posterior de la misión Convertir y Agregar. Se le da una lista de
tuplas. Cada tupla consta de dos valores: una cadena y un entero. Tienes que crear y devolver
un diccionario, donde las claves son valores de cadena (excepto el primer carácter) de
las tuplas de entrada. Los valores son valores enteros agregados de tuplas de entrada
para cada clave específica. Cada operación de agregación debe realizarse según el signo
de la operación: el primer carácter de la clave de cadena. La división por cero debe
ignorarse. El diccionario resultante no debe incluir elementos con clave vacía o valor cero.

Entrada: Lista de tuplas.

Salida: Diccionario.

Ejemplo:
assert aggr_operation([("+a", 7), ("-b", 8), ("*a", 10)]) == {"a": 70, "b": -8}
assert aggr_operation([]) == {}
assert aggr_operation([("+a", 5), ("+a", -5), ("-a", 5), ("-a", -5)]) == {}
assert aggr_operation([("*a", 0), ("=a", 0), ("/a", 0), ("-a", -5)]) == {"a": 5}
"""

from collections import defaultdict


def aggr_operation(data: list[tuple[str, int]]) -> dict[str, int]:
    # your code here
    d = defaultdict(int)

    for s, n in data:
        sing, key = s[0], s[1:]

        if sing == "+":
            d[key] += n
        elif sing == "-":
            d[key] -= n
        elif sing == "*":
            d[key] *= n
        elif sing == "/" and n != 0:
            d[key] /= n
        elif sing == "=":
            d[key] = n

    return {k: v for k, v in d.items() if k and v}


print("Example:")
print(aggr_operation([("+a", 7), ("-b", 8), ("*a", 10)]))

# These "asserts" are used for self-checking
assert aggr_operation([("+a", 7), ("-b", 8), ("*a", 10)]) == {"a": 70, "b": -8}
assert aggr_operation([]) == {}
assert aggr_operation([("+a", 5), ("+a", -5), ("-a", 5), ("-a", -5)]) == {}
assert aggr_operation([("*a", 0), ("=a", 0), ("/a", 0), ("-a", -5)]) == {"a": 5}

print("The mission is done! Click 'Check Solution' to earn rewards!")
