'''
In a given string you should reverse every word, but the words should stay in their places.

Input: A string.

Output: A string.

Example:
assert backward_string_by_word("") == ""
assert backward_string_by_word("world") == "dlrow"
assert backward_string_by_word("hello world") == "olleh dlrow"
assert backward_string_by_word("hello   world") == "olleh   dlrow"

Precondition: The line consists only from alphabetical symbols and spaces.

----------
----------

En una cadena dada debe invertir cada palabra, pero las palabras deben permanecer en su lugar.

Entrada: Una cadena.

Salida: Una cadena.

Ejemplo:
assert cadena_por_palabra("") == ""
assert cadena_por_palabra("mundo") == "dlrow"
assert backward_string_by_word("hola mundo") == "olleh dlrow"
assert retroceso_palabra_por_palabra("hola mundo") == "olleh dlrow"

Condición previa: La línea se compone sólo de símbolos alfabéticos y espacios.

Traducción realizada con la versión gratuita del traductor www.DeepL.com/Translator
'''


def backward_string_by_word(text: str) -> str:
    # your code here
    words = text.split(' ')
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)


print("Example:")
print(backward_string_by_word(""))

# These "asserts" are used for self-checking
assert backward_string_by_word("") == ""
assert backward_string_by_word("world") == "dlrow"
assert backward_string_by_word("hello world") == "olleh dlrow"
assert backward_string_by_word("hello   world") == "olleh   dlrow"
assert backward_string_by_word("welcome to a game") == "emoclew ot a emag"

print("The mission is done! Click 'Check Solution' to earn rewards!")
