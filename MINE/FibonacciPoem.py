"""
This mission is inspired by the following Brian Bilston's facebook post:

Split a given text into multiline one with "\n", where each line includes number of
words equal to the current Fibonacci number.

Here are some clarifications:

Fibonacci sequence starts from 0, 1, but the result string should include only non-empty lines;
in case, there are not enough words for current line - complement to proper length with "_";
punctuation marks are considered as a part of a previous or next word.

Let's look at the schematic example ("w" for a word):

"w w w w w w w w" -> '''w
                        w
                        w w
                        w w w
                        w _ _ _ _'''
Input: A string (str).

Output: A string (str).

Examples:
assert fibo_poem("") == ""
assert fibo_poem("Django framework") == "Django\nframework"
assert fibo_poem("Zen of Python") == "Zen\nof\nPython _"
assert (
    fibo_poem("There are three kinds of lies: Lies, damned lies, and the benchmarks.")
    == "There\nare\nthree kinds\nof lies: Lies,\ndamned lies, and the benchmarks."
)

----------
----------

Esta misión está inspirada en el siguiente post de facebook de Brian Bilston:

Dividir un texto dado en uno multilínea con "\n", donde cada línea incluye un número de
palabras igual al número Fibonacci actual.

He aquí algunas aclaraciones:

La secuencia Fibonacci comienza en 0, 1, pero la cadena resultante debe incluir sólo líneas no vacías;
en caso de que no haya suficientes palabras para la línea actual - complemente a la longitud adecuada con "_";
los signos de puntuación se consideran parte de la palabra anterior o siguiente.

Veamos el ejemplo esquemático ("w" para una palabra):

"w w w w w w w" -> '''w
                        w
                        w w
                        w w w
                        w _ _ _ _'''
Entrada: Una cadena (str).

Salida: Una cadena (str).

Ejemplo:
assert fibo_poem("") == ""
assert fibo_poem("Django framework") == "Django\nframework"
assert fibo_poem("Zen of Python") == "Zen\nof\nPython _"
assert (
    fibo_poem("Hay tres tipos de mentiras: Mentiras, malditas mentiras y los puntos de referencia")
    == "Hay tres clases de mentiras: Las mentiras, las malditas mentiras y los puntos de referencia".
)

https://en.wikipedia.org/wiki/Fibonacci_sequence
"""


def fibo_poem(text: str) -> str:
    # your code here
    a, b, text, poem = 0, 1, text.split(), []
    while text:
        row, text = text[:b], text[b:]
        row.extend("_" * (b - len(row)))
        poem.append(" ".join(row))
        a, b = b, a + b
    return "\n".join(poem)


print("Example:")
print(fibo_poem("Zen of Python"))

# These "asserts" are used for self-checking
assert fibo_poem("") == ""
assert fibo_poem("Django framework") == "Django\nframework"
assert fibo_poem("Zen of Python") == "Zen\nof\nPython _"
assert (
    fibo_poem("There are three kinds of lies: Lies, damned lies, and the benchmarks.")
    == "There\nare\nthree kinds\nof lies: Lies,\ndamned lies, and the benchmarks."
)

print("The mission is done! Click 'Check Solution' to earn rewards!")
