'''
You are given a string and two markers (the initial one and final). You have to find a substring enclosed
between these two markers. But there are a few important conditions.

The initial and final markers are always different.
The initial and final markers are always 1 char size.
The initial and final markers always exist in a string and go one after another.
Input: Three arguments. All of them are strings. The second and third arguments are the initial and final markers.

Output: A string.

Example:
assert between_markers("What is >apple<", ">", "<") == "apple"
assert between_markers("What is [apple]", "[", "]") == "apple"
assert between_markers("What is ><", ">", "<") == ""
assert between_markers("[an apple]", "[", "]") == "an apple"

How it is used: For text parsing.

Precondition: There can't be more than one final and one initial markers.

----------
----------

Se le da una cadena y dos marcadores (el inicial y el final). Tienes que encontrar una subcadena e
ncerrada entre estos dos marcadores. Pero hay algunas condiciones importantes.

Los marcadores inicial y final son siempre diferentes.
Los marcadores inicial y final tienen siempre un tamaño de 1 carácter.
Los marcadores inicial y final siempre existen en una cadena y van uno detrás de otro.
Entrada: Tres argumentos. Todos ellos son cadenas. El segundo y tercer argumento son los marcadores inicial y final.

Salida: Una cadena.

Ejemplo:
assert entre_marcadores("Qué es >manzana<", ">", "<") == "manzana"
assert between_markers("¿Qué es [manzana]", "[", "]") == "manzana"
assert between_markers("Qué es ><", ">", "<") == ""
assert between_markers("[una manzana]", "[", "]") == "una manzana"

Cómo se utiliza: Para analizar texto.

Condición previa: No puede haber más de un marcador final y uno inicial.

Traducción realizada con la versión gratuita del traductor www.DeepL.com/Translator
'''


def between_markers(text: str, start: str, end: str) -> str:
    # your code here
    marker1 = text.find(start) + 1
    marker2 = text.find(end)
    if marker1 == -1 or marker2 == -1 or marker1 >= marker2:
        return ""
    else:
        return text[marker1:marker2]


print("Example:")
print(between_markers("What is >apple<", ">", "<"))

# These "asserts" are used for self-checking
assert between_markers("What is >apple<", ">", "<") == "apple"
assert between_markers("What is [apple]", "[", "]") == "apple"
assert between_markers("What is ><", ">", "<") == ""
assert between_markers("[an apple]", "[", "]") == "an apple"

print("The mission is done! Click 'Check Solution' to earn rewards!")
