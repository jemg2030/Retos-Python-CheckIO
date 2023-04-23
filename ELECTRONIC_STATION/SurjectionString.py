'''
Maybe it's a cipher? Maybe, but we don’t know for sure.

Maybe you can call it "homomorphism"? I wish I knew this word before.

You need to check that the String A is isometric to the String B. There exists a function that turns
characters from String A into characters in the same spot in String B.

Characters in String A correspond to a unique character value in String B. Characters in String B are
allowed to correspond to multiple character values in String A.

Input: Two arguments. String A and String B.

Output: Boolean.

Examples:
assert isometric_strings("add", "egg") == True
assert isometric_strings("foo", "bar") == False
assert isometric_strings("bar", "foo") == True
assert isometric_strings("", "") == True

Precondition:
both strings are the same length.

----------
----------

¿Tal vez es una cifra? Tal vez, pero no lo sabemos con seguridad.

¿Quizás puedas llamarlo "homomorfismo"? Desearía haber conocido esta palabra antes.

Tienes que registrar que la Cadena A es isométrica a la Cadena B. Existe una función que convierte
caracteres de la Cadena A en caracteres en el mismo lugar en la Cadena B.

Los caracteres de la cadena A corresponden a un único valor de carácter en la cadena B. Se permite
que los caracteres de la cadena B correspondan a múltiples valores de carácter en la cadena A.

Entrada: Dos argumentos. Cadena A y Cadena B.

Salida: Booleano.

Ejemplo:
assert isometric_strings("add", "egg") == True
assert isometric_strings("foo", "bar") == False
assert isometric_strings("bar", "foo") == True
assert isometric_strings("", "") == True

Precondición:
ambas cadenas tienen la misma longitud.
'''


def isometric_strings(a: str, b: str) -> bool:
    # your code here
    cipher = {}
    for i, c in enumerate(a):
        if c not in cipher:
            cipher[c] = b[i]
        elif cipher[c] != b[i]:
            return False

    return True


print("Example:")
print(isometric_strings("add", "egg"))

# These "asserts" are used for self-checking
assert isometric_strings("add", "egg") == True
assert isometric_strings("foo", "bar") == False
assert isometric_strings("bar", "foo") == True
assert isometric_strings("", "") == True
assert isometric_strings("all", "all") == True
assert isometric_strings("gogopy", "doodle") == False
assert isometric_strings("abba", "cccc") == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
