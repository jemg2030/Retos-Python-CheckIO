'''
An anagram is a type of word play, the result of rearranging the letters of a word or phrase to
produce a new word or phrase, using all the original letters exactly once. Two words are anagrams
to each other if we can get one from another by rearranging the letters. Anagrams are case-insensitive
and don't take account whitespaces. For example: "Gram Ring Mop" and "Programming" are anagrams. But
"Hello" and "Ole Oh" are not.

You are given two words or phrase. Try to verify are they anagrams or not.

Input: Two arguments as strings.

Output: Are they anagrams or not as boolean (True or False)

Examples:
assert verify_anagrams("Programming", "Gram Ring Mop") == True
assert verify_anagrams("Hello", "Ole Oh") == False
assert verify_anagrams("Kyoto", "Tokyo") == True

How it is used: Anagramming can be a fun way to train your brain, but they have and another application.
Psychologists use anagram-oriented tests, often called "anagram solution tasks", to assess the implicit
memory. Anagrams are connected to pseudonyms, by the fact that they may conceal or reveal, or operate
somewhere in between like a mask that can establish identity. In addition to this, multiple anagramming
is a technique sometimes used to solve some kinds of cryptograms.

Preconditions:
0 < |first_word| < 100;
0 < |second_word| < 100;
Words contain only ASCII latin letters and whitespaces.

----------
----------

Un anagrama un un tipo de juego de palabras, el resultado de reordenar las letras de una palabra
u oración para producir otra palabra u oración nueva, using todas las letras originales de la
sentencia anterior. Dos palabras son anagramas entre ellas si somos capaces de llegar crear una
de ellas reordenando las letras de la otra. Los anagramas son case-insensitive (distinguen entre
mayúsculas y minúsculas) y no tienen en cuenta los espacios en blanco. Por ejemplo: "Gram Ring Mop"
and "Programming" son anagramas. Pero "Hello" y "Ole Oh" no.

Dadas dos palabras o frases intenta verificar si son anagramas o no.

Input: Dos argumentos de tipo string.

Output: Confirmar o desmentir si son anagramas como booleano (True o False)

Examples:
assert verify_anagrams("Programming", "Gram Ring Mop") == True
assert verify_anagrams("Hello", "Ole Oh") == False
assert verify_anagrams("Kyoto", "Tokyo") == True

Para qué se usa: Anagramming puede ser una divertidad manera de entrenar el cerebro, pero tiene
otras aplicaciones. Los piscologos usan tests basados en anagramas, normalmente llamados "anagram
solution tasks", para evaluar la memoria implicita. Los anagramas están conectados con los pseudonimos,
por el hecho de que pueden ocultar o revelar, u operar en algún punto intermedio, como una máscara que
puede establecer la identidad. Además de esto, el "multiple anagramming" es una tecnica que se usa a veces
para resolver criptosistemas.

Condicion previa:
0 < |primera palabra| < 100;
0 < |segunda palabra| < 100;
Las palabras solo contienen letras latinas ASCII y espacios en blanco.
'''


def verify_anagrams(a: str, b: str) -> bool:
    # your code here
    # Remove whitespace characters and convert to lowercase
    first_word = a.replace(" ", "").lower()
    second_word = b.replace(" ", "").lower()

    # Sort the letters of both strings
    sorted_first = sorted(first_word)
    sorted_second = sorted(second_word)

    # Debugging output
    print(sorted_first)
    print(sorted_second)

    # Compare the sorted strings
    return sorted_first == sorted_second


print("Example:")
print(verify_anagrams("Programming", "Gram Ring Mop"))

assert verify_anagrams("Programming", "Gram Ring Mop") == True
assert verify_anagrams("Hello", "Ole Oh") == False
assert verify_anagrams("Kyoto", "Tokyo") == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
