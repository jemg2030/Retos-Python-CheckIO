'''
We have a list of booleans. Let's check if the majority of elements are True.

Some cases worth mentioning: 1) an empty list should return False; 2) if True-s and False-s have an equal
amount, function should return False.

Input: A list of booleans.

Output: A Boolean.

Examples:
assert is_majority([True, True, False, True, False]) == True
assert is_majority([True, True, False]) == True
assert is_majority([True, True, False, False]) == False
assert is_majority([True, True, False, False, False]) == False

----------
----------

Tenemos una lista de booleanos. Registremos si la mayoría de los elementos son True.

Algunos casos dignos de mención: 1) una lista vacía debería devolver False; 2) si True-s y False-s tienen
la misma cantidad, la función debería devolver False.

Entrada: Una lista de booleanos.

Salida: Un booleano.

Ejemplos:
assert es_mayoria([Verdadero, Verdadero, Falso, Verdadero, Falso]) == Verdadero
assert es_mayoría([Verdadero, Verdadero, Falso]) == Verdadero
assert is_majority([Verdadero, Verdadero, Falso, Falso]) == False
assert is_majority([Verdadero, Verdadero, Falso, Falso, False]) == False
'''


def is_majority(items: list[bool]) -> bool:
    # your code here
    if not items:
        return False

    count_true = items.count(True)
    count_false = items.count(False)

    if count_true > count_false:
        return True
    else:
        return False


print("Example:")
print(is_majority([True, True, False, True, False]))

# These "asserts" are used for self-checking
assert is_majority([True, True, False, True, False]) == True
assert is_majority([True, True, False]) == True
assert is_majority([True, True, False, False]) == False
assert is_majority([True, True, False, False, False]) == False
assert is_majority([False]) == False
assert is_majority([True]) == True
assert is_majority([]) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
