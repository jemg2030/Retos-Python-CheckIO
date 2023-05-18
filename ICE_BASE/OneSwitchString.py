'''
CheckiO platform has a similar mission Verify Anagrams, but in it you have to determine whether
words are anagrams. In this mission, the task will be a little different. You are given two strings
and need to determine whether you can swap two letters in the first string to get the second string.
If so (or words are the same) - return True, if not - False.

For example, the string "btry", if we swap y and t, we get "byrt".

Input: Two strings.

Output: Bool.

Examples:
assert switch_strings("btry", "byrt") == True
assert switch_strings("boss", "boss") == True
assert switch_strings("solid", "disel") == False
assert switch_strings("false", "flaes") == False

Precondition:
All letters are in lower case;
Only letters.

----------
----------

La plataforma CheckiO tiene una misión similar Verificar anagramas, pero en ella hay que
determinar si las palabras son anagramas. En esta misión, la tarea estará un poco diferente.
Se te dan dos cadenas y tienes que determinar si puedes intercambiar dos letras de la primera
cadena para obtener la segunda. Si es así (o las palabras son iguales) - devuelve Verdadero,
si no - Falso.

Por ejemplo, la cadena "btry", si intercambiamos y y t, obtenemos "byrt".

Entrada: Dos cadenas.

Salida: Bool.

Ejemplo:
assert switch_strings("btry", "byrt") == True
assert switch_strings("jefe", "jefe") == True
assert switch_strings("solid", "disel") == False
assert switch_strings("false", "flaes") == False

Precondición:
Todas las letras están en minúsculas;
Sólo letras.
'''


def switch_strings(line: str, result: str) -> bool:
    # your code here
    if line == result:
        return True

    if len(line) != len(result):
        return False

    differing_chars = []
    for i in range(len(line)):
        if line[i] != result[i]:
            differing_chars.append(i)
            if len(differing_chars) > 2:
                return False

    if len(differing_chars) == 2:
        i, j = differing_chars
        if line[i] == result[j] and line[j] == result[i]:
            return True

    return False


print("Example:")
print(switch_strings("btry", "byrt"))

# These "asserts" are used for self-checking
assert switch_strings("btry", "byrt") == True
assert switch_strings("boss", "boss") == True
assert switch_strings("solid", "disel") == False
assert switch_strings("false", "flaes") == False
assert switch_strings("true", "treu") == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
