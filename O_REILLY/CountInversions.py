'''
En ciencias de la computación y matemáticas discretas, una inversión es un par de lugares en una
secuencia en la que los elementos en dichos lugares están fuera de su orden natural. Por lo tanto,
si utilizamos orden ascendente para caracterizar un grupo de números, entonces una inversión es cuando
uno o más números grandes aparecen antes de números más pequeños en la secuencia.

Echa un vistazo a esta secuencia de ejemplo: (1, 2, 5, 3, 4, 7, 6). Podemos ver aquí tres inversiones:
- 5 y 3;
- 5 y 4;
- 7 y 6.
Se te da una secuencia de números únicos y deberás contar el número de inversiones en dicha secuencia.

Datos de Entrada: Una secuencia, como una tupla de enteros ( int ).

Salida: El número de inversiones, como un entero ( int ).

Ejemplo:
count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3
count_inversion((0, 1, 2, 3)) == 0

¿Cómo se usa?: En esta misión podrás experimentar la maravilla de bucles anidados, por supuesto, si no
utilizas ningún algoritmo avanzado.

Condiciones: 2 < len(sequence) < 200
len(sequence) == len(set(sequence))
all(-100 < x < 100 for x in sequence)

----------
----------

In computer science and discrete mathematics, an inversion is a pair of places in a sequence in which
the elements in those places are out of their natural order. So, if we use ascending order to characterize
a group of numbers, then an inversion is when one or more large numbers appear before smaller numbers in
the sequence.

Take a look at this example sequence: (1, 2, 5, 3, 4, 7, 6). We can see three inversions here:
- 5 y 3;
- 5 y 4;
- 7 y 6.
You are given a sequence of unique numbers and you must count the number of inversions in that sequence.

Input Data: A sequence, as a tuple of integers ( int ).

Output: The number of inversions, as an integer ( int ).

Example:
count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3.
count_inversion((0, 1, 2, 3, 3)) == 0

How to use: In this mission you can experience the wonder of nested loops, of course, if you do not use any
advanced algorithms.

Conditions: 2 < len(sequence) < 200
len(sequence) == len(set(sequence))
all(-100 < x < 100 for x in sequence)
'''


def count_inversion(sequence):
    """
        Count inversions in a sequence of numbers
    """
    inversions = 0
    for i in range(len(sequence)):
        for j in range(i + 1, len(sequence)):
            if sequence[i] > sequence[j]:
                inversions += 1
    return inversions

if __name__ == '__main__':
    print("Example:");
    print(count_inversion([1, 2, 5, 3, 4, 7, 6]));

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3, "Example"
    assert count_inversion((0, 1, 2, 3)) == 0, "Sorted"
    assert count_inversion((99, -99)) == 1, "Two numbers"
    assert count_inversion((5, 3, 2, 1, 0)) == 10, "Reversed"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
