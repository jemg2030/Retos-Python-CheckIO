"""
This mission is the part of the set. Another one - Caesar cipher decriptor .

Your mission is to encrypt a secret message (text only, without special chars like "!",
"&", "?" etc.) using Caesar cipher where each letter of input text is replaced by another
that stands at a fixed distance. For example ("a b c", 3) == "d e f"

Input: A secret message as a string (lowercase letters only and white spaces)

Output: The same string, but encrypted

Example:
to_encrypt("a b c", 3) == "d e f"
to_encrypt("a b c", -3) == "x y z"
to_encrypt("simple text", 16) == "iycfbu junj"
to_encrypt("important text", 10) == "swzybdkxd dohd"
to_encrypt("state secret", -13) == "fgngr frperg"

How it is used: For cryptography and to save important information.

Precondition :
0 < len(text) < 50
-26 < delta < 26

----------
----------

Esta misión es la parte del conjunto. Otra - Cifrado César .

Tu misión consiste en cifrar un mensaje secreto (sólo texto, sin caracteres especiales como
"!", "&", "?", etc.) utilizando el cifrado César, en el que cada letra del texto de entrada se
sustituye por otra que se encuentra a una distancia fija. Por ejemplo ("a b c", 3) == "d e f"

Entrada: Un mensaje secreto en forma de cadena (sólo letras minúsculas y espacios en blanco)

Salida: La misma cadena, pero cifrada

Ejemplo
to_encrypt("a b c", 3) == "d e f"
to_encrypt("a b c", -3) == "x y z"
to_encrypt("texto simple", 16) == "iycfbu junj"
to_encrypt("texto importante", 10) == "swzybdkxd dohd"
to_encrypt("secreto de estado", -13) == "fgngr frperg"

Cómo se usa: Para criptografía y para guardar información importante.

Precondición : 0 < len(text) < 50 -26 < delta < 26
"""


def to_encrypt(text, delta):
    # replace this for solution
    encrypted = ""
    for char in text:
        if char == " ":
            encrypted += char
        else:
            char_index = ord(char) - ord("a")
            new_index = (char_index + delta) % 26
            new_char = chr(new_index + ord("a"))
            encrypted += new_char
    return encrypted


if __name__ == "__main__":
    print("Example:")
    print(to_encrypt("abc", 10))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")
