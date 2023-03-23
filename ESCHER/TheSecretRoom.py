'''
Here you are in the castle. Despite the fact that it’s already about 200 years old, it doesn’t look
like an ancient ruin at all. In the great hall (of a very odd geometrical form) you’re seeing the
following: - a beautiful spiral staircase leading to the 2nd floor; - an equally attractive staircase
that leads into the dungeon; - a lot of doors of a wide variety of different shapes, colors and designs.
Having decided to explore the doors on this floor first, you’ve assumed that the most interesting things
should be in the very last room. However, finding it won’t be as easy as it seems.

Before going on this trip, you’ve gathered some information about the Lord Escher's quirks. One of them
was a very unusual numbering of doors - he numbered them according to how the numbers go in the alphabetical
order. For example, if there were five doors positioned from left to right, they were numbered as: five, four,
one, three, two (instead of a completely logical numeration - 1, 2, 3, 4, 5). Thus, the very last door was actually
the leftmost, not the very right one, as it might be assumed. Your task is to find the very last door.
As input your function will receive an integer - the total number of doors in the current room. You will need to
sort the door numbers in the order in which these numbers, expressed in words, go in the alphabetical order. And
then return the position number of the last door (the door with the highest number). The count starts from the 1st
position (not from the 0th). The maximum number of doors is 1000. The numbers after 100 are written in the format
like - 'one hundred twenty nine'.

Input: the door number.

Output: the 'right' door number.

Example:
secret_room(5) == 1, #five, four, one, three, two
secret_room(3) == 2, #one, three, two
secret_room(1000) == 551

How it is used: For the work with numbers in their alphabetical representation.

Precondition :
2 <= amount of the doors <= 1000

----------
----------

Aquí estás en el castillo. A pesar de que ya tiene unos 200 años, no parece en absoluto una ruina
antigua. En el gran vestíbulo (de una forma geométrica muy extraña) verás lo siguiente - una bonita
escalera de caracol que lleva al 2º piso; - una escalera igualmente atractiva que lleva a la mazmorra; -
un montón de puertas de una gran variedad de formas, colores y diseños diferentes. Habiendo decidido
explorar primero las puertas de esta planta, has supuesto que lo más interesante debería estar en la
última habitación. Sin embargo, encontrarlo no será tan fácil como parece.

Antes de emprender este viaje, has reunido información sobre las peculiaridades de Lord Escher. Una
de ellas era una numeración muy inusual de las puertas: las numeraba según el orden alfabético de los
números. Por ejemplo, si había cinco puertas colocadas de izquierda a derecha, se numeraban como: cinco,
cuatro, uno, tres, dos (en lugar de una numeración completamente lógica: 1, 2, 3, 4, 5). Por lo tanto, la
última puerta era en realidad la más a la izquierda, no la más a la derecha, como podría suponerse. Su tarea
consiste en encontrar la última puerta.
Como entrada, la función recibirá un número entero: el número total de puertas de la sala actual. Tendrás que
ordenar los números de las puertas en el orden en que estos números, expresados en palabras, van en el orden
alfabético. Y luego devolver el número de posición de la última puerta (la puerta con el número más alto).
El recuento comienza desde la 1ª posición (no desde la 0ª). El número máximo de puertas es 1000. Los números
después de 100 se escriben en el formato como - 'ciento veintinueve'.

Entrada: el número de puerta.

Salida: el número de puerta 'correcto'.

Ejemplo:
secret_room(5) == 1, #cinco, cuatro, uno, tres, dos
secret_room(3) == 2, #uno, tres, dos
secret_room(1000) == 551

Cómo se utiliza: Para el trabajo con números en su representación alfabética.

Condición previa :
2 <= cantidad de las puertas <= 1000
'''


BELOW_20 = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen'
}

TENS = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

# Precompute English words for numbers up to the given door
english_words = {0: '', 1000: 'one thousand'}
for nb in range(1, 1000):
    if nb < 20:
        english_words[nb] = BELOW_20[nb]
    elif nb < 100:
        tens, below_ten = divmod(nb, 10)
        english_words[nb] = TENS[tens - 2] + ' ' + BELOW_20[below_ten]
    else:
        hundreds, below_hundred = divmod(nb, 100)
        if below_hundred == 0:
            english_words[nb] = BELOW_20[hundreds] + ' hundred'
        else:
            english_words[nb] = BELOW_20[hundreds] + ' hundred and ' + english_words[below_hundred]

def get_english_word(nb):
    return english_words[nb]

def secret_room(number):
    # replace this for solution
    return sum(get_english_word(nb) < get_english_word(number) for nb in range(number))


if __name__ == '__main__':
    print("Example:")
    print(secret_room(5))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert secret_room(5) == 1 #five, four, one, three, two
    assert secret_room(3) == 2 #one, three, two
    assert secret_room(1000) == 551
    print("Coding complete? Click 'Check' to earn cool rewards!")
