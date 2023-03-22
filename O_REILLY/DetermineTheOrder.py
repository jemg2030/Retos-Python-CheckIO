'''
The Robots have found an encrypted message. We cannot decrypt it at the moment, but we can take the
first steps towards doing so. You have a set of "words", all in lower case, and each word contains
symbols in "alphabetical order". (it's not your typical alphabetical order, but a new and different
order.) We need to determine the order of the symbols from each "word" and create a single "word" with
all of these symbols, placing them in the new alphabetical order. In some cases, if we cannot determine
the order for several symbols, you should use the traditional latin alphabetical order. For example: Given
words "acb", "bd", "zwa". As we can see "z" and "w" must be before "a" and "d" after "b". So the result is
"zwacbd".

Input: Words as a list of strings.

Output: The order as a string.

Examples:
assert checkio(["acb", "bd", "zwa"]) == "zwacbd"
assert checkio(["klm", "kadl", "lsm"]) == "kadlsm"
assert checkio(["a", "b", "c"]) == "abc"
assert checkio(["aazzss"]) == "azs"
assert checkio(["dfg", "frt", "tyg"]) == "dfrtyg"
assert checkio(["hello", "low", "lino", "itttnosw"]) == "helitnosw"
assert checkio(["my", "name", "myke"]) == "namyke"
assert checkio(["xxxyyz", "yyww", "wwtt", "ttzz"]) == "xywtz"
assert checkio(["axton", "bxton"]) == "abxton"
assert checkio(["is", "not", "abc", "nots", "iabcn"]) == "iabcnots"
assert checkio(["qwerty", "asdfg", "zxcvb", "yagz"]) == "qwertyasdfgzxcvb"
How it is used: This concept can be useful for the cryptology, helping you to find regularities and
patterns in natural text and ciphered messages.

Preconditions:
for each test, there can be the only one solution;
0 < |words| < 10.

----------
----------

Los Robots han encontrado un mensaje encriptado. De momento no podemos desencriptarlo, pero podemos dar
los primeros pasos para hacerlo. Tiene un conjunto de "palabras", todas en minúsculas, y cada palabra
contiene símbolos en "orden alfabético". (No es el típico orden alfabético, sino un orden nuevo y diferente.)
Tenemos que determinar el orden de los símbolos de cada "palabra" y crear una única "palabra" con todos esos
símbolos, colocándolos en el nuevo orden alfabético. En algunos casos, si no podemos determinar el orden de
varios símbolos, hay que utilizar el orden alfabético latino tradicional. Por ejemplo: Dadas las palabras
"acb", "bd", "zwa". Como podemos ver, "z" y "w" deben estar antes de "a" y "d" después de "b". El resultado es
"zwacbd".

Entrada: Palabras como una lista de cadenas.

Salida: El orden como una cadena.

Ejemplo:
assert checkio(["acb", "bd", "zwa"]) == "zwacbd"
assert checkio(["klm", "kadl", "lsm"]) == "kadlsm"
assert checkio(["a", "b", "c"]) == "abc"
assert checkio(["aazzss"]) == "azs"
assert checkio(["dfg", "frt", "tyg"]) == "dfrtyg"
assert checkio(["hello", "low", "lino", "itttnosw"]) == "helitnosw"
assert checkio(["my", "name", "myke"]) == "namyke"
assert checkio(["xxxyyz", "yyww", "wwtt", "ttzz"]) == "xywtz"
assert checkio(["axton", "bxton"]) == "abxton"
assert checkio(["is", "not", "abc", "nots", "iabcn"]) == "iabcnots"
assert checkio(["qwerty", "asdfg", "zxcvb", "yagz"]) == "qwertyasdfgzxcvb"
Cómo se utiliza: Este concepto puede ser útil para la criptología, ayudando a encontrar regularidades
y patrones en texto natural y mensajes cifrados.

Precondiciones:
para cada prueba, sólo puede haber una solución;
0 < |palabras| < 10.
'''


from collections import OrderedDict


def checkio(data: list[str]) -> str:
    data = ["".join(OrderedDict.fromkeys(d)) for d in data]
    unique_data = sorted(set("".join(data)))
    ret = ""
    while unique_data:
        for c in unique_data:
            if all(c not in d[1:] for d in data):
                ret += c
                data = [d.replace(c, "") for d in data]
                unique_data.remove(c)
                break
    return ret


print("Example:")
print(checkio(["acb", "bd", "zwa"]))

# These "asserts" are used for self-checking
assert checkio(["acb", "bd", "zwa"]) == "zwacbd"
assert checkio(["klm", "kadl", "lsm"]) == "kadlsm"
assert checkio(["a", "b", "c"]) == "abc"
assert checkio(["aazzss"]) == "azs"
assert checkio(["dfg", "frt", "tyg"]) == "dfrtyg"
assert checkio(["hello", "low", "lino", "itttnosw"]) == "helitnosw"
assert checkio(["my", "name", "myke"]) == "namyke"
assert checkio(["xxxyyz", "yyww", "wwtt", "ttzz"]) == "xywtz"
assert checkio(["axton", "bxton"]) == "abxton"
assert checkio(["is", "not", "abc", "nots", "iabcn"]) == "iabcnots"
assert checkio(["qwerty", "asdfg", "zxcvb", "yagz"]) == "qwertyasdfgzxcvb"

print("The mission is done! Click 'Check Solution' to earn rewards!")
