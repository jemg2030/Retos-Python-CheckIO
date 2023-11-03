"""
You are given a dictionary, where keys and values are strings. Your function should
return a dictionary as well, where keys and values from input dictionary are switched:
input keys become output values and vice versa. Looks easy? It is so! The only thing
left to mention: the values in the result dictionary should be sets (so the input key(s) -
the element(s) of the set). Good luck!

Input: A dictionary.

Output: A dictionary.

Examples:
assert switch_dict({"rouses": "red", "car": "red", "sky": "blue"}) == {
    "red": {"car", "rouses"},
    "blue": {"sky"},
}
assert switch_dict({"1": "one", "2": "two", "3": "one", "4": "two"}) == {
    "one": {"3", "1"},
    "two": {"4", "2"},
}
assert switch_dict({"a": "b", "b": "c", "c": "a"}) == {
    "b": {"a"},
    "c": {"b"},
    "a": {"c"},
}

----------
----------

Se le da un diccionario, donde las claves y los valores son cadenas. Su función debe
devolver también un diccionario, donde las claves y los valores del diccionario de entrada
se intercambian: las claves de entrada se convierten en valores de salida y viceversa.
¿Parece fácil? Pues sí. Lo único que queda por mencionar: los valores en el diccionario
resultante deben ser conjuntos (por lo que la(s) clave(s) de entrada - el(los) elemento(s)
del conjunto). ¡Suerte!

Entrada: Un diccionario.

Salida: Un diccionario.

Ejemplo:
assert switch_dict({"rouses": "red", "car": "red", "sky": "blue"}) == {
    "rojo": {"coche", "rouses"},
    "azul": {"sky"},
}
assert switch_dict({"1": "uno", "2": "dos", "3": "uno", "4": "dos"}) == {
    "uno": {"3", "1"},
    "dos": {"4", "2"},
}
assert switch_dict({"a": "b", "b": "c", "c": "a"}) == {
    "b": {"a"},
    "c": {"b"},
    "a": {"c"},
}
"""


from collections import defaultdict
from typing import Any


def switch_dict(data: dict[str, str]) -> defaultdict[Any, set]:
    # your code here
    d = defaultdict(set)
    for k, v in data.items():
        d[v].add(k)
    return d


print("Example:")
print(switch_dict({"rouses": "red", "car": "red", "sky": "blue"}))

# These "asserts" are used for self-checking
assert switch_dict({"rouses": "red", "car": "red", "sky": "blue"}) == {
    "red": {"car", "rouses"},
    "blue": {"sky"},
}
assert switch_dict({"1": "one", "2": "two", "3": "one", "4": "two"}) == {
    "one": {"3", "1"},
    "two": {"4", "2"},
}
assert switch_dict({"a": "b", "b": "c", "c": "a"}) == {
    "b": {"a"},
    "c": {"b"},
    "a": {"c"},
}

print("The mission is done! Click 'Check Solution' to earn rewards!")
