'''
Your task at hand is to find all the quotes in a given text. And, as per usual, do everything
as quickly as possible. 😉
You are given a string that consists of characters and a paired number of quotation marks. You
need to return an Iterable consisting of the texts inside the quotation marks. But choose only
quotes with double quotation marks ("). Single quotation marks (') aren’t appropriate.

Input: A string.

Output: An iterable.

Example:
find_quotes('"Greetings"') == ['Greetings']
find_quotes('Hi') == []

----------
----------

Tu tarea consiste en encontrar todas las citas de un texto determinado. Y, como de costumbre,
hazlo todo lo más rápido posible 😉 .
Se te da una cadena formada por caracteres y un número par de comillas. Tienes que devolver un
Iterable formado por los textos entrecomillados. Pero elige sólo las comillas dobles ("). Las
comillas simples (') no son apropiadas.

Entrada: Una cadena.

Salida: Un iterable.

Ejemplo:
find_quotes('"Saludos"') == ['Saludos']
find_quotes('Hola') == []
'''


import re


def find_quotes(a):
    # your code here
    pattern = r'"([^"]*)"'
    matches = re.findall(pattern, a)
    return matches


if __name__ == '__main__':
    print("Example:")
    print(find_quotes('"Greetings"'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert find_quotes('"Greetings"') == ['Greetings']
    assert find_quotes('Hi') == []
    assert find_quotes('good morning mister "superman"') == ['superman']
    assert find_quotes('"this" doesn\'t make any "sense"') == ['this', 'sense']
    assert find_quotes('"Lorem Ipsum" is simply dummy text '
 'of the printing and typesetting '
 'industry. Lorem Ipsum has been the '
 '"industry\'s standard dummy text '
 'ever since the 1500s", when an '
 'unknown printer took a galley of '
 'type and scrambled it to make a type '
 'specimen book. It has survived not '
 'only five centuries, but also the '
 'leap into electronic typesetting, '
 'remaining essentially unchanged. "It '
 'was popularised in the 1960s" with '
 'the release of Letraset sheets '
 'containing Lorem Ipsum passages, and '
 'more recently with desktop '
 'publishing software like Aldus '
 'PageMaker including versions of '
 'Lorem Ipsum.') == ['Lorem Ipsum',
 "industry's standard dummy text ever "
 'since the 1500s',
 'It was popularised in the 1960s']
    assert find_quotes('count empty quotes ""') == ['']
    print("Coding complete? Click 'Check' to earn cool rewards!")
