'''
Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence
1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, ... shows the first 11 ugly numbers. By convention,
1 is included. Write a program to find and print the N’th ugly number

Input: N, int.

Output: N'th Ugly Number, int.

Example:
ugly_number(4) == 4
ugly_number(6) == 6
ugly_number(11) == 15

How it’s used: Demonstrate that straight way can be very slow

Precondition: Given int is below or equal of 1500

The mission was taken from ICPC challenge

----------
----------

Los números feos son números cuyos únicos factores primos son 2, 3 ó 5. La secuencia
1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, ... muestra los 11 primeros números feos. Por
convención, se incluye el 1. Escribe un programa para encontrar e imprimir el N'º número feo

Entrada: N, int.

Salida: N'th Número Feo, int.

Ejemplo:
numero_feo(4) == 4
número_feo(6) == 6
número_feo(11) == 15

Cómo se utiliza: Demostrar que el camino recto puede ser muy lento

Precondición: Dado int es inferior o igual a 1500

La misión fue tomada del desafío ICPC
'''


def ugly_number(n: int) -> int:
    # your code here
    ugly_numbers = [1]  # Initialize the list with the first ugly number
    i2 = i3 = i5 = 0  # Pointers for multiplying by 2, 3, and 5

    while len(ugly_numbers) < n:
        # Find the next ugly number by multiplying the current ugly numbers with 2, 3, and 5
        next_ugly = min(ugly_numbers[i2] * 2, ugly_numbers[i3] * 3, ugly_numbers[i5] * 5)

        # Update the pointers
        if next_ugly == ugly_numbers[i2] * 2:
            i2 += 1
        if next_ugly == ugly_numbers[i3] * 3:
            i3 += 1
        if next_ugly == ugly_numbers[i5] * 5:
            i5 += 1

        ugly_numbers.append(next_ugly)  # Add the next ugly number to the list

    return ugly_numbers[-1]  # Return the Nth ugly number


if __name__ == "__main__":
    print("Example:")
    print(ugly_number(4))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert ugly_number(4) == 4
    assert ugly_number(6) == 6
    assert ugly_number(11) == 15
    print("Ugly Numbers coding complete? Click 'Check' to earn cool rewards!")
