'''
Try to find out how many zeros a given number has at the end.

Input: A positive Int

Output: An Int.

Example:
assert end_zeros(0) == 1
assert end_zeros(1) == 0
assert end_zeros(10) == 1
assert end_zeros(101) == 0
assert end_zeros(245) == 0
assert end_zeros(100100) == 2

----------
----------

Intenta averiguar cuántos ceros tiene al final un número dado.

Entrada: Un Int positivo

Salida: Un Int.

Ejemplo:
assert fin_zeros(0) == 1
assert fin_zeros(1) == 0
assert ceros(10) == 1
assert ceros(101) == 0
'''


def end_zeros(a: int) -> int:
    count = 0
    while a % 10 == 0 and a != 0:
        count += 1
        a //= 10
    if(a == 0):
        return 1
    return count


print("Example:")
print(end_zeros(10))

# These "asserts" are used for self-checking
assert end_zeros(0) == 1
assert end_zeros(1) == 0
assert end_zeros(10) == 1
assert end_zeros(101) == 0
assert end_zeros(245) == 0
assert end_zeros(100100) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")