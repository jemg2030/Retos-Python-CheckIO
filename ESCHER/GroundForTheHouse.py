'''
It was a long trip to the island, so you’ve decided to pass the time sitting in the captain's
cabin and splitting the treasures remained to be found. Aside from that, a couple of weeks
before you left for the expedition, you’ve managed to negotiate with several very wealthy
people and approximately knew how much you could get by selling the Hypercube.

Purchasing land in a picturesque place have been one of your long-held wishes. You’ve dreamed
of building a house there and breeding the rare species. All of this requires a considerable
amount of money that are likely to come into your possession in the near future.
As the input data you will get the multiline string consists of '0' & '#'. where '0' means
the empty piece of the ground and the '#' is the piece of your house. Your task is to count
the minimal area of the rectangle ground which is enough for the building.

Input: The plan of the house.

Output: The total area of the rectangle piece of the ground.

Example:
house('''
0000000
##00##0
######0
##00##0
#0000#0
''') == 24

How it is used: For the rational use of the resources.

Precondition :
2x2 <= multiline string <= 10x10

----------
----------

El viaje a la isla fue largo, así que decidiste pasar el tiempo sentado en el camarote del 
capitán repartiéndote los tesoros que quedaban por encontrar. Aparte de eso, un par de 
semanas antes de partir para la expedición, has conseguido negociar con varias personas 
muy adineradas y aproximadamente sabías cuánto podrías conseguir vendiendo el Hipercubo.

Comprar un terreno en un lugar pintoresco ha sido uno de tus deseos desde hace mucho tiempo. 
Has soñado con construir allí una casa y criar especies raras. Todo ello requiere una cantidad 
considerable de dinero que probablemente llegará a tus manos en un futuro próximo.
Como datos de entrada obtendrás la cadena multilínea formada por '0' & '#'. donde '0' significa 
el trozo de terreno vacío y el '#' es el trozo de tu casa. Tu tarea es contar el área mínima del 
rectángulo de terreno que es suficiente para el edificio.

Entrada: El plano de la casa.

Salida: El área total del rectángulo del terreno.

Ejemplo:
casa('''
0000000
##00##0
######0
##00##0
#0000#0
''') == 24

Cómo se utiliza: Para el uso racional de los recursos.

Precondición :
2x2 <= cadena multilínea <= 10x10

Traducción realizada con la versión gratuita del traductor www.DeepL.com/Translator
'''


def house(plan):
    #replace this for solution
    # Split the input string into lines and remove any leading/trailing whitespace
    lines = plan.strip().split('\n')

    # Find the coordinates of all '#' symbols
    coords = [(i, j) for i, line in enumerate(lines) for j, ch in enumerate(line) if ch == '#']

    # If there are no '#' symbols, the area is 0
    if not coords:
        return 0

    # Find the minimum and maximum x and y values
    min_x = min(x for x, y in coords)
    max_x = max(x for x, y in coords)
    min_y = min(y for x, y in coords)
    max_y = max(y for x, y in coords)

    # Calculate the width and height of the rectangle
    width = max_x - min_x + 1
    height = max_y - min_y + 1

    # Return the area of the rectangle
    return width * height

if __name__ == '__main__':
    print("Example:")
    print(house('''
0000000
##00##0
######0
##00##0
#0000#0
'''))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert house('''
0000000
##00##0
######0
##00##0
#0000#0
''') == 24

    assert house('''0000000000
#000##000#
##########
##000000##
0000000000
''') == 30

    assert house('''0000
0000
#000
''') == 1

    assert house('''0000
0000
''') == 0

    assert house('''
0##0
0000
#00#
''') == 12

    print("Coding complete? Click 'Check' to earn cool rewards!")
