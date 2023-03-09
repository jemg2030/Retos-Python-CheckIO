'''
Split the string into pairs of two characters. If the string contains an odd number of characters,
then the missing second character of the final pair should be replaced with an underscore ('_').

Input: A string.

Output: A list or another Iterable of strings.

Example:
assert list(split_pairs("abcd")) == ["ab", "cd"]
assert list(split_pairs("abc")) == ["ab", "c_"]
assert list(split_pairs("abcdf")) == ["ab", "cd", "f_"]
assert list(split_pairs("a")) == ["a_"]

Precondition: 0 <= len(text) <= 100

----------
----------

Divide la cadena en pares de dos caracteres. Si la cadena contiene un número impar de caracteres,
el segundo carácter que falte en el último par se sustituirá por un guión bajo ('_').

Entrada: Una cadena.

Salida: Una lista u otro Iterable de cadenas.

Ejemplo:
assert lista(split_pares("abcd")) == ["ab", "cd"]
assert list(split_pairs("abc")) == ["ab", "c_"]
assert list(split_pairs("abcdf")) == ["ab", "cd", "f_"]
assert list(split_pairs("a")) == ["a_"]

Precondición: 0 <= len(texto) <= 100
'''


from typing import Iterable


def split_pairs(text: str) -> Iterable[str]:
    # your code here
    result = []
    for i in range(0, len(text), 2):
        pair = text[i:i + 2]
        if len(pair) < 2:
            pair += "_"
        result.append(pair)
    return result


print("Example:")
print(list(split_pairs("abcd")))

assert list(split_pairs("abcd")) == ["ab", "cd"]
assert list(split_pairs("abc")) == ["ab", "c_"]
assert list(split_pairs("abcdf")) == ["ab", "cd", "f_"]
assert list(split_pairs("a")) == ["a_"]
assert list(split_pairs("")) == []

print("The mission is done! Click 'Check Solution' to earn rewards!")
