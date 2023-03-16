'''
You have a text and a list of words. You need to check if the words in a list appear in the same
order as in the given text.

Cases you should expect while solving this challenge:

a word from the list is not in the text - your function should return False;
any word can appear more than once in a text - use only the first one;
two words in the given list are the same - your function should return False;
the condition is case sensitive, which means 'hi' and 'Hi' are two different words;
the text includes only English letters and spaces.
Input: Two arguments. The first one is a given text, the second is a list of words.

Output: A bool.

Examples:
assert words_order("hi world im here", ["world", "here"]) == True
assert words_order("hi world im here", ["here", "world"]) == False
assert words_order("hi world im here", ["world"]) == True
assert words_order("hi world im here", ["world", "here", "hi"]) == False

----------
----------

Tiene un texto y una lista de palabras. Debe registrar si las palabras de una lista aparecen en el mismo
orden que en el texto dado.

Casos que debe esperar al resolver este reto:

una palabra de la lista no aparece en el texto - su función debe devolver False;
cualquier palabra puede aparecer más de una vez en un texto - utilice sólo la primera;
dos palabras de la lista dada son iguales - su función debe devolver False;
la condición distingue entre mayúsculas y minúsculas, lo que significa que "hi" y "Hi" son dos palabras diferentes;
el texto sólo incluye letras inglesas y espacios.
Entrada: Dos argumentos. El primero es un texto dado, el segundo es una lista de palabras.

Salida: Un bool.

Ejemplo:
assert orden_palabras("hola mundo estoy aqui", ["mundo", "aqui"]) == True
assert orden_palabras("hola mundo estoy aquí", ["aquí", "mundo"]) == False
assert orden_palabras("hola mundo estoy aquí", ["mundo"]) == True
assert words_order("hola mundo estoy aquí", ["mundo", "aquí", "hola"]) == False
'''


def words_order(text: str, words: list) -> bool:
    # your code here
    text_words = text.split()
    if len(set(words)) != len(words):
        return False
    index = 0
    for word in words:
        try:
            i = text_words.index(word, index)
        except ValueError:
            return False
        index = i + 1
    return True

print("Example:")
print(words_order("hi world im here", ["world", "here"]))

# These "asserts" are used for self-checking
assert words_order("hi world im here", ["world", "here"]) == True
assert words_order("hi world im here", ["here", "world"]) == False
assert words_order("hi world im here", ["world"]) == True
assert words_order("hi world im here", ["world", "here", "hi"]) == False
assert words_order("hi world im here", ["world", "im", "here"]) == True
assert words_order("hi world im here", ["world", "hi", "here"]) == False
assert words_order("hi world im here", ["world", "world"]) == False
assert words_order("hi world im here", ["country", "world"]) == False
assert words_order("hi world im here", ["wo", "rld"]) == False
assert words_order("", ["world", "here"]) == False
assert words_order("hi world world im here", ["world", "world"]) == False
assert (
    words_order("hi world world im here hi world world im here", ["world", "here"])
    == True
)

print("The mission is done! Click 'Check Solution' to earn rewards!")
