'''
I might see a simplified version of this mission already First Word (simplified). This mission is a little bit
more complex as not only English letters can be in the given string.

You are given a string where you have to find its first word.

When solving a task pay attention to the following points:

There can be dots and commas in a string.
A string can start with a letter or, for example, one/multiple dot(s) or space(s).
A word can contain an apostrophe and it's a part of a word.
The whole text can be represented with one word and that's it.
Input: A string.

Output: A string.

Example:

assert first_word("Hello world") == "Hello"
assert first_word(" a word ") == "a"
assert first_word("don't touch it") == "don't"
assert first_word("greetings, friends") == "greetings"

How it is used: the first word is a command in a command line

Precondition: the text can contain a-z A-Z , . '

----------
----------

Puede que ya exista una versión simplificada de esta misión Primera palabra (simplificada). Esta
misión es un poco más compleja, ya que no sólo las letras inglesas pueden estar en la cadena dada.

Se te da una cadena en la que tienes que encontrar su primera palabra.

Cuando resuelvas una tarea presta atención a los siguientes puntos:

En una cadena puede haber puntos y comas.
Una cadena puede empezar por una letra o, por ejemplo, por uno o varios puntos o espacios.
Una palabra puede contener un apóstrofo y es parte de una palabra.
Todo el texto puede representarse con una palabra y ya está.
Entrada: Una cadena.

Salida: Una cadena.

Ejemplo:

assert primera_palabra("Hola mundo") == "Hola"
assert primera_palabra(" una palabra ") == "una"
assert primera_palabra("no lo toques") == "no"
assert primera_palabra("saludos, amigos") == "saludos"

Cómo se utiliza: la primera palabra es un comando en una línea de comandos

Condición previa: el texto puede contener a-z A-Z , . '

Traducción realizada con la versión gratuita del traductor www.DeepL.com/Translator
'''


def first_word(text: str) -> str:
    # your code here
    # replace all commas and dots with spaces
    text = text.replace(',', ' ').replace('.', ' ')

    # strip leading and trailing spaces
    text = text.strip()

    # split the string into a list of words
    words = text.split()

    # return the first word
    return words[0]


print("Example:")
print(first_word("Hello world"))

# These "asserts" are used for self-checking
assert first_word("Hello world") == "Hello"
assert first_word(" a word ") == "a"
assert first_word("don't touch it") == "don't"
assert first_word("greetings, friends") == "greetings"
assert first_word("... and so on ...") == "and"
assert first_word("hi") == "hi"

print("The mission is done! Click 'Check Solution' to earn rewards!")
