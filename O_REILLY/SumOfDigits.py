'''
The task in this mission is as follows:

You are given an integer. If it consists of one digit, simply return its value. If it consists of two or more
digits - add them until the number contains only one digit and return it.

Input: A int.

Output: A int.

Example:
assert sum_digits(38) == 2
assert sum_digits(0) == 0
assert sum_digits(10) == 1
assert sum_digits(132) == 6

---------
---------

La tarea de esta misión es la siguiente:

Se le da un número entero. Si consta de un dígito, simplemente devuelva su valor. Si consta de dos o más
dígitos, súmelos hasta que el número contenga un solo dígito y devuélvalo.

Entrada: Un int.

Salida: Un int.

Ejemplo:
assert suma_dígitos(38) == 2
assert suma_dígitos(0) == 0
assert suma_dígitos(10) == 1
assert suma_dígitos(132) == 6
'''


def sum_digits(num: int) -> int:
    # your code here
    # If the num has only one digit, return it
    if num < 10:
        return num

    # If the num has two or more digits, keep adding them until we get a single digit
    while num >= 10:
        # Compute the sum of the digits
        digit_sum = 0
        for digit in str(num):
            digit_sum += int(digit)
        num = digit_sum

    return num


print("Example:")
print(sum_digits(38))

assert sum_digits(38) == 2
assert sum_digits(0) == 0
assert sum_digits(10) == 1
assert sum_digits(132) == 6
assert sum_digits(232) == 7
assert sum_digits(811) == 1
assert sum_digits(702) == 9

print("The mission is done! Click 'Check Solution' to earn rewards!")
