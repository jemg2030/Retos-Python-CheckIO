'''
This is the first in a series of missions inspired by classical cryptography. In this mission we
will take a look at the Atbash cipher.

Atbash is one of the oldest known ciphers, created in Middle East around 600 B.C.; the first known
examples of it can be found in the Dead Sea Scrolls (ancient religious Hebrew manuscripts), where
it was used to encrypt certain important names and words.

Atbash is an example of a simple substitution cipher. In this type of ciphers each letter of the
message (or plaintext ) is mapped to a single correspinding letter of the ciphertext. in case of
Atbash the plaintext alphabet is simply mapped to it's reverse, so that the first letter is
replaced with the last, the second letter - with the second to last and so on. For example, the
message "Hello, world!" is enciphered to "Swool, dliow!". The substitution table (for Latin alphabet)
looks like this:

    Plaintext alphabet:  abcdefghijklmnopqrstuvwxyz
    Ciphertext alphabet: zyxwvutsrqponmlkjihgfedcba
To decrypt a message, the same algorithm is applied to the ciphertext.

It's easy to see that Atbash provides virtually no information security. Anyone who intercepts
the message encrypted with the Atbash cipher can easily decipher it by applying the same substitution table.

For this mission you need to write a function that encrypts given text with Atbash. Punctuation,
whitespaces and other characters should remain unchanged.

Input: plaintext: str

Output: ciphertext: str

Example:
atbash('testing') == 'gvhgrmt'
atbash('Hello, world!') == 'Svool, dliow!'

----------
----------

Esta es la primera de una serie de misiones inspiradas en la criptografía clásica. En esta misión
analizaremos el cifrado Atbash.

Atbash es uno de los cifrados más antiguos que se conocen, creado en Oriente Próximo alrededor del
año 600 a.C.; los primeros ejemplos conocidos se encuentran en los Rollos del Mar Muerto (antiguos
manuscritos religiosos hebreos), donde se utilizaba para cifrar ciertos nombres y palabras importantes.

Atbash es un ejemplo de cifrado por sustitución simple. En este tipo de cifrado, cada letra del mensaje
(o texto plano) se asigna a una única letra correspondiente del texto cifrado. En el caso de Atbash, el
alfabeto del texto plano simplemente se asigna a su inverso, de modo que la primera letra se sustituye
por la última, la segunda por la penúltima y así sucesivamente. Por ejemplo, el mensaje "¡Hola, mundo!"
se cifra en "¡Swool, dliow!". La tabla de sustitución (para el alfabeto latino) tiene el siguiente aspecto:

    Alfabeto del texto sin cifrar: abcdefghijklmnopqrstuvwxyz
    Alfabeto del texto cifrado: zyxwvutsrqponmlkjihgfedcba
Para desencriptar un mensaje, se aplica el mismo algoritmo al texto cifrado.

Es fácil ver que Atbash no proporciona prácticamente ninguna seguridad de la información. Cualquiera
que intercepte el mensaje cifrado con el cifrado Atbash puede descifrarlo fácilmente aplicando la misma
tabla de sustitución.

Para esta misión necesitas escribir una función que cifre un texto dado con Atbash. La puntuación, los
espacios en blanco y otros caracteres deben permanecer inalterados.

Entrada: texto plano: str

Salida: texto cifrado: str

Ejemplo:
atbash('testing') == 'gvhgrmt'
atbash('¡Hola, mundo!') == 'Svool, dliow!'
'''


def atbash(plaintext: str) -> str:
    # your code here
    plain_alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher_alphabet = "zyxwvutsrqponmlkjihgfedcba"
    result = ""
    for char in plaintext:
        if char.lower() in plain_alphabet:
            cipher_char = cipher_alphabet[plain_alphabet.index(char.lower())]
            if char.isupper():
                cipher_char = cipher_char.upper()
            result += cipher_char
        else:
            result += char
    return result


if __name__ == "__main__":
    print("Example:\nplaintext: testing")
    print(atbash("testing"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert atbash("testing") == "gvhgrmt"
    assert atbash("attack at dawn") == "zggzxp zg wzdm"
    assert atbash("Hello, world!") == "Svool, dliow!"

    print("Coding complete? Click 'Check' to earn cool rewards!")
