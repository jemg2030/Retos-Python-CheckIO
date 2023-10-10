"""
Sometimes you find yourself in a situation when, among a huge number of files on your computer
or in a separate folder, you need to find files of a certain type. For example, images with the
extension '.jpg' or documents with the extension '.txt', or even files that have the word
'butterfly' in their name. Doing this manually can be time-consuming. 'Matching' or patterns
for searching files by a specific mask are just what you need for these sort of challenges.
This mission will help you understand how this works.

You need to find out if the given unix pattern matches the given filename.

Let me show you what I mean by matching the filenames in the unix-shell. For example, * matches
everything and *.txt matches all of the files that have txt extension. Here is a small table that
shows symbols that can be used in patterns.

*	matches everything
?	matches any single character
Input: Two arguments. Both are strings.

Output: Bool.

Examples:
assert unix_match("somefile.txt", "*") == True
assert unix_match("other.exe", "*") == True
assert unix_match("my.exe", "*.txt") == False
assert unix_match("log1.txt", "log?.txt") == True

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

Permíteme mostrarte a qué me refiero cuando digo que los nombres de archivo coinciden en
el shell unix. Por ejemplo, * coincide con todo y *.txt coincide con todos los archivos
que tienen extensión txt. Aquí hay una pequeña tabla que muestra los símbolos que se pueden
utilizar en los patrones.

* coincide con todo
? coincide con cualquier carácter
Entrada: Dos argumentos. Ambos son cadenas.

Salida: Bool.

Ejemplo:
assert unix_match("algunarchivo.txt", "*") == True
assert unix_match("otro.exe", "*") == True
assert unix_match("mi.exe", "*.txt") == False
assert unix_match("log1.txt", "log?.txt") == True

Cómo se usa: en el unix-shell.

Precondición: 0 < len(cadenas) < 100
"""


import re


def unix_match(filename: str, pattern: str) -> bool:
    # your code here
    return (
        re.match(
            pattern.replace(".", "\.").replace("*", ".*").replace("?", ".{1}"), filename
        )
        is not None
    )


print("Example:")
print(unix_match("somefile.txt", "*"))

# These "asserts" are used for self-checking
assert unix_match("somefile.txt", "*") == True
assert unix_match("other.exe", "*") == True
assert unix_match("my.exe", "*.txt") == False
assert unix_match("log1.txt", "log?.txt") == True
assert unix_match("log12.txt", "log?.txt") == False
assert unix_match("log12.txt", "log??.txt") == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
