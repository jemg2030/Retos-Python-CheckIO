'''

In a given text you need to sum the numbers while excluding any digits that form part of a word.

The text consists of numbers, spaces and letters from the English alphabet.

Input: A string.

Output: An int.

Example:
1 sum_numbers('hi') == 0
2 sum_numbers('who is 1st here') == 0
3 sum_numbers('my numbers is 2') == 2
4 sum_numbers('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year') == 3755
5 sum_numbers('5 plus 6 is') == 11
6 sum_numbers('') == 0

---------
---------

En un texto dado hay que sumar los números excluyendo los dígitos que forman parte de una palabra.

El texto está formado por números, espacios y letras del alfabeto inglés.

Entrada: Una cadena.

Salida: Un int.

Ejemplo:
1 sum_numbers('hi') == 0
2 sum_numbers('quién es el primero aquí') == 0
3 sum_numbers('mi número es 2') == 2
4 sum_numbers('Este cuadro es un óleo sobre lienzo '
 'pintura de la artista danesa Anna '
 'Petersen entre 1845 y 1910 año') == 3755
5 sum_numbers('5 más 6 es') == 11
6 sum_numbers('') == 0

'''


def sum_numbers(text: str) -> int:
    # your code here
    return 0


if __name__ == '__main__':
    print("Example:")
    print(sum_numbers('hi'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sum_numbers('hi') == 0
    assert sum_numbers('who is 1st here') == 0
    assert sum_numbers('my numbers is 2') == 2
    assert sum_numbers('This picture is an oil on canvas '
                       'painting by Danish artist Anna '
                       'Petersen between 1845 and 1910 year') == 3755
    assert sum_numbers('5 plus 6 is') == 11
    assert sum_numbers('') == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")