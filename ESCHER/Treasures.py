'''
The vault turned out to have a quite gratifying content, and unlike the current paper currencies, the
truly valuable things used to be made of gold and silver. On top of that, there were precious stones,
jewelry, and many other valuable items. You wanted so badly to take everything, but, unfortunately,
your crew has died, and by yourself you could carry only a part of the treasure. Well, let it be the
most valuable part then!
As input you'll receive the information about the vault contents in the following format: {'golden
coin': {'price': 100, 'weight': 50, 'amount': 200}, 'silver coin': {'price': 10, 'weight': 20, 'amount':
1000} , 'ruby': {'price': 1000, 'weight': 200, 'amount': 2}}, where price is measured in the standard
units of your country's currency, weight is measured in grams, and amount is measured in pieces.
In addition, you'll also have a weight limit (in kilograms), over which you won't be able to carry.

Your task is to collect such a set of treasures so that their total weight doesn't exceed the limit,
and their total cost was as high as possible. The answer must be returned as the list of strings, for
example: ['golden coin: 150', 'silver coin: 700', 'ruby: 2']. There always be 3 types of the treasures
(golden coin, silver coin and ruby) and it should be represent in the answer in the same order. If some
type of the treasures are out of limit (so you 'can' take it 0) - just don't include it into answer.

Input: Dictionary with information about treasures and weight limit.

Output: All treasures, which you take (a list of strings).

Example:
treasures({'golden coin':
              {'price': 100, 'weight': 50, 'amount': 200},
           'silver coin':
              {'price': 10, 'weight': 20, 'amount': 1000},
           'ruby':
              {'price': 1000, 'weight': 200, 'amount': 2}}, 5) == [
               'golden coin: 92', 'ruby: 2']

How it is used: For finding the optimal set of the objects.

Precondition :
3 types of treasures

----------
----------

La cámara acorazada resultó tener un contenido bastante gratificante y, a diferencia de las monedas de
papel actuales, las cosas verdaderamente valiosas solían estar hechas de oro y plata. Además, había
piedras preciosas, joyas y muchos otros objetos de valor. Tenías tantas ganas de llevártelo todo, pero,
por desgracia, tu tripulación ha muerto, y tú solo sólo podías cargar con una parte del tesoro. Pues bien,
¡que sea la parte más valiosa!
Como entrada recibirás la información sobre el contenido de la bóveda en el siguiente formato: {'moneda
de oro': {'precio': 100, 'peso': 50, 'cantidad': 200}, 'moneda de plata': {"precio": 10, 'peso': 20,
'cantidad': 1000} , 'rubí': {'precio': 1000, 'peso': 200, 'cantidad': 2}}, donde el precio se mide en
las unidades estándar de la moneda de su país, el peso se mide en gramos y la cantidad se mide en piezas.
Además, también tendrás un límite de peso (en kilogramos), por encima del cual no podrás cargar.

Tu tarea consiste en reunir tal conjunto de tesoros de modo que su peso total no supere el límite, y su
coste total sea el máximo posible. La respuesta debe ser devuelta como la lista de cadenas, por ejemplo:
['moneda de oro: 150', 'moneda de plata: 700', 'rubí: 2']. Siempre hay 3 tipos de tesoros (moneda de oro,
moneda de plata y rubí) y deben estar representados en la respuesta en el mismo orden. Si algún tipo de
tesoro está fuera del límite (por lo que "puedes" cogerlo 0), no lo incluyas en la respuesta.

Entrada: Diccionario con información sobre tesoros y límite de peso.

Salida: Todos los tesoros que has cogido (una lista de cadenas).

Ejemplo:
tesoros({'moneda de oro':
              {'precio': 100, 'peso': 50, 'cantidad': 200},
           'moneda de plata':
              {'precio': 10, 'peso': 20, 'cantidad': 1000},
           'rubí':
              {'precio': 1000, 'peso': 200, 'cantidad': 2}}, 5) == [
               'moneda de oro: 92', 'rubí: 2']

Cómo se utiliza: Para encontrar el conjunto óptimo de los objetos.

Condición previa :
3 tipos de tesoros
'''


