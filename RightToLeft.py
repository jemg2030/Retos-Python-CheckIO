'''
"For centuries, left-handers have suffered unfair discrimination in a world designed for right-handers."
Santrock, John W. (2008). Motor, Sensory, and Perceptual Development.

"Most humans (say 70 percent to 95 percent) are right-handed, a minority (say 5 percent to 30 percent) are
left-handed, and an indeterminate number of people are probably best described as ambidextrous."
Scientific American. www.scientificamerican.com

One of the robots is charged with a simple task: to join a sequence of strings into one sentence to produce
instructions on how to get around the ship. But this robot is left-handed and has a tendency to joke around
and confuse its right-handed friends.

You are given a sequence of strings. You should join these strings into a chunk of text where the initial
strings are separated by commas. As a joke on the right handed robots, you should replace all cases of the
words "right" with the word "left", even if it's a part of another word. All strings are given in lowercase.

Input: A sequence of strings.

Output: The text as a comma-separated string.

Example:

assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
assert left_join(("bright aright", "ok")) == "bleft aleft,ok"
assert left_join(("brightness wright",)) == "bleftness wleft"
assert left_join(("enough", "jokes")) == "enough,jokes"

How it is used: This is a simple example of operations using strings and sequences.

Precondition:
0 < len(phrases) < 42

----------
----------

"Durante siglo, los zurdos han sufrido una discriminación injusta en un mundo diseñado para diestros."
Santrock, John W. (2008). Desarrollador Motor, Sensorial, y Perceptual.

"La mayoría de los humanos (entre el 70 y el 95 por ciento) son diestros, una minoría (entre el 5 y el 30
por ciento) son zurdos, y un número intermedio de personas son, probablemente, mejor definidos como ambidiestros."
Scientific American. www.scientificamerican.com

A uno de los robots se le ha asignado la tarea sencilla de unir una secuencia de palabras en una frase para
generar las instrucciones de cómo moverse por la nave. Pero este robot es zurdo y tiene la tendencia de bromear
y confundir a sus amigos diestros.

Se da una secuencia de palabras. Debes unir estas palabras en una cadena de texto donde las palabras están
separadas por comas. Debido a las bromas gastadas a los robots diestros, debes reemplazar todas las ocurrencias
de la palabra "right" (derecha) por la palabra "left" (izquierda), incluso si esta forma parte de otra palabra.
Todas las cadenas de texto son dadas en minúscula.

Entrada: Una secuencia de palabras en forma.

Salida: El texto como cadena de texto.

Ejemplo:

assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
assert left_join(("bright aright", "ok")) == "bleft aleft,ok"
assert left_join(("brightness wright",)) == "bleftness wleft"
assert left_join(("enough", "jokes")) == "enough,jokes"

Cómo se usa: Este es un ejemplo sencillo de operaciones usando cadenas de texto y secuencias:

Precondición:
0 < len(phrases) < 42
'''


def left_join(phrases: tuple[str]) -> str:
    # your code here
    # replace all occurrences of 'right' with 'left'
        return ",".join([phrase.replace("right", "left") for phrase in phrases])

print("Example:")
print(left_join(("left", "right", "left", "stop")))

# These "asserts" are used for self-checking
assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
assert left_join(("bright aright", "ok")) == "bleft aleft,ok"
assert left_join(("brightness wright",)) == "bleftness wleft"
assert left_join(("enough", "jokes")) == "enough,jokes"

print("The mission is done! Click 'Check Solution' to earn rewards!")
