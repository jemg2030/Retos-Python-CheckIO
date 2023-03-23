'''
Write a function that finds the longest palindromic substring of a given string. Try to be as efficient
as possible!

If you find more than one substring, you should return the one that’s closer to the beginning.

Input: A text as a string.

Output: The longest palindromic substring.

Examples:
longest_palindromic('abc') == 'a'
longest_palindromic('abacada') == 'aba'

Precondition: 1 < |text| ≤ 20
The text contains only ASCII characters.

----------
----------

Escribe una función que encuentre la subcadena palindrómica más larga de una cadena dada. Intenta ser
lo más eficiente posible.

Si encuentras más de una subcadena, debes devolver la que esté más cerca del principio.

Entrada: Un texto en forma de cadena.

Salida: La subcadena palindrómica más larga.

Ejemplo:
longest_palindromic('abc') == 'a'
longest_palindromic('abacada') == 'aba'

Precondición: 1 < |text| ≤ 20
El texto sólo contiene caracteres ASCII.
'''


def longest_palindromic(a):
    # your code here
    return None


if __name__ == '__main__':
    print("Example:")
    print(longest_palindromic('abc'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert longest_palindromic('abc') == 'a'
    assert longest_palindromic('abacada') == 'aba'
    assert longest_palindromic('artrartrt') == 'rtrartr'
    assert longest_palindromic('aaaaa') == 'aaaaa'
    print("Coding complete? Click 'Check' to earn cool rewards!")
