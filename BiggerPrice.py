'''
You have a list with all available products in a store. The data is represented as a list of dicts

Your mission here is to find the most expensive products in the list. The number of products we are
looking for will be given as the first argument and the list of all products as the second argument.

Input: int and list of dicts. Each dict has the two keys "name" and "price"

Output: The same format as the second input argument.

Example:
assert bigger_price(
    2,
    [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1},
    ],
) == [{"name": "wine", "price": 138}, {"name": "bread", "price": 100}]
assert bigger_price(
    1, [{"name": "pen", "price": 5}, {"name": "whiteboard", "price": 170}]
) == [{"name": "whiteboard", "price": 170}]

----------
----------

Se tiene una lista con todos los productos disponibles en una tienda. Los datos se representan como una lista de dicts

Tu misión aquí es encontrar los productos más caros de la lista. El número de productos que buscamos se dará como
primer argumento y la lista de todos los productos como segundo argumento.

Entrada: int y lista de dicts. Cada dict tiene las dos claves "nombre" y "precio"

Salida: El mismo formato que el segundo argumento de entrada.

Ejemplo:

assert mayor_precio(
    2,
    [
        {"nombre": "pan", "precio": 100},
        {"nombre": "vino", "precio": 138},
        {"nombre": "carne", "precio": 15},
        {"nombre": "agua", "precio": 1},
    ],
) == [{"nombre": "vino", "precio": 138}, {"nombre": "pan", "precio": 100}]
assert mayor_precio(
    1, [{"nombre": "bolígrafo", "precio": 5}, {"nombre": "pizarra", "precio": 170}]
) == [{"nombre": "pizarra", "precio": 170}]

Traducción realizada con la versión gratuita del traductor www.DeepL.com/Translator
'''


def bigger_price(limit: int, data: list[dict]) -> list[dict]:
    """
    TOP most expensive goods
    """
    # your code here
    return sorted(data, key=lambda x: x['price'], reverse=True)[:limit]


print("Example:")
print(
    bigger_price(
        2,
        [
            {"name": "bread", "price": 100},
            {"name": "wine", "price": 138},
            {"name": "meat", "price": 15},
            {"name": "water", "price": 1},
        ],
    )
)

assert bigger_price(
    2,
    [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1},
    ],
) == [{"name": "wine", "price": 138}, {"name": "bread", "price": 100}]
assert bigger_price(
    1, [{"name": "pen", "price": 5}, {"name": "whiteboard", "price": 170}]
) == [{"name": "whiteboard", "price": 170}]

print("The mission is done! Click 'Check Solution' to earn rewards!")
