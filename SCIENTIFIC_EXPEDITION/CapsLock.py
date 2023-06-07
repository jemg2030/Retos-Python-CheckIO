'''
Joe Palooka has fat fingers, so he always hits the “Caps Lock” key whenever he actually intends
to hit the key “a” by itself. (When Joe tries to type in some accented version of “a” that needs
more keystrokes to conjure the accents, he is more careful in the presence of such raffinated
characters ([Shift] + [Char]) and will press the keys correctly.) Compute and return the result
of having Joe type in the given text. The “Caps Lock” key affects only the letter keys from “a”
to “z” , and has no effect on the other keys or characters. “Caps Lock” key is assumed to be
initially off.

For Joe's keyboard, Caps Lock is always uppercase a letter. That means if Caps Lock is on, and
Joe does Shift + b - he gets 'B' (in upper case) printed.

Input: A string. The typed text.

Output: A string. The showed text after being typed.

Example:
caps_lock("Why are you asking me that?") == "Why RE YOU sking me thT?"
caps_lock("Madder than Mad Brian of Madcastle") == "MDDER THn MD BRIn of MDCstle"
caps_lock("Aloha from Hawaii") == "Aloh FROM HwII"

The mission was taken from Python CCPS 109 Fall 2018. It is taught for Ryerson Chang School of
Continuing Education by Ilkka Kokkarinen

----------
----------

Joe Palooka tiene los dedos gordos, así que siempre pulsa la tecla "Bloq Mayús" cuando
quiere pulsar la tecla "a" sola. (Cuando Joe intenta teclear alguna versión acentuada
de "a" que necesita más pulsaciones para conjurar los acentos, es más cuidadoso en
presencia de tales caracteres rafinados ([Shift] + [Char]) y estará pulsando las teclas
correctamente). Calcula y devuelve el resultado de hacer que Joe teclee el texto dado.
La tecla "Bloq Mayús" afecta sólo a las teclas de letras de la "a" a la "z" , y no tiene
ningún efecto sobre las demás teclas o caracteres. Se supone que la tecla "Bloq Mayús"
está inicialmente desactivada.

Para el teclado de Joe, "Caps Lock" siempre pone en mayúscula una letra. Eso significa que
si Bloq Mayús está activada, y Joe hace Mayús + b - obtiene "B" (en mayúsculas) impresa.

Entrada: Una cadena. El texto escrito.

Salida: Una cadena. El texto mostrado después de ser tecleado.

Ejemplo:
caps_lock("¿Por qué me preguntas eso?") == "¿Por qué me preguntas eso?"
caps_lock("Más Loco que el Loco Brian de Madcastle") == "MÁS Loco que el Loco Brian de MDCstle"
caps_lock("Aloha desde Hawai") == "Aloh DESDE HwII"

La misión fue tomada de Python CCPS 109 Otoño 2018. Es impartida para la escuela de educación
continua Ryerson Chang por Ilkka Kokkarinen
'''


def caps_lock(text: str) -> str:
    # your code here
    caps, result = False, []
    for c in text:
        if c == 'a':
            caps = not caps
        else:
            result.append(c.upper() if caps else c)
    return "".join(result)


if __name__ == "__main__":
    print("Example:")
    print(caps_lock("Why are you asking me that?"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert caps_lock("Why are you asking me that?") == "Why RE YOU sking me thT?"
    assert caps_lock("Always wanted to visit Zambia.") == "AlwYS Wnted to visit ZMBI."
    assert caps_lock("Aloha from Hawaii") == "Aloh FROM HwII"
    print("Coding complete? Click 'Check' to earn cool rewards!")
