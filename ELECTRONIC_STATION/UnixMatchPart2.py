"""
Sometimes you find yourself in a situation when, among a huge number of files on
your computer or in a separate folder, you need to find files of a certain type.
For example, images with the extension '.jpg' or documents with the extension '.txt',
or even files that have the word 'butterfly' in their name. Doing this manually can be
time-consuming. 'Matching' or patterns for searching files by a specific mask are just
what you need for these sort of challenges.
This mission will help you understand how this works.

You need to find out if the given unix pattern matches the given filename.

Here is a small table that shows symbols that can be used in patterns.

[seq]	matches any character in seq, for example [123] means any character - '1', '2' or '3'
[!seq]	matches any character not in seq, for example [!123] means any character except '1', '2' and '3'
[]	seq without any chars will never match
Note that the expression in one pair of square brackets responds only for 1 character. So:

unix_match('0123', '[!abc]123') == True
# but
unix_match('00123', '[!abc]123') == False

Input: Two arguments. Both are strings.

Output: Bool.

Examples:
assert unix_match("log1.txt", "log[1234567890].txt") == True
assert unix_match("log1.txt", "log[!1].txt") == False

How it is used: in the unix-shell.

Precondition: 0 < len(strings) < 100

----------
----------

A veces se encuentra en una situación en la que, entre un gran número de archivos en su
ordenador o en una carpeta separada, necesita encontrar archivos de un determinado tipo.
Por ejemplo, imágenes con la extensión '.jpg' o documentos con la extensión '.txt', o
incluso archivos que tienen la palabra 'mariposa' en su nombre. Hacer esto manualmente
puede llevar mucho tiempo. Las 'coincidencias' o patrones para buscar archivos por una
máscara específica son justo lo que necesitas para este tipo de retos.
Esta misión te ayudará a entender cómo funciona.

Tienes que averiguar si el patrón unix dado coincide con el nombre de archivo dado.

Aquí hay una pequeña tabla que muestra los símbolos que se pueden utilizar en los patrones.

[seq] coincide con cualquier caracter en seq, por ejemplo [123] significa cualquier caracter - '1', '2' o '3
[!seq] coincide con cualquier carácter que no esté en seq, por ejemplo [!123] significa cualquier
carácter excepto '1', '2' y '3
[] seq sin ningún carácter nunca coincidirá
Tenga en cuenta que la expresión entre un par de corchetes sólo responde para 1 carácter. Por ejemplo

unix_match('0123', '[!abc]123') == True
# pero
unix_match('00123', '[!abc]123') == Falso

Entrada: Dos argumentos. Ambos son cadenas.

Salida: Bool.

Ejemplo:
assert unix_match("log1.txt", "log[1234567890].txt") == True
assert unix_match("log1.txt", "log[!1].txt") == False

Cómo se utiliza: en el unix-shell.

Precondición: 0 < len(cadenas) < 100
"""


import re


def unix_match(filename: str, pattern: str) -> bool:
    # your code here
    pattern = (
        pattern.replace("*", "\\*")
        .replace(".", "\\.")
        .replace("[!", "[^")
        .replace("[]", "[^.]")
        .replace("[^]", "\[!\]")
    )
    return re.match(pattern, filename) != None


print("Example:")
print(unix_match("log1.txt", "log[1234567890].txt"))

# These "asserts" are used for self-checking
assert unix_match("log1.txt", "log[1234567890].txt") == True
assert unix_match("log1.txt", "log[!1].txt") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
