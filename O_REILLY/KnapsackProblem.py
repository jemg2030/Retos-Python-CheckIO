'''
This mission is dedicated to a famous and classical Knapsack Problem.

You are given a list of kinds of items items, that you want to put into knapsack. Item of each kind is a
tuple of its value, weight and maximum amount (optional). You need to find a subset of items, such that:

the total value of the items in subset is as large as possible;
the total weight of items in subset is at most weight, that is weight of the knapsack;
for each kind of items you can select at most given amount items. If its not given - there is no
restriction for amount.
Input: Two arguments. Maximum weight as integer, items as list of tuples of two or three integers.

Output: Maximum value as integer.

Examples:
assert knapsack(5, [(4, 2, 1), (5, 2, 1), (2, 1, 1), (8, 3, 1)]) == 13
assert knapsack(8, [(4, 2), (5, 2), (2, 1), (8, 3)]) == 21
assert knapsack(8, [(10, 10, 3)]) == 0
assert knapsack(8, [(4, 3, 2), (2, 1, 1), (1, 2, 4), (3, 2, 2)]) == 12

----------
----------

Esta misión está dedicada al famoso y clásico Problema de la Mochila.

Se le da una lista de artículos similares, que desea poner en la mochila. El elemento de cada similar es
una tupla de su valor, el peso y la cantidad máxima (opcional). Es necesario encontrar un subconjunto de
elementos, tales que:

el valor total de los elementos del subconjunto sea lo mayor posible;
el peso total de los elementos del subconjunto sea como máximo el peso, es decir, la capacidad de la mochila;
para cada tipo de artículo se puede seleccionar como máximo una cantidad determinada de artículos. Si no se
especifica, no hay restricción de cantidad.
Entrada: Dos argumentos. Peso máximo como entero, elementos como lista de tuplas de dos o tres enteros.

Salida: Valor máximo como entero.

Ejemplo:
assert mochila(5, [(4, 2, 1), (5, 2, 1), (2, 1, 1), (8, 3, 1)]) == 13
assert mochila(8, [(4, 2), (5, 2), (2, 1), (8, 3)]) == 21
assert mochila(8, [(10, 10, 3)]) == 0
assert mochila(8, [(4, 3, 2), (2, 1, 1), (1, 2, 4), (3, 2, 2)]) == 12
'''


def knapsack(weight: int, items: list[tuple[int, int] | tuple[int, int, int]]) -> int:
    # your code here
    num_items = len(items)
    dp = [[0] * (weight + 1) for _ in range(num_items + 1)]

    for item in range(1, num_items + 1):
        item_value, item_weight, item_amount = items[item - 1]
        for curr_weight in range(weight + 1):
            dp[item][curr_weight] = dp[item - 1][curr_weight]
            for amount in range(1, item_amount + 1):
                if curr_weight >= amount * item_weight:
                    dp[item][curr_weight] = max(
                        dp[item][curr_weight],
                        dp[item][curr_weight - amount * item_weight] + amount * item_value
                    )

    return dp[num_items][weight]


print("Example:")
print(knapsack(8, [(4, 3, 2), (2, 1, 1), (1, 2, 4), (3, 2, 2)]))

# These "asserts" are used for self-checking
assert knapsack(5, [(4, 2, 1), (5, 2, 1), (2, 1, 1), (8, 3, 1)]) == 13
assert knapsack(8, [(4, 2), (5, 2), (2, 1), (8, 3)]) == 21
assert knapsack(8, [(10, 10, 3)]) == 0
assert knapsack(8, [(4, 3, 2), (2, 1, 1), (1, 2, 4), (3, 2, 2)]) == 12

print("The mission is done! Click 'Check Solution' to earn rewards!")