import numpy as np
from math import gcd


def treasures(info, limit):
    #replace this for solution
    l = int(limit * 1000)
    g = [info['golden coin']['price'], info['golden coin']['weight'], info['golden coin']['amount']]
    s = [info['silver coin']['price'], info['silver coin']['weight'], info['silver coin']['amount']]
    r = [info['ruby']['price'], info['ruby']['weight'], info['ruby']['amount']]

    d = l
    for i in (g, s, r):
        d = gcd(d, i[1])
    l = int(l / d)
    g[1] = int(g[1] / d)
    s[1] = int(s[1] / d)
    r[1] = int(r[1] / d)

    result = np.zeros((g[2] + s[2] + r[2], l + 1, 4), dtype=int)
    for i in range(l + 1):
        if i >= g[1]:
            result[(0, i, 0)] = g[0]
            result[(0, i, 1)] = 1

    for i in range(1, g[2]):
        for j in range(1, l + 1):
            if j < g[1]:
                result[(i, j)] = result[(i - 1, j)]
            elif result[(i - 1, j, 0)] < result[(i - 1, j - g[1], 0)] + g[0]:
                result[(i, j)] = result[(i - 1, j - g[1])]
                result[(i, j, 0)] += g[0]
                result[(i, j, 1)] += 1
            else:
                result[(i, j)] = result[(i - 1, j)]

    for i in range(g[2], g[2] + s[2]):
        for j in range(1, l + 1):
            if j < s[1]:
                result[(i, j)] = result[(i - 1, j)]
            elif result[(i - 1, j, 0)] < result[(i - 1, j - s[1], 0)] + s[0]:
                result[(i, j)] = result[(i - 1, j - s[1])]
                result[(i, j, 0)] += s[0]
                result[(i, j, 2)] += 1
            else:
                result[(i, j)] = result[(i - 1, j)]

    for i in range(g[2] + s[2], g[2] + s[2] + r[2]):
        for j in range(1, l + 1):
            if j < r[1]:
                result[(i, j)] = result[(i - 1, j)]
            elif result[(i - 1, j, 0)] < result[(i - 1, j - r[1], 0)] + r[0]:
                result[(i, j)] = result[(i - 1, j - r[1])]
                result[(i, j, 0)] += r[0]
                result[(i, j, 3)] += 1
            else:
                result[(i, j)] = result[(i - 1, j)]

    n1 = result[(-1, -1, 1)]
    n2 = result[(-1, -1, 2)]
    n3 = result[(-1, -1, 3)]

    result_list = []
    if n1:
        result_list.append('golden coin: ' + str(n1))
    if n2:
        result_list.append('silver coin: ' + str(n2))
    if n3:
        result_list.append('ruby: ' + str(n3))

    return result_list


if __name__ == '__main__':
    print("Example:")
    print(treasures({'golden coin':
                        {'price': 100, 'weight': 50, 'amount': 200},
                     'silver coin':
                        {'price': 10, 'weight': 20, 'amount': 1000},
                     'ruby':
                        {'price': 1000, 'weight': 200, 'amount': 2}}, 5))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert treasures({'golden coin':
                         {'price': 100, 'weight': 50, 'amount': 200},
                      'silver coin':
                         {'price': 10, 'weight': 20, 'amount': 1000},
                      'ruby':
                         {'price': 1000, 'weight': 200, 'amount': 2}}, 5) == [
                          'golden coin: 92', 'ruby: 2']
    assert treasures({'golden coin':
                         {'price': 100, 'weight': 50, 'amount': 100},
                      'silver coin':
                         {'price': 10, 'weight': 20, 'amount': 100},
                      'ruby':
                         {'price': 1000, 'weight': 200, 'amount': 1}}, 7.5) == [
                          'golden coin: 100', 'silver coin: 100', 'ruby: 1']
    print("Coding complete? Click 'Check' to earn cool rewards!")
