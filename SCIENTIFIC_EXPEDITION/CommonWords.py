'''
Let's continue examining words. You are given two strings with words separated by commas. Try
to find what is common between these strings. The words in the same string don't repeat.

Your function should find all of the words that appear in both strings. The result must be
represented as a string of words separated by commas in alphabetic order.

Input: Two arguments as strings.

Output: The common words as a string.

Example:
assert checkio("hello,world", "hello,earth") == "hello"
assert checkio("one,two,three", "four,five,six") == ""
assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two"

How it is used: Here you can learn how to work with strings and sets. This knowledge can be useful
for linguistic analysis.

Precondition:
Each string contains no more than 10 words.
All words separated by commas.

----------
----------

Sigamos examinando palabras. Se te asignaran dos cadenas ( str ) con palabras, separadas por comas,
y deberás encontrar cual palabra es común a las dos cadenas. Ten en cuenta que las palabras no se
repiten al interior de una misma cadena.

Tu función deberá encontrar todas las palabras que aparecen en ambas cadenas. El resultado debe ser
representado como una cadena de palabras, separadas por comas y en orden alfabético .

Datos de Entrada: Dos argumentos, como cadenas ( str ).

Salida: Las palabras comunes, como una cadena ( str ).

Ejemplo:
assert checkio("hello,world", "hello,earth") == "hello"
assert checkio("one,two,three", "four,five,six") == ""
assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two"

¿Cómo se usa?: Aquí podrás aprender cómo trabajar con cadenas y conjuntos. Este conocimiento puede ser
útil para análisis lingüísticos.

Condiciones:
Cada cadena contiene un máximo de 10 palabras.
Todas las palabras están separadas por comas.
Todas las palabras se componen de letras latinas en minúsculas.
'''


def checkio(line1: str, line2: str) -> str:
    # your code here
    # Step 1: Split the input strings into lists of words
    words1 = line1.split(',')
    words2 = line2.split(',')

    # Step 2: Convert the lists of words into sets
    set1 = set(words1)
    set2 = set(words2)

    # Step 3: Find the intersection of the two sets
    common_set = set1.intersection(set2)

    # Step 4: Convert the resulting set into a sorted list of words
    common_words = sorted(list(common_set))

    # Step 5: Join the sorted list of words using commas as separators
    result = ','.join(common_words)
    return result


print("Example:")
print(checkio("hello,world", "hello,earth"))

assert checkio("hello,world", "hello,earth") == "hello"
assert checkio("one,two,three", "four,five,six") == ""
assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two"

print("The mission is done! Click 'Check Solution' to earn rewards!")
