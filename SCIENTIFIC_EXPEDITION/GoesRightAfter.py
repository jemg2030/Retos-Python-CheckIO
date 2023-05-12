'''
In a given word you need to check if one symbol goes only right after another.

Cases you should expect while solving this challenge:

one of the symbols is not in the given word - your function should return False;
any symbol appears in a word more than once - use only the first one;
two symbols are the same - your function should return False;
the condition is case sensitive, which means 'a' and 'A' are two different symbols.
Input: Three arguments. The first one is a given string, second is a symbol that should go first, and
the third is a symbol that should go after the first one.

Output: A bool.

Examples:
assert goes_after("world", "w", "o") == True
assert goes_after("world", "w", "r") == False
assert goes_after("world", "l", "o") == False
assert goes_after("panorama", "a", "n") == True
assert goes_after("list", "l", "o") == False
assert goes_after("", "l", "o") == False
assert goes_after("list", "l", "l") == False
assert goes_after("world", "d", "w") == False
assert goes_after("Almaz", "a", "l") == False
assert goes_after("transport", "r", "t") == False
assert goes_after("almaz", "m", "a") == False

----------
----------

En una palabra dada debe registrar si un símbolo va justo después de otro.

Casos que debe esperar al resolver este reto:

uno de los símbolos no está en la palabra dada - su función debe devolver False;
cualquier símbolo aparece en una palabra más de una vez - utilice sólo el primero;
dos símbolos son iguales: la función devolverá False;
la condición distingue entre mayúsculas y minúsculas, lo que significa que "a" y "A" son dos
símbolos diferentes.
Entrada: Tres argumentos. El primero es una cadena dada, el segundo es un símbolo que debe ir
primero, y el tercero es un símbolo que debe ir después del primero.

Salida: Un bool.

Ejemplos:
assert goes_after("world", "w", "o") == True
assert goes_after("world", "w", "r") == False
assert goes_after("world", "l", "o") == False
assert goes_after("panorama", "a", "n") == True
assert goes_after("list", "l", "o") == False
assert goes_after("", "l", "o") == False
assert goes_after("list", "l", "l") == False
assert goes_after("world", "d", "w") == False
assert goes_after("Almaz", "a", "l") == False
assert goes_after("transport", "r", "t") == False
assert goes_after("almaz", "m", "a") == False
'''


def goes_after(word: str, first: str, second: str) -> bool:
    # your code here
    return 0 < word.find(second) == word.find(first) + 1


print("Example:")
print(goes_after("world", "w", "o"))

# These "asserts" are used for self-checking
assert goes_after("world", "w", "o") == True
assert goes_after("world", "w", "r") == False
assert goes_after("world", "l", "o") == False
assert goes_after("panorama", "a", "n") == True
assert goes_after("list", "l", "o") == False
assert goes_after("", "l", "o") == False
assert goes_after("list", "l", "l") == False
assert goes_after("world", "d", "w") == False
assert goes_after("Almaz", "a", "l") == False
assert goes_after("transport", "r", "t") == False
assert goes_after("almaz", "m", "a") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
