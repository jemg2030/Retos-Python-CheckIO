'''
There are few things that are so unpardonably neglected in our country as poker. The upper
class knows very little about poker. Now and then you find ambassadors who have sort of a
general knowledge of poker, but the ignorance of the people is fearful. Why, I have known
clergymen, good men, kind-hearted, liberal, sincere, and all that, who did not know the
meaning of a "flush". It is enough to make one ashamed of the species.
-- Mark Twain
Texas hold'em is a variation of the standard card game of poker. Two cards (hole cards) are
dealt face down to each player and then five community cards are placed face-up by the dealer.
And when all openings we need to define what is the combination a player have.

You are given a sequence of 7 cards and you should choose the best hand (5 cards) in it. Card
sequence are described as a string, where each card are defined by two character - rank and suit.
Cards separated by commas.

The descending ranks are: "A" (Ace), "K" (King), "Q" (Queen), "J" (Jack), "T" (Ten), and "9" to "2".
The descending suits are "h" (hearts), "d" (diamonds), "c" (clubs), "s" (spades).

Texas holdem uses the classical poker hand list : Straight flush, Four of a kind, Full house, Flush,
Straight, Three of a kind, Two Pair, One Pair and High card.

Because of the presence of community cards in Texas hold 'em, different players' hands can often come
very close in value. As a result, it is common for kickers to be used to determine the winning hand for
cases where two or more hands tie. A kicker is a card which is part of the five-card poker hand, but is
not used in determining a hand's rank. For instance, in the hand A-A-A-K-Q, the king and queen are kickers.

In our version of Texas Hold'em cards of differing suits have different values. This means that there is
only ever one best five-card hand to return. So "Td" is higher than "Tc", but lower then "Jc".

Your goal is to choose the best hand with 5 cards and return them as a string, where cards are
separated by commas and ordering from the highest to lowest value. For example: We have two pair
by queens (heart and spades) and eights (diamonds and clubs) and nine heart as a kicker. The result:
"Qh,Qs,9h,8d,8c". Be careful with order.

Input: A list of cards as a string.

Output: The best hand as a string.

Example:
texas_referee("Kh,Qh,Ah,9s,2c,Th,Jh") == "Ah,Kh,Qh,Jh,Th"
texas_referee("Qd,Ad,9d,8d,Td,Jd,7d") == "Qd,Jd,Td,9d,8d",

How it is used: This concept is a good example of combinatorial optimisation process, and
could come in handy should you make a poker game in Python.

Precondition:

cards_quantity == 7
All cards correct and unique.

----------
----------

Hay pocas cosas tan imperdonablemente descuidadas en nuestro país como el póquer.
La clase alta sabe muy poco de póquer. De vez en cuando encuentras embajadores que
tienen una especie de conocimiento general del póquer, pero la ignorancia de la
gente es temible. He conocido a clérigos, hombres buenos, de buen corazón, liberales,
sinceros y todo eso, que no sabían lo que significaba una "escalera de color". Es
suficiente para avergonzarse de la especie.
-- Mark Twain
El Texas hold'em es una variante del póquer. Se reparten dos cartas (cartas ocultas)
boca abajo a cada jugador y, a continuación, el crupier coloca cinco cartas comunitarias
boca arriba. Y cuando todo se abre hay que definir cuál es la combinación que tiene un jugador.

Se le da una secuencia de 7 cartas y debe elegir la mejor mano (5 cartas) en ella. La secuencia
de cartas se describe como una cadena, donde cada carta se define por dos caracteres - rango
y palo. Las cartas están separadas por comas.

Los rangos descendentes son: "A" (As), "K" (Rey), "Q" (Reina), "J" (Jota), "T" (Diez), y del
"9" al "2".
Los palos descendentes son "h" (corazones), "d" (diamantes), "c" (tréboles), "s" (picas).

El Texas holdem utiliza la clásica lista de manos de póquer: escalera de color, cuádruple, full,
color, escalera, trío, dos parejas, una pareja y carta alta.

Debido a la presencia de cartas comunitarias en el Texas hold 'em, las manos de diferentes jugadores
pueden a menudo acercarse mucho en valor. Como resultado, es común que se utilicen kickers para
determinar la mano ganadora en los casos en los que dos o más manos empatan. Un kicker es una carta
que forma parte de la mano de póquer de cinco cartas, pero que no se utiliza para determinar el rango
de una mano. Por ejemplo, en la mano A-A-A-K-Q, el rey y la reina son kickers.

En nuestra versión del Texas Hold'em, las cartas de palos diferentes tienen valores diferentes. Esto
significa que sólo hay una mejor mano de cinco cartas para devolver. Así que "Td" es más alta que "Tc",
pero más baja que "Jc".

Su objetivo es elegir la mejor mano con 5 cartas y devolverlas como una cadena, donde las cartas están
separadas por comas y ordenadas de mayor a menor valor. Por ejemplo: Tenemos dos pares por reinas
(corazón y picas) y ochos (diamantes y tréboles) y nueve corazones como kicker. El resultado:
"Qh,Qs,9h,8d,8c". Cuidado con el orden.

Entrada: Una lista de cartas en forma de cadena.

Salida: La mejor mano como cadena.

Ejemplo:
texas_referee("Kh,Qh,Ah,9s,2c,Th,Jh") == "Ah,Kh,Qh,Jh,Th"
texas_referee("Qd,Ad,9d,8d,Td,Jd,7d") == "Qd,Jd,Td,9d,8d",

Cómo se utiliza: Este concepto es un buen ejemplo de proceso de optimización combinatoria, y podría
resultarte útil si haces un juego de póquer en Python.

Precondición:
cantidad_cartas == 7
Todas las cartas son correctas y únicas.
'''


