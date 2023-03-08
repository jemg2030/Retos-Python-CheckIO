'''
You are given a list of integers. Your task in this mission is to find, how many times the sorting direction
was changed in the given list. If the elements are equal - the previous sorting direction remains the same,
if the sequence starts from the same elements - look for the next different to determine the sorting direction.

Let's look at the scheme:

There are three sorting directions:

on the chunk 1, 2, 2 - up (increasing);
on the chunk 2, 1 - down (decreasing);
and on the chunk 1, 2, 2 - up again.
So, you have two points of changing the sorting direction: #1 - from up to down, and #2 - from down to up.
That's the result your function should return.
Input: A list of integers.

Output: Integer.

Examples:
assert changing_direction([1, 2, 3, 4, 5]) == 0
assert changing_direction([1, 2, 3, 2, 1]) == 1
assert changing_direction([1, 2, 2, 1, 2, 2]) == 2

Preconditions:
the list is non-empty;
the elements in the list are positive integers.

----------
----------

Se le da una lista de números enteros. Su tarea en esta misión es encontrar, cuántas veces se cambió la
dirección de ordenación en la lista dada. Si los elementos son iguales - la dirección de ordenación anterior
sigue siendo el mismo, si la secuencia se inicia a partir de los mismos elementos - buscar la siguiente
diferente para determinar la dirección de ordenación.

Veamos el esquema

Hay tres direcciones de ordenación

en el chunk 1, 2, 2 - hacia arriba (creciente);
en el chunk 2, 1 - hacia abajo (decreciente);
y en el chunk 1, 2, 2 - arriba otra vez.
Por lo tanto, tiene dos puntos de cambiar la dirección de clasificación: #1 - de arriba a abajo, y #2 - de
abajo a arriba. Ese es el resultado que debe devolver tu función.
Entrada: Una lista de enteros.

Salida: Entero.

Ejemplos:
assert cambio_direccion([1, 2, 3, 4, 5]) == 0
assert cambio_direccion([1, 2, 3, 2, 1]) == 1
assert cambio_dirección([1, 2, 2, 1, 2, 2]) == 2

Precondiciones:
la lista no está vacía;
los elementos de la lista son enteros positivos.
'''


def changing_direction(elements: list[int]) -> int:
    # your code here
    direction = 0
    prev = elements[0]
    count = 0
    for i in range(1, len(elements)):
        curr = elements[i]
        if curr > prev:
            curr_dir = 1
        elif curr < prev:
            curr_dir = -1
        else:
            curr_dir = 0
        if curr_dir != 0 and direction != 0 and curr_dir != direction:
            count += 1
        direction = curr_dir if curr_dir != 0 else direction
        prev = curr
    return count


print("Example:")
print(changing_direction([1, 2, 3, 4, 5]))

# These "asserts" are used for self-checking
assert changing_direction([1, 2, 3, 4, 5]) == 0
assert changing_direction([1, 2, 3, 2, 1]) == 1
assert changing_direction([1, 2, 2, 1, 2, 2]) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")
