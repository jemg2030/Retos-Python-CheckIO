'''
A pangram (Greek: παν γράμμα, pan gramma, "every letter") or holoalphabetic sentence for a given
alphabet is a sentence using every letter of the alphabet at least once. Perhaps you are familiar
with the well known pangram "The quick brown fox jumps over the lazy dog".

For this mission, we will use the latin alphabet (A-Z). You are given a text with latin letters and
punctuation symbols. You need to check if the sentence is a pangram or not. Case does not matter.

Input: A text as a string.

Output: Whether the sentence is a pangram or not as a boolean.

Examples:
assert check_pangram("The quick brown fox jumps over the lazy dog.") == True
assert check_pangram("ABCDEF") == False
assert check_pangram("abcdefghijklmnopqrstuvwxyz") == True
assert check_pangram("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == True

How it is used: Pangrams have been used to display typefaces, test equipment, and develop skills in
handwriting, calligraphy, and keyboarding for ages.

Precondition:
all(ch in (string.punctuation + string.ascii_letters + " ") for ch in text);
0 < len(text).

----------
----------

Un pangrama (en griego: παν γράμμα, pan gramma, "cada letra") u oración holoalfabética para un
alfabeto dado es una oración que utiliza cada letra del alfabeto al menos una vez. Quizá conozca
el conocido pangrama "El zorro rápido salta sobre el perro perezoso".

Para esta misión, estaremos utilizando el alfabeto latino (A-Z). Se le da un texto con letras latinas
y signos de puntuación. Debe registrar si la frase es un pangrama o no. Las mayúsculas y minúsculas
son indiferentes.

Entrada: Un texto en forma de cadena.

Salida: Si la frase es un pangrama o no como un booleano.

Ejemplo:
assert check_pangram("El zorro rápido salta sobre el perro perezoso") == True
assert check_pangram("ABCDEF") == False
assert check_pangram("abcdefghijklmnopqrstuvwxyz") == True
assert check_pangram("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == True

Cómo se utiliza: Los pangramas se han utilizado durante siglos para mostrar tipos de letra, probar
equipos y desarrollar habilidades de escritura a mano, caligrafía y teclado.

Condición previa:
all(ch in (cadena.puntuación + cadena.ascii_letras + " ") for ch in texto);
0 < len(texto).
'''


import string


def check_pangram(text: str) -> bool:
    # your code here
    alphabet = set(string.ascii_lowercase)
    text = text.lower()
    text = ''.join(ch for ch in text if ch.isalpha())
    text_letters = set(text)
    return alphabet == text_letters


print("Example:")
print(check_pangram("The quick brown fox jumps over the lazy dog."))

# These "asserts" are used for self-checking
assert check_pangram("The quick brown fox jumps over the lazy dog.") == True
assert check_pangram("ABCDEF") == False
assert check_pangram("abcdefghijklmnopqrstuvwxyz") == True
assert check_pangram("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == True
assert check_pangram("abcdefghijklmnopqrstuvwxy") == False
assert (
    check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!")
    == True
)
assert check_pangram("As quirky joke, chefs won't pay devil magic zebra tax.") == True
assert check_pangram("Six big devils from Japan quickly forgot how to walt.") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
