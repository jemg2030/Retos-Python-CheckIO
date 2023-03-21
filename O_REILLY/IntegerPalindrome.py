'''
You need to determine whether the given integer (in base 10) is a palindrome or not in base B.
Base (or radix) is written as subscript text. A number is a palindrome if it reads the same in
both directions, for example 12110 is a palindrome, and 12210 is not. If the integerB is a palindrome,
return True, if not, return False. Read more about number bases.

The most common base is decimal. To convert an integer10 to another base you need to divide it by
base and take reminders until the number becomes equal zero. Let's look at the following example -
convert integer 610 into the binary form 62.

Integer	Quotient	Reminder	Normal	Reversed
6	        3	        0	        0	    0
3	        1	        1	        10	    01
1	        0	        1	        110	    011
0

Since reversed 011 is not equal normal 110 - 62 is not a palindrome.
To return back to the decimal form, start from zero, multiply by base and add reminders.
For 62 == 110 it's (((0*2) + 1)*2 + 1)*2 + 0 = 6.

Input: Given integer and base B (integer).

Output: Bool.

Examples:
assert int_palindrome(6, 2) == False
assert int_palindrome(34, 2) == False
assert int_palindrome(455, 2) == True

Preconditions:
number >= 0;
number is integer;
B >= 2;
B is integer.

----------
----------

Tienes que determinar si el número entero dado (en base 10) es un palíndromo o no en base B.
La base (o radix) se escribe como texto de subíndice. Un número es un palíndromo si se lee igual
en ambas direcciones, por ejemplo 12110 es un palíndromo, y 12210 no lo es. Si el número enteroB
es un palíndromo, devuelve True, si no, devuelve False. Más información sobre bases numéricas.

La base más común es la decimal. Para convertir un entero10 a otra base hay que dividirlo por la
base y tomar recordatorios hasta que el número sea igual a cero. Veamos el siguiente ejemplo - convertir
el entero 610 a la forma binaria 62.

Integer	Quotient	Reminder	Normal	Reversed
6	        3	        0	        0	    0
3	        1	        1	        10	    01
1	        0	        1	        110	    011
0

Como invertido 011 no es igual a normal 110 - 62 no es un palíndromo.
Para volver a la forma decimal, se parte de cero, se multiplica por la base y se añaden los recordatorios.
Para 62 == 110 es (((0*2) + 1)*2 + 1)*2 + 0 = 6.

Entrada: Dado entero y base B (entero).

Salida: Bool.

Ejemplos:
assert int_palindrome(6, 2) == False
assert int_palindrome(34, 2) == False
assert int_palindrome(455, 2) == True

Precondiciones:
número >= 0;
número es entero;
B >= 2;
'''


def int_palindrome(number: int, B: int) -> bool:
    # your code here
    # Convert the number to the specified base
    digits = []
    while number > 0:
        digits.append(number % B)
        number //= B
    # Check if the resulting number is a palindrome
    for i in range(len(digits) // 2):
        if digits[i] != digits[-i - 1]:
            return False
    return True


print("Example:")
print(int_palindrome(455, 2))

# These "asserts" are used for self-checking
assert int_palindrome(6, 2) == False
assert int_palindrome(34, 2) == False
assert int_palindrome(455, 2) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
