'''
Sort the given list so that its elements should be grouped and those groups end up in the
decreasing frequency order, that is, the number of times element appears in the list. If two
elements have the same frequency, their groups should end up according to the natural order
of elements. For example: [5, 2, 4, 1, 1, 1, 3] ==> [1, 1, 1, 2, 3, 4, 5].

If you want to practice more with the similar case, try Sort Array by Element Frequency mission.

Input: List of integers.

Output: List or another Iterable (tuple, iterator, generator).

Examples:
assert list(frequency_sorting([1, 2, 3, 4, 5])) == [1, 2, 3, 4, 5]
assert list(frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3])) == [
    4,
    4,
    4,
    3,
    3,
    11,
    11,
    7,
    13,
]

How it is used: For analyzing data using mathematical statistics and mathematical analysis,
and for finding trends and predicting future changes (systems, phenomena, etc.).

Preconditions:
list length <= 100;
max number <= 100.

----------
----------

Ordena la lista dada de modo que sus elementos se agrupen y esos grupos terminen en el
orden de frecuencia decreciente, es decir, el número de veces que el elemento aparece en
la lista. Si dos elementos tienen la misma frecuencia, sus grupos se ordenarán según el
orden natural de los elementos. Por ejemplo: [5, 2, 4, 1, 1, 1, 3] ==> [1, 1, 1, 2, 3, 4, 5].

Si quieres practicar más con el caso similar, prueba la misión Ordenar array por frecuencia de elementos.

Entrada: Lista de enteros.

Salida: Lista u otro Iterable (tupla, iterador, generador).

Ejemplos:
assert list(frecuencia_orden([1, 2, 3, 4, 5])) == [1, 2, 3, 4, 5])
assert list(frecuencia_clasificacion([3, 4, 11, 13, 11, 4, 4, 7, 3])) == [
    4,
    4,
    4,
    3,
    3,
    11,
    11,
    7,
    13,
]

Cómo se utiliza: Para analizar datos utilizando la estadística matemática y el análisis
matemático, y para encontrar tendencias y predecir cambios futuros (sistemas, fenómenos, etc.).

Precondiciones:
longitud lista <= 100;
número máximo <= 100.
'''


from collections.abc import Iterable


def frequency_sorting(numbers: list[int]) -> Iterable[int]:
    # replace this for solution
    freq = {}
    for n in numbers:
        if n in freq:
            freq[n] += 1
        else:
            freq[n] = 1
    return sorted(numbers, key=lambda n: (-freq[n], n))


print("Example:")
print(list(frequency_sorting([1, 2, 3, 4, 5])))

# These "asserts" are used for self-checking
assert list(frequency_sorting([1, 2, 3, 4, 5])) == [1, 2, 3, 4, 5]
assert list(frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3])) == [
    4,
    4,
    4,
    3,
    3,
    11,
    11,
    7,
    13,
]

print("The mission is done! Click 'Check Solution' to earn rewards!")