RANKS = "AKQJT98765432"
SUITS = "hdcs"
KEY = lambda c: RANKS.find(c[0])*len(SUITS) + SUITS.find(c[1])


def get_straight_flush(cards):
    for c in sorted(cards, key=KEY):
        ci = RANKS.find(c[0])
        if ci + 5 > len(RANKS):
            return None
        for i in range(1, 5):
            if (RANKS[ci + i] + c[1]) not in cards:
                break
        else:
            return [RANKS[ci + i] + c[1] for i in range(5)]
    else:
        return None


def get_same_kinds(a, cards):
    results = []
    for n in a:
        for r in sorted(set(c[0] for c in cards), key=lambda c: RANKS.find(c)):
            same_kind = list(filter(lambda c: c[0] == r, cards))
            if len(same_kind) == n:
                results += same_kind
                cards = list(filter(lambda c: c not in same_kind, cards))
                break
        else:
            return None
    return results + sorted(cards, key=KEY)[:5-len(results)]


def get_flush(cards):
    for s in SUITS:
        same_suit = list(filter(lambda c: c[1] == s, cards))
        if len(same_suit) == 5:
            return same_suit
    return None


def get_straight(cards):
    cards = sorted(cards, key=KEY)
    ranks = "".join(map(lambda c: c[0], cards))
    for i in range(len(RANKS)-5):
        results = []
        ri = 0
        for r in RANKS[i:i+5]:
            ri = ranks.find(r, ri)
            if ri < 0:
                break
            results.append(cards[ri])
        else:
            return results
    return None


def get_high_card(cards):
    return sorted(cards, key=KEY)[:5]


PREDICATES = [get_straight_flush,
              [4],
              [3, 2],
              get_flush,
              get_straight,
              [3],
              [2, 2],
              [2],
              get_high_card]


def texas_referee(cards_str):
    global results
    cards = cards_str.split(",")
    for predicate in PREDICATES:
        if isinstance(predicate, list):
            results = get_same_kinds(predicate, cards)
        else:
            results = predicate(cards)
        if results:
            break
    return ",".join(sorted(results, key=KEY)[:5])


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert texas_referee("Kh,Qh,Ah,9s,2c,Th,Jh") == "Ah,Kh,Qh,Jh,Th", "High Straight Flush"
    assert texas_referee("Qd,Ad,9d,8d,Td,Jd,7d") == "Qd,Jd,Td,9d,8d", "Straight Flush"
    assert texas_referee("5c,7h,7d,9s,9c,8h,6d") == "9c,8h,7h,6d,5c", "Straight"
    assert texas_referee("Ts,2h,2d,3s,Td,3c,Th") == "Th,Td,Ts,3c,3s", "Full House"
    assert texas_referee("Jh,Js,9h,Jd,Th,8h,Td") == "Jh,Jd,Js,Th,Td", "Full House vs Flush"
    assert texas_referee("Js,Td,8d,9s,7d,2d,4d") == "Td,8d,7d,4d,2d", "Flush"
    assert texas_referee("Ts,2h,Tc,3s,Td,3c,Th") == "Th,Td,Tc,Ts,3c", "Four of Kind"
    assert texas_referee("Ks,9h,Th,Jh,Kd,Kh,8s") == "Kh,Kd,Ks,Jh,Th", "Three of Kind"
    assert texas_referee("2c,3s,4s,5s,7s,2d,7h") == "7h,7s,5s,2d,2c", "Two Pairs"
    assert texas_referee("2s,3s,4s,5s,2d,7h,8h") == "8h,7h,5s,2d,2s", "One Pair"
    assert texas_referee("3h,4h,Th,6s,Ad,Jc,2h") == "Ad,Jc,Th,6s,4h", "High Cards"
