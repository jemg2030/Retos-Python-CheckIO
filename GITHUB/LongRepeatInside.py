'''
There are four substring missions that were born all in one day and you shouldn’t be needed more
than one day to solve them. All of those mission can be simply solved by brute force, but is it
always the best way to go? (you might not have access to all of those missions yet, but they are
going to be available with more opened islands on the map).

It is the fourth and the last mission of the series. But if in the first mission you needed to find
repeating letters, then in this one you should find a repeating sequence inside the substring. I
have an example for you: in a string "abababc" - "ab" is a sequence that repeats more than once,
so the answer will be "ababab"

Input: String.

Output: String.

Example:
assert repeat_inside("aaaaa") == "aaaaa"
assert repeat_inside("aabbff") == "aa"
assert repeat_inside("aababcc") == "abab"
assert repeat_inside("abc") == ""

----------
----------

Hay cuatro misiones de subcadenas que nacieron todas en un día y no deberías necesitar más de un día
para resolverlas. Todas esas misiones pueden resolverse simplemente por fuerza bruta, pero ¿es siempre
la mejor manera de hacerlo? (puede que aún no tengas acceso a todas esas misiones, pero estarán
disponibles con más islas abiertas en el mapa).

Es la cuarta y última misión de la serie. Pero si en la primera misión necesitabas encontrar letras
repetidas, en esta deberás encontrar una secuencia repetida dentro de la subcadena. Tengo un ejemplo
para ti: en una cadena "abababc" - "ab" es una secuencia que se repite más de una vez, así que la
respuesta será "ababab".

Entrada: Cadena.

Salida: Cadena.

Ejemplo:
assert repetir_dentro("aaaaa") == "aaaaa"
assert repetir_dentro("aabbff") == "aa"
assert repeat_inside("aababcc") == "abab"
assert repeat_inside("abc") == ""
'''


def longest_substring(string, predicate):
    n = len(string)
    for length in range(n, -1, -1):
        for start in range(n - length + 1):
            substring = string[start:start+length]
            if predicate(substring):
                return substring

def repeat_inside(line: str) -> str:
    """
    first the longest repeating substring
    """
    # your code here
    return longest_substring(line, lambda s: s in (s + s)[1:-1])


print("Example:")
print(repeat_inside("aaaaa"))

assert repeat_inside("aaaaa") == "aaaaa"
assert repeat_inside("aabbff") == "aa"
assert repeat_inside("aababcc") == "abab"
assert repeat_inside("abc") == ""
assert repeat_inside("abcabcabab") == "abcabc"

print("The mission is done! Click 'Check Solution' to earn rewards!")
