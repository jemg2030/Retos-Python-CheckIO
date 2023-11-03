"""
You are given the current stock prices. You have to find out which stocks cost more.

Input: The dictionary where the market identifier code is a key and the value is a stock price.

Output: The market identifier code (ticker symbol) as a string.

Example:
assert best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}) == "ATX"
assert best_stock({"CAC": 91.1, "ATX": 1.01, "TASI": 120.9}) == "TASI"

Preconditions: All the prices are unique.

----------
----------

Se le dan los precios actuales de las acciones. Tienes que averiguar qué acciones cuestan más.

Entrada: El diccionario donde el código identificador del mercado es una clave y el valor
es el precio de una acción.

Salida: El código identificador del mercado (símbolo del ticker) como cadena.

Ejemplo:
assert mejor_acción({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}) == "ATX"
assert mejor_acción({"CAC": 91,1, "ATX": 1,01, "TASI": 120,9}) == "TASI"

Precondiciones: Todos los precios son únicos.
"""


def best_stock(data: dict[str, float]) -> str:
    # your code here
    return max(data, key=data.get)


print("Example:")
print(best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}))

assert best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}) == "ATX"
assert best_stock({"CAC": 91.1, "ATX": 1.01, "TASI": 120.9}) == "TASI"

print("The mission is done! Click 'Check Solution' to earn rewards!")
