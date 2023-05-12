'''
You are given a list of tuples. Each tuple consists of two values: a string and an integer. You need
to create and return a dictionary, where keys are string values from input tuples and values are
aggregated (summed) integer values from input tuples for each specific key. The resulted dictionary
should not include items with empty key or zero value.

Input: List of tuples.

Output: Dictionary.

Examples:
assert conv_aggr([("a", 7), ("b", 8), ("a", 10)]) == {"a": 17, "b": 8}
assert conv_aggr([]) == {}
assert conv_aggr([("a", 5), ("a", -5)]) == {}
assert conv_aggr([("a", 5), ("a", 5), ("a", 0)]) == {"a": 10}

----------
----------

Se le da una lista de tuplas. Cada tupla consta de dos valores: una cadena y un entero. Debe
crear y devolver un diccionario en el que las claves sean valores de cadena de las tuplas de
entrada y los valores sean valores enteros agregados (sumados) de las tuplas de entrada para
cada clave específica. El diccionario resultante no debe incluir elementos con clave vacía o valor cero.

Entrada: Lista de tuplas.

Salida: Diccionario.

Ejemplo:
assert conv_aggr([("a", 7), ("b", 8), ("a", 10)]) == {"a": 17, "b": 8}
assert conv_aggr([]) == {}
assert conv_aggr([("a", 5), ("a", -5)]) == {}
assert conv_aggr([("a", 5), ("a", 5), ("a", 0)]) == {"a": 10}
'''


def conv_aggr(data: list[tuple[str, int]]) -> dict[str, int]:
    # your code here
    result = {}
    for tup in data:
        key, val = tup
        if key == "":
            continue
        if key in result:
            result[key] += val
        else:
            result[key] = val

        if result[key] == 0:
            del result[key]
    return result


print("Example:")
print(conv_aggr([("a", 7), ("b", 8), ("a", 10)]))

# These "asserts" are used for self-checking
assert conv_aggr([("a", 7), ("b", 8), ("a", 10)]) == {"a": 17, "b": 8}
assert conv_aggr([]) == {}
assert conv_aggr([("a", 5), ("a", -5)]) == {}
assert conv_aggr([("a", 5), ("a", 5), ("a", 0)]) == {"a": 10}
assert conv_aggr([("a", 5), ("", 15)]) == {"a": 5}

print("The mission is done! Click 'Check Solution' to earn rewards!")
