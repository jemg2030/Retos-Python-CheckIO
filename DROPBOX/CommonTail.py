'''
You are given two lists of integers. Elements are unique inside each list. These lists may have common
element(s). But we are interested in the common element(s) at the end of the lists. Your function should
return an element, from what a common part starts and there are no different element(s) after this part -
the first element of the last common part (common tail). If there is no such element (lists don't end with
common element) your function should return None. Good luck!

Input: Two lists of integers.

Output: Integer or None.

Examples:
assert common_tail([], [1, 2, 3]) == None
assert common_tail([1], [1]) == 1
assert common_tail([3], [1, 2, 3]) == 3

----------
----------

Se dan dos listas de números enteros. Los elementos son únicos dentro de cada lista. Estas listas pueden
tener elemento(s) común(es). Pero estamos interesados en el elemento común (s) al final de las listas. Su
función debe devolver un elemento, de lo que comienza una parte común y no hay elemento(s) diferente(s)
después de esta parte - el primer elemento de la última parte común (cola común). Si no hay tal elemento
(las listas no terminan con un elemento común) tu función debería devolver Ninguno. Suerte

Entrada: Dos listas de enteros.

Salida: Entero o Ninguno.

Ejemplo:
assert cola_común([], [1, 2, 3]) == Ninguno
assert cola_común([1], [1]) == 1
assert cola_común([3], [1, 2, 3]) == 3
'''


def common_tail(a: list[int], b: list[int]) -> int | None:
    # your code here
    i = len(a) - 1
    j = len(b) - 1

    while i >= 0 and j >= 0 and a[i] == b[j]:
        i -= 1
        j -= 1

    if i < len(a) - 1:
        return a[i + 1]
    else:
        return None


print("Example:")
print(common_tail([1, 2, 3, 4], [5, 6, 3, 4]))

# These "asserts" are used for self-checking
assert common_tail([], [1, 2, 3]) == None
assert common_tail([1], [1]) == 1
assert common_tail([3], [1, 2, 3]) == 3

print("The mission is done! Click 'Check Solution' to earn rewards!")
