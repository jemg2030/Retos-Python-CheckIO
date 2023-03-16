'''
You are given a list of files. You need to sort this list by the file extension. The files
with the same extension (or without one) should be sorted by name.

Some possible cases:

Filename cannot be an empty string;
Sorting order: files without name, files without extension, files with name and extension;
Filename .config or config. is all name with an empty extension;
Filename like str1.str2.str3 has an extension str3 and a name str1.str2;
Filename like .str1.str2 has an extension str2 and a name .str1.
Input: List of strings.

Output: List of strings.

Examples:
assert sort_by_ext(["1.cad", "1.bat", "1.aa"]) == ["1.aa", "1.bat", "1.cad"]
assert sort_by_ext(["1.cad", "1.bat", "1.aa", "2.bat"]) == [
    "1.aa",
    "1.bat",
    "2.bat",
    "1.cad",
]
assert sort_by_ext(["1.cad", "1.bat", "1.aa", ".bat"]) == [
    ".bat",
    "1.aa",
    "1.bat",
    "1.cad",
]
assert sort_by_ext(["1.cad", "1.bat", ".aa", ".bat"]) == [
    ".aa",
    ".bat",
    "1.bat",
    "1.cad",
]

----------
----------

Se le proporciona una lista de archivos. Tiene que ordenar esta lista por la extensión del fichero. Los ficheros con la misma extensión (o sin ella) deben ordenarse por nombre.

Algunos casos posibles:

El nombre del fichero no puede ser una cadena vacía;
Orden de clasificación: ficheros sin nombre, ficheros sin extensión, ficheros con nombre y extensión;
Filename .config o config. es todo nombre con una extensión vacía;
Nombre de fichero como str1.str2.str3 tiene una extensión str3 y un nombre str1.str2;
Filename like .str1.str2 has an extension str2 and a name .str1.
Entrada: Lista de cadenas.

Salida: Lista de cadenas.

Ejemplos:
assert sort_by_ext(["1.cad", "1.bat", "1.aa"]) == ["1.aa", "1.bat", "1.cad"].
assert sort_by_ext(["1.cad", "1.bat", "1.aa", "2.bat"]) == [
    "1.aa",
    "1.bat",
    "2.bat",
    "1.cad",
]
assert sort_by_ext(["1.cad", "1.bat", "1.aa", ".bat"]) == [
    ".bat",
    "1.aa",
    "1.bat",
    "1.cad",
]
assert sort_by_ext(["1.cad", "1.bat", ".aa", ".bat"]) == [
    ".aa",
    ".bat",
    "1.bat",
    "1.cad",
]
'''


def sort_by_ext(files: list[str]) -> list[str]:
    # your code here
    def get_key(filename):
        parts = filename.split(".")
        if len(parts) == 1:
            # file without extension
            return ("", filename)
        elif len(parts) == 2 and not parts[0]:
            # file with extension only
            return ("", parts[1])
        else:
            # file with name and extension
            return (parts[-1], ".".join(parts[:-1]))

    return sorted(files, key=get_key)


print("Example:")
print(sort_by_ext(["1.cad", "1.bat", "1.aa"]))

# These "asserts" are used for self-checking
assert sort_by_ext(["1.cad", "1.bat", "1.aa"]) == ["1.aa", "1.bat", "1.cad"]
assert sort_by_ext(["1.cad", "1.bat", "1.aa", "2.bat"]) == [
    "1.aa",
    "1.bat",
    "2.bat",
    "1.cad",
]
assert sort_by_ext(["1.cad", "1.bat", "1.aa", ".bat"]) == [
    ".bat",
    "1.aa",
    "1.bat",
    "1.cad",
]
assert sort_by_ext(["1.cad", "1.bat", ".aa", ".bat"]) == [
    ".aa",
    ".bat",
    "1.bat",
    "1.cad",
]
assert sort_by_ext(["1.cad", "1.", "1.aa"]) == ["1.", "1.aa", "1.cad"]
assert sort_by_ext(["1.cad", "1.bat", "1.aa", "1.aa.doc"]) == [
    "1.aa",
    "1.bat",
    "1.cad",
    "1.aa.doc",
]
assert sort_by_ext(["1.cad", "1.bat", "1.aa", ".aa.doc"]) == [
    "1.aa",
    "1.bat",
    "1.cad",
    ".aa.doc",
]

print("The mission is done! Click 'Check Solution' to earn rewards!")
