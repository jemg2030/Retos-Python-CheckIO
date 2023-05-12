'''
You are given a text, which contains different English letters and punctuation symbols. You
should find the most frequent letter in the text. The letter returned must be in lower case.
While checking for the most wanted letter, casing does not matter, so for the purpose of your
search, "A" == "a". Make sure you do not count punctuation symbols, digits and whitespaces,
only letters.

If you have two or more letters with the same frequency, then return the letter which comes
first in the Latin alphabet. For example -- "one" contains "o", "n", "e" only once for each,
thus we choose "e".

Input: A text for analysis as a string.

Output: The most frequent letter in lower case as a string.

Example:
assert checkio("Hello World!") == "l"
assert checkio("How do you do?") == "o"
assert checkio("One") == "e"
assert checkio("Oops!") == "o"

How it is used: For most decryption tasks you need to know the frequency of occurrence for
various letters in a section of text. For example: we can easily crack a simple addition or
substitution cipher if we know the frequency in which letters appear. This is interesting
stuff for language experts!

Precondition:
A text contains only ASCII symbols.
0 < len(text) ≤ 105

----------
----------

Se le dará un texto, el cual contiene diferentes letras y símbolos de puntuación. Debes
encontrar la letra más frecuente en el texto. La letra retornada debe estar en minúscula.
Mientras realizas la búsqueda de la letra, no considerar diferencias entre mayúsculas y
minúsculas, asi que para efectos de la búsqueda, "A" == "a". Asegurarse de no contar los
signos de puntuación, dígitos o espacios en blanco, considerar solo letras.

Si se tiene una o más letras con la misma frecuencia, entonces el resultado será la letra que
aparece primero en el alfabeto latino. Por ejemplo -- "one" contiene "o", "n", "e" solo hay una
por cada letra, por lo tanto escogemos la letra "e".

Entrada: Una cadena de caracteres (string) como texto para el análisis.

Salida: La letra mas frecuente en minúscula como una cadena de caracteres (string).

Ejemplo:
assert checkio("Hello World!") == "l"
assert checkio("How do you do?") == "o"
assert checkio("One") == "e"
assert checkio("Oops!") == "o"

¿Cómo es usado?: Para la mayoría de procedimientos de desencriptado necesitas conocer la
frecuencia de ocurrencia de varias letras en una sección de texto. Por ejemplo: podemos
descifrar con facilidad un simple cifrado de adición o substitución si conocemos la
frecuencia con la cual aparecen las letras. ¡Esto es algo interesante para los expertos en
idiomas!

Pre-condicion:
El texto contiene solo caracteres ASCII.
0 < len(text) ≤ 105
'''


def checkio(text: str) -> str:

    #replace this for solution
    frequencies = {}
    text = text.lower()

    for char in text:
        if char.isalpha():
            frequencies[char] = frequencies.get(char, 0) + 1

    max_frequency = max(frequencies.values(), default=0)
    most_frequent_letters = [letter for letter, frequency in frequencies.items() if frequency == max_frequency]

    return min(most_frequent_letters, default='')


if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
