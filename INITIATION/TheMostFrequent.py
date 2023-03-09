'''
You have a sequence of strings, and you’d like to determine the most frequently occurring string in
the sequence. It can be only one.

Input: non empty list of strings.

Output: a string.

Example:
assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"
assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"

----------
----------

Tiene una secuencia de cadenas y desea determinar la cadena que aparece con más frecuencia en la
secuencia. Sólo puede ser una.

Entrada: lista no vacía de cadenas.

Salida: una cadena.

Ejemplo:
assert más_frecuente(["a", "b", "c", "a", "b", "a"]) == "a"
assert más_frecuente(["a", "a", "bi", "bi", "bi"]) == "bi"
'''


def most_frequent(data: list[str]) -> str:
    # your code here
    freq = {}
    for s in data:
        if s in freq:
            freq[s] += 1
        else:
            freq[s] = 1
    max_freq = 0
    most_freq = None
    for s, f in freq.items():
        if f > max_freq:
            max_freq = f
            most_freq = s
    return most_freq


print("Example:")
print(most_frequent(["a", "b", "c", "a", "b", "a"]))

# These "asserts" are used for self-checking
assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"
assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"

print("The mission is done! Click 'Check Solution' to earn rewards!")
