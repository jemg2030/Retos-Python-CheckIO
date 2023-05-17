'''
There are four substring missions that were born all in one day and you shouldn’t need more than
one day to solve them. All of these missions can be simply solved by brute force, but is it always
the best way to go? (You might not have access to all of those missions yet, but they are going to
be available with more opened islands on the map).

This mission is the first one of the series. Here you should find the length of the longest substring
that consists of the same letter. For example, line "aaabbcaaaa" contains four substrings with the same
letters "aaa", "bb","c" and "aaaa". The last substring is the longest one, which makes it the answer.

Input: A string.

Output: An int.

Example:
assert long_repeat("sdsffffse") == 4
assert long_repeat("ddvvrwwwrggg") == 3

----------
----------

Hay cuatro misiones de subcadenas que nacieron todas en un día y no deberías necesitar más de un
día para resolverlas. Todas estas misiones pueden resolverse simplemente por fuerza bruta, pero
¿es siempre la mejor manera de hacerlo? (Puede que aún no tengas acceso a todas estas misiones,
pero estarán disponibles con más islas abiertas en el mapa).

Esta misión es la primera de la serie. Aquí debes encontrar la longitud de la subcadena más larga
que conste de la misma letra. Por ejemplo, la línea "aaabbcaaaa" contiene cuatro subcadenas con
las mismas letras "aaa", "bb", "c" y "aaaa". La última subcadena es la más larga, por lo que es
la respuesta.

Entrada: Una cadena.

Salida: Un int.

Ejemplo:
assert long_repeat("sdsffffse") == 4
assert long_repeat("ddvvrwwwrggg") == 3
'''


def long_repeat(line: str) -> int:
    """
    length the longest substring that consists of the same char
    """
    # your code here
    if not line:
        return 0

    longest_length: int = 1  # Initialize with 1 as the minimum length of a substring

    current_char = line[0]
    current_count = 1

    for i in range(1, len(line)):
        if line[i] == current_char:
            current_count += 1
        else:
            if current_count > longest_length:
                longest_length = current_count
            current_char = line[i]
            current_count = 1

    if current_count > longest_length:
        longest_length = current_count

    return longest_length


print("Example:")
print(long_repeat("sdsffffse"))

assert long_repeat("sdsffffse") == 4
assert long_repeat("ddvvrwwwrggg") == 3

print("The mission is done! Click 'Check Solution' to earn rewards!")
