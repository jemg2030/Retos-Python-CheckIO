'''
You are given two strings and you have to find an index of the second occurrence of the second string in
the first one.

Let's go through the first example where you need to find the second occurrence of "s" in a word "sims".
It’s easy to find its first occurrence with a function index or find which will point out that "s" is the
first symbol in a word "sims" and therefore the index of the first occurrence is 0. But we have to find the
second "s" which is 4th in a row and that means that the index of the second occurrence (and the answer to
a question) is 3.

Input: Two strings.

Output: Int or None

Example:
assert second_index("sims", "s") == 3
assert second_index("find the river", "e") == 12
assert second_index("hi", " ") == None
assert second_index("hi mayor", " ") == None

---------
---------

Se le dan dos cadenas y tiene que encontrar un índice de la segunda aparición de la segunda cadena en
la primera.

Veamos el primer ejemplo, en el que necesitas encontrar la segunda aparición de "s" en la palabra "sims".
Es fácil encontrar su primera aparición con una función index o find que nos indicará que "s" es el primer
símbolo en una palabra "sims" y por tanto el índice de la primera aparición es 0. Pero tenemos que encontrar
la segunda "s" que es la 4ª en una fila y eso significa que el índice de la segunda aparición (y la respuesta
a una pregunta) es 3.

Entrada: Dos cadenas.

Salida: Int o Ninguno

Ejemplo:

assert segundo_índice("sims", "s") == 3
assert second_index("encontrar el río", "e") == 12
assert second_index("hi", " ") == None
assert second_index("hola alcalde", " ") == None

Traducción realizada con la versión gratuita del traductor www.DeepL.com/Translator
'''


def second_index(text: str, symbol: str) -> [int, None]:
    """
    returns the second index of a symbol in a given text
    """
    # your code here
    # Find the index of the first occurrence of the symbol text
    first_index = text.find(symbol)
    if first_index == -1:
        # symbol text not found, return None
        return None
    # Search for the second occurrence of the symbol text
    second_index = text.find(symbol, first_index + 1)
    if second_index == -1:
        # Second occurrence not found, return None
        return None
    else:
        return second_index


print("Example:")
print(second_index("sims", "s"))

assert second_index("sims", "s") == 3
assert second_index("find the river", "e") == 12
assert second_index("hi", " ") == None
assert second_index("hi mayor", " ") == None
assert second_index("hi mr Mayor", " ") == 5

print("The mission is done! Click 'Check Solution' to earn rewards!")