'''
For the input of your function, you will be given one sentence. You have to return a corrected version,
that starts with a capital letter and ends with a period (dot).

Pay attention to the fact that not all of the fixes are necessary. If a sentence already ends with
a period (dot), then adding another one will be a mistake.

Input: A string.

Output: A string.

Example:
assert correct_sentence("greetings, friends") == "Greetings, friends."
assert correct_sentence("Greetings, friends") == "Greetings, friends."
assert correct_sentence("Greetings, friends.") == "Greetings, friends."
assert correct_sentence("greetings, friends.") == "Greetings, friends."

Precondition: No leading and trailing spaces, text contains only spaces, a-z A-Z , and ".".

----------
----------

Para la entrada de su función, se le dará una frase. Tiene que devolver una versión corregida, que
empiece por mayúscula y termine por punto.

Tenga en cuenta que no todas las correcciones son necesarias. Si una frase ya termina con un punto,
añadir otro sería un error.

Entrada: Una cadena.

Salida: Una cadena.

Ejemplo:
assert frase_correcta("saludos, amigos") == "Saludos, amigos."
assert correct_sentence("Saludos, amigos") == "Saludos, amigos".
assert correct_sentence("Saludos, amigos") == "Saludos, amigos".
assert correct_sentence("Saludos, amigos.") == "Saludos, amigos."

Condición previa: Sin espacios iniciales ni finales, el texto sólo contiene espacios, a-z A-Z , y ".".

Traducción realizada con la versión gratuita del traductor www.DeepL.com/Translator
'''


def correct_sentence(text: str) -> str:
    # your code here
    text = text.strip()  # Remove leading and trailing spaces
    if not text.endswith('.'):
        text += '.'  # Add period at the end if it's not already there
    text = text[0].upper() + text[1:]  # Capitalize the first letter
    return text


print("Example:")
print(correct_sentence("greetings, friends"))

# These "asserts" are used for self-checking
assert correct_sentence("greetings, friends") == "Greetings, friends."
assert correct_sentence("Greetings, friends") == "Greetings, friends."
assert correct_sentence("Greetings, friends.") == "Greetings, friends."
assert correct_sentence("greetings, friends.") == "Greetings, friends."

print("The mission is done! Click 'Check Solution' to earn rewards!")
