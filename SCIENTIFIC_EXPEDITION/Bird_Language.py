'''
Stephan has a friend who happens to be a little mechbird. Recently, he was trying to teach it how to
speak basic language. Today the bird spoke its first word: "hieeelalaooo". This sounds a lot like "hello",
but with too many vowels. Stephan asked Nikola for help and he helped to examine how the bird changes words.
With the information they discovered, we should help them to make a translation module.

The bird converts words by two rules:
- after each consonant letter the bird appends a random vowel letter (l ⇒ la or le);
- after each vowel letter the bird appends two of the same letter (a ⇒ aaa);
Vowels letters == "aeiouy".

You are given an ornithological phrase as several words which are separated by white-spaces (each pair of
words by one whitespace). The bird does not know how to punctuate its phrases and only speaks words as
letters. All words are given in lowercase. You should translate this phrase from the bird language to
something more understandable.

Input: A bird phrase as a string.

Output: The translation as a string.

Example:
assert translate("hieeelalaooo") == "hello"
assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
assert translate("aaa bo cy da eee fe") == "a b c d e f"
assert translate("sooooso aaaaaaaaa") == "sos aaa"

How it is used: This is a similar cipher to those used by children when they invent their own "bird"
language. Now you will be ready to crack the code.

Precondition: re.match("\A([a-z]+\ ?)+(?<!\ )\Z", phrase)
A phrase always has the translation.

----------
----------

Stephan tiene un amigo quien resulta ser un pequeño pájaro mecánico (mechbird). Recientemente, él
estaba tratando de enseñarle a su amigo cómo hablar usando lenguaje básico, y el día de hoy, el
pájaro dijo su primera palabra: "hieeelalaooo". Esto suena muy parecido a "hello" (“hola” en inglés),
pero con demasiadas vocales. Stephan le pidió ayuda a Nikola, y juntos, examinaron cómo el ave cambia
las palabras. Con la información que descubrieron, debemos ayudarles a crear un módulo de traducción.

El pájaro convierte las palabras siguiendo dos reglas:
- después de cada consonante, el pájaro añade una vocal aleatoria (l ⇒ la ó le);
- después de cada vocal, el pájaro añade dos veces dicha vocal (a ⇒ aaa);
Vocales == "aeiouy".

Se te dará una “frase ornitológica” como varias palabras separadas por espacios en blanco (cada par de
palabras las separa un espacio). El pájaro no sabe cómo usar signos de puntuación y por lo tanto sólo
usa letras en sus palabras. Todas las palabras están dadas en minúsculas. Deberás traducir la frase de
la lengua de aves a algo más comprensible.

Datos de Entrada: Una frase de nuestra ave, como una cadena (str).

Salida: La traducción, como una cadena (str).

Ejemplo:
assert translate("hieeelalaooo") == "hello"
assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
assert translate("aaa bo cy da eee fe") == "a b c d e f"
assert translate("sooooso aaaaaaaaa") == "sos aaa"

¿Cómo se usa?: Este es una algoritmo de cifrado similar al que usan los niños cuando inventan su
propio lenguaje "pájaro". ¡En adelante estarás listo para descifrar su código!

Condiciones: re.match("\A([a-z]+\ ?)+(?<!\ )\Z", phrase)
La frase siempre tiene traducción.
'''

VOWELS = "aeiouy"


def translate(text: str) -> str:
    # your code here
    translated_words = []
    words = text.split()
    for word in words:
        translated_word = ""
        i = 0
        while i < len(word):
            if word[i] not in VOWELS:
                translated_word += word[i]
                i += 2
            else:
                translated_word += word[i]
                i += 3 if i < len(word) - 1 and word[i] == word[i + 1] else 1
        translated_words.append(translated_word)
    return " ".join(translated_words)


print("Example:")
print(translate("hieeelalaooo"))

# These "asserts" are used for self-checking
assert translate("hieeelalaooo") == "hello"
assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
assert translate("aaa bo cy da eee fe") == "a b c d e f"
assert translate("sooooso aaaaaaaaa") == "sos aaa"

print("The mission is done! Click 'Check Solution' to earn rewards!")
