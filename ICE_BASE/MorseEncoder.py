"""
Your task is to encrypt the text message using the Morse code. The input text will consist
of letters (in uppercase and lowercase), numbers and white spaces. There won't be any special
characters ('&', '?', '#' etc.)
You need to use 3 spaces between words and 1 space between each letter of each word.

Input: The secret message (str).

Output: The same message (str), but encrypted.

Examples:
assert morse_encoder("some text") == "... --- -- .   - . -..- -"
assert (
    morse_encoder("I was born in 1990")
    == "..   .-- .- ...   -... --- .-. -.   .. -.   .---- ----. ----. -----"
)

How it is used: For cryptography and spy work.

Preconditions:
0 < len(text) < 50;
Only English letters (in uppercase and lowercase), numbers and white spaces.

----------
----------

Su tarea consiste en cifrar el mensaje de texto utilizando el código Morse. El texto de
entrada constará de letras (en mayúsculas y minúsculas), números y espacios en blanco.
No habrá caracteres especiales ('&', '?', '#' etc.)
Debe utilizar 3 espacios entre palabras y 1 espacio entre cada letra de cada palabra.

Entrada: El mensaje secreto (str).

Salida: El mismo mensaje (str), pero encriptado.

Ejemplo:
assert codificador_morse("algun texto") == "... --- -- .   - . -..- -"
assert (
    morse_encoder("Nací en 1990")
    == ".. .-- .- ...   -... --- .-. -. .. -. .---- ----. ----. -----"
)

Cómo se utiliza: Para criptografía y labores de espionaje.

Precondiciones:
0 < len(texto) < 50;
Sólo letras inglesas (en mayúsculas y minúsculas), números y espacios en blanco.
"""


MORSE = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}


def morse_encoder(text: str) -> str:
    # your code here
    # Iterate through each character of the input text
    # If the characer (in lowercase) is encoded, encrypt it,
    ## oterwise (i. e. if character is a white space), don't change it.
    # Join the list consisting of encrypted characters and whitespaces
    ## into a string, the characters being separated by " ".
    return " ".join(
        [MORSE[char.lower()] if char.lower() in MORSE else char for char in text]
    )


print("Example:")
print(morse_encoder("some text"))

# These "asserts" are used for self-checking
assert morse_encoder("some text") == "... --- -- .   - . -..- -"
assert (
    morse_encoder("I was born in 1990")
    == "..   .-- .- ...   -... --- .-. -.   .. -.   .---- ----. ----. -----"
)

print("The mission is done! Click 'Check Solution' to earn rewards!")
