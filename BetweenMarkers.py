'''
You are given a string and two markers (the initial and final). You have to find a substring enclosed between
these two markers. But there are a few important conditions:

The initial and final markers are always different.
If there is no initial marker, then the first character should be considered the beginning of a string.
If there is no final marker, then the last character should be considered the ending of a string.
If the initial and final markers are missing then simply return the whole string.
If the final marker comes before the initial marker, then return an empty string.
Input: Three arguments. All of them are strings. The second and third arguments are the initial and final markers.

Output: A string.

Example:
assert between_markers("What is >apple<", ">", "<") == "apple"
assert (
    between_markers("<head><title>My new site</title></head>", "<title>", "</title>")
    == "My new site"
)
assert between_markers("No[/b] hi", "[b]", "[/b]") == "No"
assert between_markers("No [b]hi", "[b]", "[/b]") == "hi"

How it is used: for parsing texts

Precondition: can't be more than one final marker and can't be more than one initial. Marker can't be an empty string

----------
----------

Se le da una cadena y dos marcadores (el inicial y el final). Tienes que encontrar una subcadena encerrada entre
estos dos marcadores. Pero hay algunas condiciones importantes:

Los marcadores inicial y final son siempre diferentes.
Si no hay marcador inicial, el primer carácter debe considerarse el principio de la cadena.
Si no hay marcador final, el último carácter debe considerarse el final de la cadena.
Si faltan los marcadores inicial y final, simplemente se devuelve la cadena completa.
Si el marcador final es anterior al marcador inicial, devuelve una cadena vacía.
Entrada: Tres argumentos. Todos ellos son cadenas. El segundo y tercer argumento son los marcadores inicial y final.

Salida: Una cadena.

Ejemplo:
assert between_markers("What is >apple<", ">", "<") == "apple"
assert (
    between_markers("<head><title>My new site</title></head>", "<title>", "</title>")
    == "My new site"
)
assert between_markers("No[/b] hi", "[b]", "[/b]") == "No"
assert between_markers("No [b]hi", "[b]", "[/b]") == "hi"

Cómo se utiliza: para analizar textos

Condición previa: no puede haber más de un marcador final y no puede haber más de un inicial. El marcador no
puede ser una cadena vacía
'''


def between_markers(text: str, begin: str, end: str) -> str:
    """
    returns substring between two given markers
    """
    # your code here
    start_index = text.find(begin)
    if start_index == -1:
        start_index = 0
    else:
        start_index += len(begin)

    end_index = text.find(end)
    if end_index == -1:
        end_index = len(text)

    if end_index < start_index:
        return ''

    return text[start_index:end_index]


print("Example:")
print(between_markers("What is >apple<", ">", "<"))

assert between_markers("What is >apple<", ">", "<") == "apple"
assert (
    between_markers("<head><title>My new site</title></head>", "<title>", "</title>")
    == "My new site"
)
assert between_markers("No[/b] hi", "[b]", "[/b]") == "No"
assert between_markers("No [b]hi", "[b]", "[/b]") == "hi"
assert between_markers("No hi", "[b]", "[/b]") == "No hi"
assert between_markers("No <hi>", ">", "<") == ""

print("The mission is done! Click 'Check Solution' to earn rewards!")
