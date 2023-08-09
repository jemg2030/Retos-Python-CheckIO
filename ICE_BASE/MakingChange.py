"""
Nicola is taking a much needed vacation. He'll be backpacking around some lesser-known countries.
Each has its own unique currency.

When making purchases, Nicola would like to use the minimum number of coins possible. For example,
Outer Leftopia has coins with denomination 1, 3, and 5 shillings. He wants to buy a souvenir that
costs 13 shillings. He can do that using two 5 shilling coins and one 3 shilling coin.

You can assume Nicola has access to an infinite number of coins of each denomination. (He has a
large bank account and access to an ATM).

Input: Two arguments. The first argument is an int: the price of the purchase. The second is a
list of ints: the denominations of available coins.

Output: int. The minimum number of coins Nicola can use to make the purchase. If the price cannot
be made with the available denominations, return None .

Example:
checkio(8, [1, 3, 5]) == 2
checkio(12, [1, 4, 5]) == 3

How it is used: Besides helping Nicola make change, this is an example of a problem in
combinatorial optimization.

Precondition: Inputs are all positive integers.

----------
----------

Nicola se toma unas vacaciones muy necesarias. Viajará de mochilero por algunos países menos
conocidos. Cada uno tiene su propia moneda.

Cuando hace compras, Nicola quiere utilizar el menor número de monedas posible. Por ejemplo,
Outer Leftopia tiene monedas de 1, 3 y 5 chelines. Quiere comprar un recuerdo que cuesta 13
chelines. Puede hacerlo con dos monedas de 5 chelines y una de 3 chelines.

Puedes suponer que Nicola tiene acceso a un número infinito de monedas de cada denominación.
(Tiene una cuenta bancaria grande y acceso a un cajero automático).

Entrada: Dos argumentos. El primer argumento es un int: el precio de la compra. El segundo es
una lista de ints: las denominaciones de las monedas disponibles.

Salida: int. El número mínimo de monedas que Nicola puede utilizar para realizar la compra. Si
el precio no se puede realizar con las denominaciones disponibles, devuelve None .

Ejemplo:
checkio(8, [1, 3, 5]) == 2
checkio(12, [1, 4, 5]) == 3

Cómo se utiliza: Además de ayudar a Nicola a hacer el cambio, es un ejemplo de problema de
optimización combinatoria.

Precondición: Las entradas son todas números enteros positivos.
"""


def checkio(price, denominations):
    """
    return the minimum number of coins that add up to the price
    """
    # Create a list to store the minimum number of coins for each price
    dp = [float("inf")] * (price + 1)
    dp[0] = 0

    # Loop through each coin denomination and update the dp list
    for coin in denominations:
        for i in range(coin, price + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If the last element in dp remains infinity, it means the price cannot be made
    if dp[price] == float("inf"):
        return None

    return dp[price]


if __name__ == "__main__":
    print("Example:")
    print(checkio(8, [1, 3, 5]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(8, [1, 3, 5]) == 2
    assert checkio(12, [1, 4, 5]) == 3
    print("Done")
