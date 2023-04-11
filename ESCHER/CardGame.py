'''
It seems that the Hypercube affects this place in a very strange way - for example, it’s not letting
the two spirits of treasure hunters to rest in peace until they figure out who between the two of them
is a winner of some weird game. Hm, what would've happened if you’d refused to finish an already started game?..

Nevertheless, you’ve had neither the time nor the inclination to think about that and you went further.
In less than a few minutes you saw something you’d rather not see - a real god damn ghost! Judging by the
similarity between the ghost and the portrait of a man hanging in a recently visited room, it’s safe to assume
that this is the Lord Escher himself. It has become increasingly clear why none of the treasure hunters returned
from the island for so many years. There’s no going back now, so it seems like you’ll have to come to an
agreement with him one way or the other.

"Only the one who can tell the truth from a lie will pass!". These were the first words the ghost said, when he
saw you. He pointed to a lying on the floor set of double-sided cards which had the numbers written on them.
Maybe these cards also belonged to one of the previous visitors of the castle, and then Lord Escher just decided
to use them as a tryout for the seekers? Well, it doesn’t matter now. In order to pass you need to determine
whether among the several first cards there are the ones that doesn’t belong.
In this mission will be used a special deck of double-sided cards which had the numbers written on them - one
number per one side of the card. The numbers on the cards are written according to the following principle: the
first card has 0 and 1, the second - 1 and 2, ..., the n-th - (n-1) and n. The cards in this set are shuffled
chaotically.

As input your function receives the total number of cards and a list of numbers which have been seen on the
alternately taken N cards, noting that you are looking only at the front side of the card. Your task is to
determine whether the cards that you’ve seen are a part of this set or the cards from some other deck have
accidentally got mixed up. Depending on the answer, return True (if all the viewed cards can be encountered
only within one deck) or False (if otherwise).

Input: Deck size, list of the picked cards.

Output: True or False.

Example:
cards(5, [2, 0, 1, 2]) == False
cards(10, [9, 9, 6, 6]) == True
cards(10, [11]) == False

How it is used: For the game analisys.

Precondition :
3 <= deck size <= 100

----------
----------

Parece que el Hipercubo afecta a este lugar de una forma muy extraña - por ejemplo, no deja descansar en
paz a los dos espíritus de los buscadores de tesoros hasta que descubran quién de los dos es el ganador de
algún extraño juego. Hm, ¿qué hubiera pasado si te hubieras negado a terminar una partida ya empezada?...

Sin embargo, no has tenido ni tiempo ni ganas de pensar en eso y has seguido adelante. En menos de unos
minutos has visto algo que preferirías no ver: ¡un maldito fantasma de verdad! A juzgar por la similitud
entre el fantasma y el retrato de un hombre que cuelga en una habitación recién visitada, es seguro suponer
que se trata del mismísimo Lord Escher. Cada vez está más claro por qué ninguno de los cazadores de tesoros
regresó de la isla durante tantos años. Ya no hay vuelta atrás, así que parece que tendrás que llegar a un
acuerdo con él de una forma u otra.

"¡Sólo pasará el que sepa distinguir la verdad de la mentira!". Estas fueron las primeras palabras que dijo
el fantasma cuando te vio. Señaló unas cartas de doble cara que estaban en el suelo y que tenían los números
escritos. ¿Quizás estas cartas también pertenecieron a uno de los visitantes anteriores del castillo, y entonces
Lord Escher simplemente decidió usarlas como prueba para los buscadores? Bueno, ahora no importa. Para pasar
necesitas determinar si entre las varias primeras cartas hay alguna que no pertenezca.
En esta misión se estará utilizando una baraja especial de cartas de doble cara que tienen los números escritos
en ellas - un número por cada cara de la carta. Los números de las cartas están escritos según el siguiente
principio: la primera carta tiene 0 y 1, la segunda - 1 y 2, ..., la n-ésima - (n-1) y n. Las cartas de este
juego se barajan caóticamente.

Como entrada tu función recibe el número total de cartas y una lista de números que se han visto en las N
cartas tomadas alternativamente, teniendo en cuenta que estás mirando sólo el anverso de la carta. Su tarea
es determinar si las cartas que ha visto forman parte de este conjunto o se han mezclado accidentalmente las
cartas de alguna otra baraja. Dependiendo de la respuesta, devuelve Verdadero (si todas las cartas vistas sólo
se pueden encontrar dentro de una baraja) o Falso (en caso contrario).

Entrada: Tamaño de la baraja, lista de las cartas elegidas.

Salida: Verdadero o Falso.

Ejemplo:
cartas(5, [2, 0, 1, 2]) == Falso
cards(10, [9, 9, 6, 6]) == True
cards(10, [11]) == Falso

Cómo se utiliza: Para el análisis del juego.

Precondición :
3 <= tamaño de la baraja <= 100
'''


def cards(deck, hand):
    #replace this for solution
    deck = {i for i in range(deck)}
    hand = sorted(hand)
    for card in hand:
        if card - 1 in deck:
            deck.discard(card - 1)
        elif card in deck:
            deck.discard(card)
        else:
            return False
    return True


if __name__ == '__main__':
    print("Example:")
    print(cards(5, [2, 0, 1, 2]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert cards(5, [2, 0, 1, 2]) == False
    assert cards(10, [9, 9, 6, 6]) == True
    assert cards(10, [11]) == False
    assert cards(3, [0, 1, 1]) == False
    assert cards(10, [3, 3, 5, 6, 6, 7]) == True
    assert cards(8, [4, 4, 5, 6, 7]) == True
    assert cards(7, [4, 4, 5, 6, 7]) == False
    assert cards(4, [0, 0]) == False
    assert cards(4, [2, 2]) == True
    assert cards(4, [4, 4]) == False
    assert cards(4, [2, 2, 2]) == False
    assert cards(4, [1, 1, 2, 2]) == False
    assert cards(4, [2, 2, 3, 3]) == False
    assert cards(4, [0, 1, 2, 3, 3]) == False
    assert cards(4, [1, 1, 2, 3, 4]) == False
    assert cards(4, [0, 1, 2, 3, 4]) == False
    assert cards(4, [1, 1, 2, 3, 3]) == False
    assert cards(10, [1, 1, 2, 3, 4, 5, 6, 7, 7]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
