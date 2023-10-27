"""
Lets cow say!
Our cow is young and can only say some of the words we teach it. Not only does it talk, but this
cow can turn into the famous Tux ( wiki/Cowsay ) if we ask it nicely.

You are given some text and your function should format it in the "cows" speech. Let's examine the
rules for this problem:
The cow is always the same, only quote changes.
Multiple spaces in a row are replaced by one space.
The top border consists of underscore characters. It starts from a single space and ends before
the border column.
Each line of the quote consists of these parts: quote border(1), space(1), line(1-39), space(1),
quote border(1).
If line is less than 40 characters, it will fit into one string. The string is quoted in <> .
If the line is greater than or equal to 40 characters, it should be split by these rules:
Max line size is 39 chars. If any spaces are in the line, split it by the rightmost space
(this space is removed from text) otherwise take the first 39 characters.
After the split align all lines to same length by adding spaces at the end of each line.
First line borders: /\
Middle line borders: ||
Last line borders: \/
The bottom border consists of the minus sign. Has same length as top.
cowsay console program has strange behavior in certain cases, this cases will not be tested here.
     _________________________________
    / Dog goes woof                   \
    | Cat goes meow                   |
    | Bird goes tweet                 |
    | And mouse goes squeek           |
    | Cow goes moo                    |
    | Duck goes quack                 |
    \ And the solution will go to you /
     ---------------------------------
            \   ^__^
             \  (oo)\_______
                (__)\       )\/\
                    ||----w |
                    ||     ||

What does the cow say?

Input: Text as a string.

Output: The result for the console as a string.

Hint: Read python docs ( 2.7 , 3.3 ) about formatting styles (str.format and %). Notice for r
before the string. It is a raw string and they use different rules for interpreting backslash
escape sequences.

Example:
cowsay('Checkio rulezz') == r'''
 ________________
< Checkio rulezz >
 ----------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''
cowsay('A longtextwithonlyonespacetofittwolines.') == r'''
 ________________________________________
/ A                                      \
\ longtextwithonlyonespacetofittwolines. /
 ----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

cowsay('Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua.') == r'''
 _________________________________________
/ Lorem ipsum dolor sit amet, consectetur \
| adipisicing elit, sed do eiusmod tempor |
| incididunt ut labore et dolore magna    |
\ aliqua.                                 /
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

How it is used: The original Cowsays are written in the Perl programming language, and as such
are easily adaptable to system tasks in Unix. They can perform functions such as telling users
their home directories are full, that they have new mail, etc. Now you will write your own
realisation for this classic unix program. This concept can teach you how to prepare and format
text for the console output.

Precondition: 0 < len(text) < 858;
text can't consist of spaces only;
text contains only ASCII letters, digits and punctuation.

----------
----------

¡Que diga la vaca!
Nuestra vaca es joven y sólo sabe decir algunas de las palabras que le enseñamos. No sólo habla,
sino que esta vaca puede convertirse en el famoso Tux ( wiki/Cowsay ) si se lo pedimos amablemente.

Se te da un texto y tu función debe formatearlo en el habla de la "vaca". Examinemos las reglas
de este problema:
La vaca es siempre la misma, sólo cambian las comillas.
Los espacios seguidos se sustituyen por un espacio.
El borde superior está formado por caracteres de subrayado. Empieza con un solo espacio y termina
antes de la columna del borde.
Cada línea de la cita consta de estas partes: cita borde(1), espacio(1), línea(1-39), espacio(1),
cita borde(1).
Si la línea tiene menos de 40 caracteres, cabe en una sola cadena. La cadena se entrecomilla en <> .
Si la línea es mayor o igual a 40 caracteres, debe dividirse mediante estas reglas:
El tamaño máximo de la línea es de 39 caracteres. Si hay espacios en la línea, divídala por el
espacio más a la derecha (este espacio se elimina del texto), de lo contrario tome los primeros
39 caracteres.
Después de la división alinee todas las líneas a la misma longitud añadiendo espacios al final de
cada línea.
Bordes de la primera línea: /\
Bordes de la línea central: ||
Bordes de la última línea: \/
El borde inferior está formado por el signo menos. Tiene la misma longitud que el superior.
El programa de consola cowsay tiene un comportamiento extraño en ciertos casos, estos casos no serán
probados aquí.

     _________________________________
    / Dog goes woof                   \
    | Cat goes meow                   |
    | Bird goes tweet                 |
    | And mouse goes squeek           |
    | Cow goes moo                    |
    | Duck goes quack                 |
    \ And the solution will go to you /
     ---------------------------------
            \   ^__^
             \  (oo)\_______
                (__)\       )\/\
                    ||----w |
                    ||     ||

¿Qué dice la vaca?

Entrada: Texto en forma de cadena.

Salida: El resultado para la consola como cadena.

Sugerencia: Lea los documentos de python ( 2.7 , 3.3 ) sobre estilos de formato (str.format y %).
 Nota para r antes de la cadena. Es una cadena cruda y utilizan diferentes reglas para interpretar
 las secuencias de escape de barra invertida.

Ejemplo:
cowsay('Checkio rulezz') == r'''
 ________________
< Checkio rulezz >
 ----------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''
cowsay('A longtextwithonlyonespacetofittwolines.') == r'''
 ________________________________________
/ A                                      \
\ longtextwithonlyonespacetofittwolines. /
 ----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

cowsay('Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.') == r'''
 _________________________________________
/ Lorem ipsum dolor sit amet, consectetur \
| adipisicing elit, sed do eiusmod tempor |
| incididunt ut labore et dolore magna    |
\ aliqua.                                 /
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

Cómo se utiliza: Los Cowsays originales están escritos en el lenguaje de programación Perl,
y como tales son fácilmente adaptables a tareas del sistema en Unix. Pueden realizar funciones
como indicar a los usuarios que sus directorios personales están llenos, que tienen correo
nuevo, etc. Ahora escribirás tu propia realización para este programa clásico de Unix. Este
concepto puede enseñarte a preparar y formatear texto para la salida de la consola.

Precondición: 0 < len(texto) < 858; el texto no puede consistir sólo de espacios; el texto
contiene sólo letras ASCII, dígitos y puntuación.
"""

