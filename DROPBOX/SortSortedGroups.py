'''
You are given a list of integers. Your goal is to find all sorted groups (group of numbers with distinct
sorting order or single value) inside the list, sort input list by these groups and return this sorted
list with groups unpacked.

For example, [5, 1, 5, 0, 5] --> [[5, 1], [5, 0], [5]] --> [[5], [5, 0], [5, 1]] --> [5, 5, 0, 5, 1].

If adjacent numbers are equal, consider sorting order remains the same. If a group starts with equal numbers,
seek the different number further to determine or check sorting order, or end of the list. You should find out
the sorting order for each group, not once for the whole list. If the first group has the descending order, it
doesn’t mean, you should build all you groups as descending. You should be greedy from the left - take as much
numbers as possible to build and determine the sequence with distinct order. Good luck!

Input: List of integers.

Output: List of integers.

Examples:
assert sorted_groups([]) == []
assert sorted_groups([5]) == [5]
assert sorted_groups([5, 1, 5, 0, 5]) == [5, 5, 0, 5, 1]
assert sorted_groups([5, 5, 1]) == [5, 5, 1]

----------
----------

Se le da una lista de números enteros. Su objetivo es encontrar todos los grupos ordenados (grupo de
números con distinto orden de clasificación o valor único) dentro de la lista, ordenar la lista de
entrada por estos grupos y devolver esta lista ordenada con los grupos desempaquetados.

Por ejemplo, [5, 1, 5, 0, 5] --> [[5, 1], [5, 0], [5]] --> [[5], [5, 0], [5, 1]] --> [5, 5, 0, 5, 1].

Si los números adyacentes son iguales, considere el orden de clasificación sigue siendo el mismo. Si un
grupo comienza con números iguales, busque el número diferente más adelante para determinar o registrar
el orden de clasificación, o el final de la lista. Debe averiguar el orden de clasificación para cada grupo,
no una vez para toda la lista. Si el primer grupo es descendente, no significa que todos los grupos deban ser
descendentes. Usted debe ser codicioso de la izquierda - tomar tantos números como sea posible para construir
y determinar la secuencia con orden distinto. Buena suerte.

Entrada: Lista de enteros.

Salida: Lista de enteros.

Ejemplo:
assert grupos_ordenados([]) == []
assert grupos_ordenados([5]) == [5]
assert grupos_ordenados([5, 1, 5, 0, 5]) == [5, 5, 0, 5, 1]
assert grupos_ordenados([5, 5, 1]) == [5, 5, 1]
'''


def sorted_groups(items: list[int]) -> list[int]:
    # your code here
    if not items:
        return items
    it = iter(items)
    direction, stack = 0, [[next(it)]]
    for i in it:
        prev, prev_dir = stack[-1][-1], direction
        direction = (prev < i) - (i < prev) or prev_dir
        if prev_dir and prev_dir != direction:
            direction = bool(stack.append([i]))
        else:
            stack[-1].append(i)
    stack.sort()
    return [x for it in stack for x in it]


print("Example:")
print(sorted_groups([5, 1, 5, 0, 5]))

# These "asserts" are used for self-checking
assert sorted_groups([]) == []
print(sorted_groups([]) == [])
print(sorted_groups([]))
assert sorted_groups([5]) == [5]
print(sorted_groups([5]) == [5])
print(sorted_groups([5]))
assert sorted_groups([5, 1, 5, 0, 5]) == [5, 5, 0, 5, 1]
print(sorted_groups([5, 1, 5, 0, 5]) == [5, 5, 0, 5, 1])
print(sorted_groups([5, 1, 5, 0, 5]))
assert sorted_groups([5, 5, 1]) == [5, 5, 1]
print(sorted_groups([5, 5, 1]) == [5, 5, 1])
print(sorted_groups([5, 5, 1]))

print("The mission is done! Click 'Check Solution' to earn rewards!")
