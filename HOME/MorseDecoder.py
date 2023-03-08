'''
Your task is to decrypt the secret message using the Morse code .
The message will consist of words with 3 spaces between them and 1 space between each letter of each word.
If the decrypted text starts with a letter then you'll have to print this letter in uppercase.

Input: The secret message (string).

Output: The decrypted text (string).

Example:
assert morse_decoder("... --- -- .   - . -..- -") == "Some text"
assert (
    morse_decoder("..   .-- .- ...   -... --- .-. -.   .. -.   .---- ----. ----. -----")
    == "I was born in 1990"
)

How it is used: For cryptography and spy work.

Precondition :
0 < len(message) < 100
The message will consists of numbers and English letters only.

---------
---------

Su tarea consiste en descifrar el mensaje secreto utilizando el código Morse .
El mensaje consistirá en palabras con 3 espacios entre ellas y 1 espacio entre cada letra de cada palabra.
Si el texto descifrado empieza por una letra, tendrás que escribir esta letra en mayúscula.

Entrada: El mensaje secreto (cadena).

Salida: El texto descifrado (cadena).

Ejemplo:
assert morse_decoder("... --- -- . - . -..-") == "Algún texto"
assert (
    morse_decoder(".. .-- .- ... -.. --- .-. -. .. -. .---- ----. ----. -----")
    == "Nací en 1990"
)

Cómo se utiliza: Para criptografía y labores de espionaje.

Precondición :
0 < len(mensaje) < 100
El mensaje constará únicamente de números y letras inglesas.

Traducción realizada con la versión gratuita del traductor www.DeepL.com/Translator
'''


MORSE = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
}


def morse_decoder(code: str) -> str:
    # replace this for solution
    words = code.split("   ")
    # Decode each word and concatenate them
    decoded_words = []
    for word in words:
        decoded_word = ""
        # Split the word into letters
        letters = word.split(" ")
        # Decode each letter and concatenate them
        for letter in letters:
            decoded_word += MORSE[letter]
        decoded_words.append(decoded_word)
    # Capitalize the first letter of the first word
    if len(decoded_words) > 0:
        first_word = decoded_words[0]
        decoded_words[0] = first_word[0].upper() + first_word[1:]
    # Concatenate the decoded words with spaces between them
    decoded_message = " ".join(decoded_words)
    return decoded_message


print("Example:")
print(morse_decoder("... --- -- .   - . -..- -"))

assert morse_decoder("... --- -- .   - . -..- -") == "Some text"
assert (
    morse_decoder("..   .-- .- ...   -... --- .-. -.   .. -.   .---- ----. ----. -----")
    == "I was born in 1990"
)

print("The mission is done! Click 'Check Solution' to earn rewards!")