COW = r"""
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
"""

MAXCHAR = 39


def cowsay(text):
    # replace multiple spaces
    while "  " in text:
        text = text.replace("  ", " ")

    # make lines
    lines = []
    line = ""
    for word in text.split(" "):
        if len(word) > MAXCHAR:  # we need divide the word
            if line:  # flush line
                lines.append(line[:-1])
                line = ""
            while len(word) > MAXCHAR:  # divide the word and append it
                lines.append(word[:MAXCHAR])
                word = word[MAXCHAR:]
            if word:  # the rest of the word
                line += word + " "  # append the rest of the word
        else:  # no divide case
            if len(line) + len(word) > MAXCHAR:  # flush line
                lines.append(line[:-1])
                line = ""
            line += word + " "  # append the word
    if line:
        lines.append(line[:-1])  # flush line

    # format output
    n = len(lines)
    maxlen = max(len(line) for line in lines)
    s = "\n {}\n".format("_" * (maxlen + 2))
    for i in range(n):
        border = ["||", "\\/", "/\\", "<>"][(2 * (i == 0) + (i == n - 1))]
        s += "{} {:{}} {}\n".format(border[0], lines[i], maxlen, border[1])
    return s + " {}{}".format("-" * (maxlen + 2), COW)


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    expected_cowsay_one_line = r"""
 ________________
< Checkio rulezz >
 ----------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
"""
    expected_cowsay_two_lines = r"""
 ________________________________________
/ A                                      \
\ longtextwithonlyonespacetofittwolines. /
 ----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
"""

    expected_cowsay_many_lines = r"""
 _________________________________________
/ Lorem ipsum dolor sit amet, consectetur \
| adipisicing elit, sed do eiusmod tempor |
| incididunt ut labore et dolore magna    |
\ aliqua.                                 /
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
"""

    cowsay_one_line = cowsay("Checkio rulezz")
    assert cowsay_one_line == expected_cowsay_one_line, (
        "Wrong answer:\n%s" % cowsay_one_line
    )

    cowsay_two_lines = cowsay("A longtextwithonlyonespacetofittwolines.")
    assert cowsay_two_lines == expected_cowsay_two_lines, (
        "Wrong answer:\n%s" % cowsay_two_lines
    )

    cowsay_many_lines = cowsay(
        "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do "
        "eiusmod tempor incididunt ut labore et dolore magna aliqua."
    )
    assert cowsay_many_lines == expected_cowsay_many_lines, (
        "Wrong answer:\n%s" % cowsay_many_lines
    )
