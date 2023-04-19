'''
You are given a positive integer. Your function should calculate the product of the digits excluding any zeroes.

For example: The number given is 123405. The result will be 1*2*3*4*5=120 (don't forget to exclude zeroes).

Input: A positive integer.

Output: The product of the digits as an integer.

Examples:
assert checkio(123405) == 120
assert checkio(999) == 729
assert checkio(1000) == 1
assert checkio(1111) == 1

How it is used: This task can teach you how to solve a problem with simple data type conversion.

Precondition:
0 < number < 106

----------
----------

Se le da un número entero positivo. Tu función debe calcular el producto de los dígitos excluyendo los ceros.

Por ejemplo: El número dado es 123405. El resultado estará 1*2*3*4*5=120 (no olvide excluir los ceros).

Entrada: Un número entero positivo.

Salida: El producto de los dígitos como un entero.

Ejemplos:
assert checkio(123405) == 120
assert checkio(999) == 729
assert checkio(1000) == 1
assert checkio(1111) == 1

Cómo se utiliza: Esta tarea puede enseñarte a resolver un problema con una simple conversión de tipos de datos.

Condición previa:
0 < número < 106
'''


def checkio(number: int) -> int:
    # your code here
    product = 1
    for digit in str(number):
        if digit != '0':
            product *= int(digit)
    return product


print("Example:")
print(checkio(123405))

# These "asserts" are used for self-checking
assert checkio(123405) == 120
assert checkio(999) == 729
assert checkio(1000) == 1
assert checkio(1111) == 1

print("The mission is done! Click 'Check Solution' to earn rewards!")
