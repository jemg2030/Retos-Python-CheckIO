"""
Sometimes you find yourself in a situation where among a huge number of files on your
computer or in a separate folder you need to find files of a certain type - for example,
images with the extension '.jpg' or documents with the extension '.txt', or even files
that have the word 'butterfly' in their name. Doing this manually can be time-consuming.
'Matching' or patterns for searching files by a specific mask are just what you need for
these sort of challenges.
This mission will help you understand how this works.

You need to find out if the given unix pattern matches the given filename.

Let me show you a couple of small examples of matching the filenames in the unix-shell. For
example, * matches everything and *.txt matches all of the files that have txt extension.
Here is a small table that shows symbols that can be used in patterns.

*	matches everything
?	matches any single character
[seq]	matches any character in seq
[!seq]	matches any character not in seq
Input: Two arguments. Both are strings.

Output: Bool.

Example:
unix_match('somefile.txt', '*') == True
unix_match('other.exe', '*') == True
unix_match('my.exe', '*.txt') == False
unix_match('log1.txt', 'log?.txt') == True
unix_match('log1.txt', 'log[1234567890].txt') == True
unix_match('log12.txt', 'log?.txt') == False
unix_match('log12.txt', 'log??.txt') == True

How it is used: in the unix-shell

----------
----------

A veces se encuentra en una situación en la que, entre un gran número de archivos en
su ordenador o en una carpeta separada, necesita encontrar archivos de un tipo determinado
- por ejemplo, imágenes con la extensión '.jpg' o documentos con la extensión '.txt', o
incluso archivos que tienen la palabra 'mariposa' en su nombre. Hacer esto manualmente
puede llevar mucho tiempo. Las 'coincidencias' o patrones para buscar archivos por una
máscara específica son justo lo que necesitas para este tipo de retos.
Esta misión te ayudará a entender cómo funciona.

Tienes que averiguar si el patrón unix dado coincide con el nombre de archivo dado.

Permíteme mostrarte un par de pequeños ejemplos de coincidencia de nombres de archivo en
unix-shell. Por ejemplo, * coincide con todo y *.txt coincide con todos los archivos que
tienen extensión txt. Aquí hay una pequeña tabla que muestra los símbolos que se pueden
utilizar en los patrones.

* coincide con todo
? coincide con cualquier carácter
[seq] coincide con cualquier carácter de seq
[!seq] coincide con cualquier carácter que no esté en seq
Entrada: Dos argumentos. Ambos son cadenas.

Salida: Bool.

Ejemplo:
unix_match('algunarchivo.txt', '*') == True
unix_match('otro.exe', '*') == True
unix_match('mi.exe', '*.txt') == False
unix_match('log1.txt', 'log?.txt') == True
unix_match('log1.txt', 'log[1234567890].txt') == True
unix_match('log12.txt', 'log?.txt') == False
unix_match('log12.txt', 'log??.txt') == True

Cómo se utiliza: en el unix-shell
"""


import re


def unix_match(filename: str, pattern: str) -> bool:
    # your code here
    list = [(".", "\."), ("?", "."), ("[.]", "."), ("[[]", "\["), ("[]]", "\]")]
    x = pattern
    for a, b in list:
        x = x.replace(a, b)
    if "[!]" not in pattern:
        x = x.replace("[!", "[^")
    else:
        x = x.replace("[!]", "\[!\]")
    if "[*]" not in pattern:
        x = x.replace("*", ".+")

    try:
        return re.match(x, filename) is not None
    except:
        return pattern == filename


if __name__ == "__main__":
    print("Example:")
    print(unix_match("somefile.txt", "*"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert unix_match("somefile.txt", "*") == True
    assert unix_match("other.exe", "*") == True
    assert unix_match("my.exe", "*.txt") == False
    assert unix_match("log1.txt", "log?.txt") == True
    assert unix_match("log1.txt", "log[1234567890].txt") == True
    assert unix_match("log12.txt", "log?.txt") == False
    assert unix_match("log12.txt", "log??.txt") == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
