'''
You are given a long line (a monospace font), and you have to break the line in order to respect a
given width. Then you have to format the text according to the given style: 'l' means you have to
align the text to the left, 'c' for center, 'r' for right, and 'j' means you have to justify the
text. Finally, the lines of the output shouldn’t end with a whitespace.

If you have to put 2 * n + 1 spaces around a line in order to center it, then put n spaces before, not n + 1.

The justification rules:
Since we can't always put the same number of spaces between words in a line, put big blocks of spaces first.
For example: X---X---X--X--X--X when you have to put 12 spaces in 5 gaps: 3-3-2-2-2.
Don't justify the last line of a text.
You won't have to consider splitting a word into two parts because the given widths are big enough.

Input: A text (string), width (integer) and style (string).

Output: The formatted text (string).

Examples:
text = "Hi, my name is Alex and I am 18 years old."

text_formatting(text, 20, 'l') == \
"""Hi, my name is Alex
and I am 18 years
old."""

text_formatting(text, 20, 'c') == \
"""Hi, my name is Alex
 and I am 18 years
        old."""

text_formatting(text, 20, 'r') == \
""" Hi, my name is Alex
   and I am 18 years
                old."""

text_formatting(text, 20, 'j') == \
"""Hi,  my name is Alex
and  I  am  18 years
old."""

Preconditions:
all(len(word) <= width for word in text.split())
'\n' not in text
style in ('l', 'c', 'r', 'j')
0 < len(text) <= 1000

----------
----------

Se te da una línea larga (una fuente monoespaciada), y tienes que romper la línea para respetar una
anchura dada. A continuación, tienes que formatear el texto de acuerdo con el estilo dado: 'l'
significa que tienes que alinear el texto a la izquierda, 'c' para el centro, 'r' para la derecha, y
'j' significa que tienes que justificar el texto. Por último, las líneas de la salida no deben terminar
con un espacio en blanco.

Si tienes que poner 2 * n + 1 espacios alrededor de una línea para centrarla, entonces pon n espacios
antes, no n + 1.

Las reglas de justificación:
Como no siempre podemos poner el mismo número de espacios entre las palabras de una línea, pon grandes
bloques de espacios antes. Por ejemplo: X---X---X--X--X--X cuando hay que poner 12 espacios en 5 espacios:
3-3-2-2-2.
No justifiques la última línea de un texto.
No tendrás que considerar dividir una palabra en dos partes porque los anchos dados son suficientemente
grandes.

Entrada: Un texto (cadena), anchura (entero) y estilo (cadena).

Salida: El texto formateado (cadena).

Ejemplos:
text = "Hola, me llamo Alex y tengo 18 años".

text_formatting(text, 20, 'l') == \
"""Hola, me llamo Alex
y tengo 18 años
años.""

text_formatting(text, 20, 'c') == \
"""Hola, me llamo Alex
 y tengo 18 años
        años.""

text_formatting(text, 20, 'r') == \
""" Hola, me llamo Alex
   y tengo 18 años
                años.""

text_formatting(text, 20, 'j') == \
"""Hola, me llamo Alex
y tengo 18 años
años.""

Precondiciones:
all(len(word) <= width for word in text.split())
\n' no en texto
style in ('l', 'c', 'r', 'j')
0 < len(texto) <= 1000
'''


def text_formatting(text: str, width: int, style: str) -> str:
    def make_row(text):
        rest = text.split()
        row = []
        while rest:
            word = rest.pop(0)
            if len(' '.join(row + [word])) > width:
                yield ' '.join(row), False
                row.clear()
            row.append(word)
        yield ' '.join(row), True

    def justify(row, width):
        q, r = divmod(width-len(row), row.count(' '))
        return ''.join(' '*(1+q+(i <= r))*(i > 0)+w for i, w in enumerate(row.split(' ')))

    result = []
    fn = {'r': str.rjust, 'l': str.ljust, 'c': str.center, 'j': justify}

    for row, last in make_row(text):
        if style == 'j' and last:
            style = 'l'
        result.append(fn[style](row, width).rstrip())

    return '\n'.join(result)


if __name__ == "__main__":
    LINE = (
        "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure "
        "harum suscipit aperiam aliquam ad, perferendis ex molestias "
        "reiciendis accusantium quos, tempore sunt quod veniam, eveniet "
        "et necessitatibus mollitia. Quasi, culpa."
    )

    print("Example:")
    print(text_formatting(LINE, 38, "l"))

    assert (
        text_formatting(LINE, 38, "l")
        == """Lorem ipsum dolor sit amet,
consectetur adipisicing elit. Iure
harum suscipit aperiam aliquam ad,
perferendis ex molestias reiciendis
accusantium quos, tempore sunt quod
veniam, eveniet et necessitatibus
mollitia. Quasi, culpa."""
    ), "Left 38"

    assert (
        text_formatting(LINE, 30, "c")
        == """ Lorem ipsum dolor sit amet,
consectetur adipisicing elit.
 Iure harum suscipit aperiam
  aliquam ad, perferendis ex
     molestias reiciendis
accusantium quos, tempore sunt
   quod veniam, eveniet et
   necessitatibus mollitia.
        Quasi, culpa."""
    ), "Center 30"

    assert (
        text_formatting(LINE, 50, "r")
        == """           Lorem ipsum dolor sit amet, consectetur
     adipisicing elit. Iure harum suscipit aperiam
   aliquam ad, perferendis ex molestias reiciendis
       accusantium quos, tempore sunt quod veniam,
 eveniet et necessitatibus mollitia. Quasi, culpa."""
    ), "Right 50"

    assert (
        text_formatting(LINE, 45, "j")
        == """Lorem   ipsum  dolor  sit  amet,  consectetur
adipisicing elit. Iure harum suscipit aperiam
aliquam    ad,   perferendis   ex   molestias
reiciendis  accusantium  quos,  tempore  sunt
quod   veniam,   eveniet   et  necessitatibus
mollitia. Quasi, culpa."""
    ), "Justify 45"
