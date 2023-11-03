"""
Your task in this mission is to truncate a sentence to a length that does not exceed a
given number of characters.

If the given sentence already is short enough, you don't have to do anything to it. But
if it needs to be truncated, the omission must be indicated by concatenating an ellipsis
("...") to the end of the shortened sentence.

The shortened sentence can contain complete words and spaces.
It must neither contain truncated words nor trailing spaces.
The ellipsis has been taken into account for the allowed number of characters, so it
does not count against the given length.

Input: Two arguments:

one-line sentence as a string (str);
max length of the truncated sentence as an integer (int).
Output: The shortened sentence plus the ellipsis (if required) as a one-line string (str).

Examples:
assert cut_sentence("Hi my name is Alex", 8) == "Hi my..."
assert cut_sentence("Hi my name is Alex", 4) == "Hi..."
assert cut_sentence("Hi my name is Alex", 20) == "Hi my name is Alex"
assert cut_sentence("Hi my name is Alex", 18) == "Hi my name is Alex"

Preconditions:
line.startswith(' ') == False
0 < len(line) ≤ 79
0 < length ≤ 76
all(char in string.ascii_letters + ' ' for char in line)

----------
----------

Su tarea en esta misión consiste en truncar una frase hasta una longitud que no supere un
número determinado de caracteres.

Si la frase dada ya es lo suficientemente corta, no tienes que hacerle nada. Pero si es
necesario truncarla, la omisión debe indicarse concatenando una elipsis ("...") al final
de la frase acortada.

La frase acortada puede contener palabras completas y espacios.
No debe contener palabras truncadas ni espacios finales.
La elipsis se ha tenido en cuenta para el número de caracteres permitido, por lo que no
cuenta para la longitud dada.

Entrada: Dos argumentos:

frase de una línea como cadena (str);
longitud máxima de la frase truncada como número entero (int).
Salida: La frase acortada más la elipsis (si es necesaria) como cadena de una línea (str).

Ejemplo:
assert frase_corta("Hola me llamo Alex", 8) == "Hola mi..."
assert cut_sentence("Hola, me llamo Alex", 4) == "Hola..."
assert cut_sentence("Hola, me llamo Alex", 20) == "Hola, me llamo Alex"
assert cut_sentence("Hola, me llamo Alex", 18) == "Hola, me llamo Alex"

Precondiciones:
line.startswith(' ') == False
0 < len(línea) ≤ 79
0 < longitud ≤ 76
all(char en cadena.ascii_letras + ' ' para char en línea)
"""


def cut_sentence(line: str, length: int) -> str:
    # your code here
    """
    Cut a given sentence, so it becomes shorter than or equal to a given length.
    """
    if length >= len(line):
        return line
    for i in range(length, 0, -1):
        if line[i] == " ":
            return line[:i] + "..."
    return "..."


print("Example:")
print(cut_sentence("Hi my name is Alex", 4))

# These "asserts" are used for self-checking
assert cut_sentence("Hi my name is Alex", 8) == "Hi my..."
assert cut_sentence("Hi my name is Alex", 4) == "Hi..."
assert cut_sentence("Hi my name is Alex", 20) == "Hi my name is Alex"
assert cut_sentence("Hi my name is Alex", 18) == "Hi my name is Alex"

print("The mission is done! Click 'Check Solution' to earn rewards!")
