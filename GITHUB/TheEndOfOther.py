'''
For language training our Robots want to learn about suffixes.

In this task, you are given a set of words in lower case. Check whether there is a pair of words,
such that one word is the end of another (a suffix of another). For example: {"hi", "hello", "lo"} --
"lo" is the end of "hello", so the result is True.

Input: Words as a set of strings.

Output: True or False, as a boolean.

Example:
checkio({"hello", "lo", "he"}) == True
checkio({"hello", "la", "hellow", "cow"}) == False
checkio({"walk", "duckwalk"}) == True
checkio({"one"}) == False
checkio({"helicopter", "li", "he"}) == False

How it is used: Here you can learn about iterating through set type and string data type functions.

Precondition: 2 ≤ len(words) < 30
all(re.match(r"\A[a-z]{1,99}\Z", w) for w in words)

Each player can create their own missions on CheckiO starting at level 9. You have the ability
to create challenges for your friends and maybe even get your mission published on CheckiO for the
whole community!

----------
----------

Para la formación lingüística, nuestros robots quieren aprender los sufijos.

En esta tarea, se le da un conjunto de palabras en minúsculas. Registre si hay un par de palabras, de
tal manera que una palabra sea el final de otra (un sufijo de otra). Por ejemplo: {"hi", "hello", "lo"} --
"lo" es el final de "hola", por lo que el resultado es True.

Entrada: Palabras como un conjunto de cadenas.

Salida: Verdadero o Falso, como booleano.

Ejemplo:
checkio({"hola", "lo", "he"}) == Verdadero
checkio({"hello", "la", "hellow", "cow"}) == False
checkio({"walk", "duckwalk"}) == True
checkio({"uno"}) == False
checkio({"helicopter", "li", "he"}) == False

Cómo se utiliza: Aquí puedes aprender a iterar a través de funciones de tipo conjunto y de tipo cadena de
datos.

Precondición: 2 ≤ len(words) < 30
all(re.match(r"\A[a-z]{1,99}\Z", w) for w in words)

Cada jugador puede crear sus propias misiones en CheckiO a partir del nivel 9. Puedes crear retos para
tus amigos e incluso publicar tu misión en CheckiO para toda la comunidad.
'''


def checkio(words_set):
    for word1 in words_set:
        for word2 in words_set:
            if word1 != word2 and word1.endswith(word2):
                return True
    return False


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio({"hello", "lo", "he"}))

    assert checkio({"hello", "lo", "he"}) == True, "helLO"
    assert checkio({"hello", "la", "hellow", "cow"}) == False, "hellow la cow"
    assert checkio({"walk", "duckwalk"}) == True, "duck to walk"
    assert checkio({"one"}) == False, "Only One"
    assert checkio({"helicopter", "li", "he"}) == False, "Only end"
    print("Done! Time to check!")
