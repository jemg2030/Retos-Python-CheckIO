"""
Magician: John, I'm going to blow your mind with a simple magic trick. Choose five cards.
The magician turns around to see nothing.
John: I just picked five cards.
Magician: Bot will tell me four of them and I will guess the fifth one.
Bot: Jack of diamonds, Ace of hearts, Queen of clubs, King of spades.
Magician: I see red, yeah it's of diamonds... And it's not a face... It's even pretty low...
The three of diamonds, right?!
The magician quickly turns around to see John's face...
John: No way!
Magician: Told you!
John: It was just luck, do it again!
Magician: I can do it all day long, dummy.
Well, it's an automatic magic trick, that I will explain in a moment. You will have to
create two functions. A function named bot which will take five cards, an integer and
return four of them ; and a function named magician which will take four cards, the same
integer and return the fifth one.

The trick use the standard 52-card deck . Cards will be represented like 'A ♥' , '3 ♦' ,
'K ♠' , 'Q ♣' , 'J ♦' ( ♣ for clubs, ♦ for diamonds, ♥ for hearts, ♠ for spades, A for Ace,
J for Jack, Q for Queen and K for King).
We will soon need to compare cards. The deck order is A ♣ < A ♦ < A ♥ < A ♠ < 2 ♣ < ... .
To compare two cards, look ranks A < 2 < ... < 10 < J < Q < K , then suits ♣ < ♦ < ♥ < ♠
(same order than with letters: club < diamond < heart < spade ).

The card the bot choose to hide and the order of the four cards the bot says is crucial
for the magician so he can guess the fifth one. There are five cards, but only four suits
so there are at least two cards from the same suit, we name them card A and card B . The
bot will hide one and say the other, but which one? Imagine the thirteen cards in a circle,
clockwise . If going from card A to card B on this circle is quicker than going from card B
to card A , then we will hide card B , say card A , and the distance from card A to card B
is noted as delta (it's necessarily a number between one and six). We still have three cards
to say, and since there are six ways to tell three cards, we can transmit "delta information".
The card A will be the starting point, then by "adding" delta to card A , the magician can "guess"
the fifth card.
Sort the three remaining cards, according to the above order, and note them C1 , C2 and C3 . If
delta is 5 or 6, put C1 first, if delta is 3 or 4, put C2 first, and C3 otherwise. You still have
two cards to say, tell them in order if delta is odd (1, 3, 5), and in reverse order otherwise (2, 4, 6).
At this point, the bot have two things to say: the card A , and a list of three cards. If we repeat
this magic trick multiple times and if we always say the card A first, John might notice it since the
fifth card and card A have the same suit. So we are not going to always tell card A first. The first
time, we will say it first, the second time, say it second, ..., the fifth time, say it first again...

Clockwise wheel of diamondsExample: John chooses A ♥ , 3 ♦ , K ♠ , Q ♣ and J ♦ .
3 ♦ and J ♦ have the same suit, it's quicker to go from J ♦ to 3 ♦ ( delta = 5 ) than otherwise
(8). The starting point is J ♦ and we hide 3 ♦ .
Remains A ♥ , K ♠ and Q ♣ . Sorted, it's A ♥ , Q ♣ and K ♠ . delta = 5 so C1 = A ♥ first, 5 is
odd so the other two in order. So A ♥ , Q ♣ and K ♠ .
Since it's the first time we do the magic trick, then the bot says J ♦ first, then A ♥ , Q ♣ and K ♠ .
The magician hears J ♦ , A ♥ , Q ♣ and K ♠ .
It's the first time he does the magic trick so J ♦ is the starting point. He can say it's of diamonds.
From A ♥ , Q ♣ , K ♠ order, he deduces delta = 5 (since A ♥ < Q ♣ < K ♠ ). So J ♦ + 5 == 3 ♦ .
He says it, with some show.

bot	magician
Input	Five strings and an integer	Four strings and an integer
Output	A list/tuple of four strings	A string

bot('A ♥', '3 ♦', 'K ♠', 'Q ♣', 'J ♦', n=1) == ['J ♦', 'A ♥', 'Q ♣', 'K ♠']
magician('J ♦', 'A ♥', 'Q ♣', 'K ♠', n=1) == '3 ♦'

How it is used: To amaze and impress people with your magic skills.

----------
----------

Mago: John, voy a volar tu mente con un simple truco de magia. Elige cinco cartas.
El mago se da la vuelta y no ve nada.
John: Acabo de elegir cinco cartas.
Mago: Bot me dirá cuatro de ellas y yo adivinaré la quinta.
Bot: Jota de diamantes, As de corazones, Reina de tréboles, Rey de picas.
Mago: Veo rojo, sí es de diamantes... Y no es una cara... Incluso es bastante bajo... ¡¿El tres
de diamantes, verdad?!
El mago se gira rápidamente para ver la cara de John...
John: ¡No puede ser!
Mago: ¡Te lo dije!
John: Ha sido sólo suerte, ¡hazlo otra vez!
Mago: Puedo hacerlo todo el día, tonto.
Bueno, es un truco de magia automático, que te explicaré en un momento. Tendrás que crear dos
funciones. Una función llamada bot que tomará cinco cartas, un número entero y devolverá cuatro
de ellas ; y una función llamada mago que tomará cuatro cartas, el mismo número entero y devolverá
la quinta.

El truco utiliza la baraja estándar de 52 cartas. Las cartas se representarán como 'A ♥' , '3 ♦' ,
'K ♠' , 'Q ♣' , 'J ♦' ( ♣ para tréboles, ♦ para diamantes, ♥ para corazones, ♠ para picas, A para As,
J para Sota, Q para Reina y K para Rey).
Pronto necesitaremos comparar cartas. El orden de la baraja es A ♣ < A ♦ < A ♥ < A ♠ < 2 ♣ < ... .
Para comparar dos cartas, mira los rangos A < 2 < ... < 10 < J < Q < K , luego palos ♣ < ♦ < ♥ < ♠
(mismo orden que con las cartas: trébol < diamante < corazón < pica ).

La carta que el bot elige esconder y el orden de las cuatro cartas que el bot dice es crucial para
que el mago pueda adivinar la quinta. Hay cinco cartas, pero sólo cuatro palos, así que hay al
menos dos cartas del mismo palo, las llamaremos carta A y carta B . El mago esconderá una y dirá
la otra, pero ¿cuál? Imagina las trece cartas en círculo, en el sentido de las agujas del reloj.
Si ir de la carta A a la carta B en este círculo es más rápido que ir de la carta B a la carta A ,
entonces esconderemos la carta B , diremos la carta A , y la distancia de la carta A a la carta B
se anota como delta (es necesariamente un número entre uno y seis). Aún nos quedan tres cartas por
decir, y como hay seis maneras de decir tres cartas, podemos transmitir la "información delta". La
carta A será el punto de partida, luego "añadiendo" delta a la carta A , el mago puede "adivinar"
la quinta carta.
Ordena las tres cartas restantes, según el orden anterior, y anótalas C1 , C2 y C3 . Si delta
es 5 o 6, pon C1 primero, si delta es 3 o 4, pon C2 primero, y C3 en caso contrario. Aún te
quedan dos cartas por decir, dilas en orden si delta es impar (1, 3, 5), y en orden inverso
en caso contrario (2, 4, 6).

En este punto, el bot tiene dos cosas que decir: la carta A , y una lista de tres cartas.
Si repetimos este truco de magia varias veces y si siempre decimos primero la carta A, John
podría darse cuenta, ya que la quinta carta y la carta A tienen el mismo palo. Así que no
vamos a decir siempre primero la carta A. La primera vez, la diremos primero, la segunda vez,
la diremos segundo, ..., la quinta vez, la diremos primero otra vez...

Rueda de diamantes en el sentido de las agujas del relojEjemplo: Juan elige A ♥ , 3 ♦ , K ♠ ,
Q ♣ y J ♦ .
3 ♦ y J ♦ tienen el mismo palo, es más rápido pasar de J ♦ a 3 ♦ ( delta = 5 ) que de otro modo
(8). El punto de partida es J ♦ y ocultamos 3 ♦ .
Queda A ♥ , K ♠ y Q ♣ . Ordenado, es A ♥ , Q ♣ y K ♠ . delta = 5 por lo que C1 = A ♥ primero,
5 es impar por lo que los otros dos en orden. Entonces A ♥ , Q ♣ y K ♠ .
Como es la primera vez que hacemos el truco de magia, entonces el bot dice J ♦ primero, luego
A ♥ , Q ♣ y K ♠ .
El mago oye J ♦ , A ♥ , Q ♣ y K ♠ .
Es la primera vez que hace el truco de magia por lo que J ♦ es el punto de partida. Puede decir
que es de diamantes.
De A ♥ , Q ♣ , K ♠ orden, deduce delta = 5 (ya que A ♥ < Q ♣ < K ♠ ). Entonces J ♦ + 5 == 3 ♦ .
Lo dice, con cierto espectáculo.

mago bot
Entrada Cinco cadenas y un entero Cuatro cadenas y un entero
Salida Una lista/tupla de cuatro cadenas Una cadena

bot('A ♥', '3 ♦', 'K ♠', 'Q ♣', 'J ♦', n=1) == ['J ♦', 'A ♥', 'Q ♣', 'K ♠']
magician('J ♦', 'A ♥', 'Q ♣', 'K ♠', n=1) == '3 ♦'

Cómo se utiliza: Para asombrar e impresionar a la gente con tus habilidades mágicas.
"""


RANKS = tuple("A 2 3 4 5 6 7 8 9 10 J Q K".split())
SUITS = tuple("♣♦♥♠")
keyranks = {key: rank for rank, key in enumerate(RANKS)}
keysuits = {key: suit for suit, key in enumerate(SUITS)}


def choose(cards):
    from itertools import combinations

    for i, j in combinations(cards, 2):
        if i[-1] == j[-1]:
            return (cards.pop(cards.index(i))), (cards.pop(cards.index(j)))


def bot(*cards, n=1):
    """Determine four cards the bot has to say to the magician."""
    # Obviously not always just the first four, put your code here instead.
    cards = list(cards)
    a, b = choose(cards)
    delta = RANKS.index(b[:-2]) - RANKS.index(a[:-2])
    delta = delta + (13 if delta < 0 else 0)
    if delta > 13 - delta:
        delta = 13 - delta
        a, b = b, a
    cards.sort(key=lambda card: (keyranks[card[:-2]], keysuits[card[-1]]))
    i = 2 - (delta - 1) // 2
    cards.insert(0, cards.pop(i))
    cards[1:] = sorted(
        cards[1:],
        key=lambda card: (keyranks[card[:-2]], keysuits[card[-1]]),
        reverse=(delta % 2 == 0),
    )
    cards.insert((n - 1) % 4, a)
    return cards


def magician(*cards, n=1):
    """Determine the fifth card with only four cards."""
    # Obviously not a random card, put your code here instead.
    cards = list(cards)
    # remove and save "a" card
    a = cards.pop((n - 1) % 4)
    # index of the card that shoul be first
    first = sorted(
        cards, key=lambda card: (keyranks[card[:-2]], keysuits[card[-1]])
    ).index(cards[0])
    cards.pop(0)
    # index that shows odd or even number
    odd = sorted(
        cards, key=lambda card: (keyranks[card[:-2]], keysuits[card[-1]])
    ).index(cards[0])
    delta = 5 - 2 * first + odd
    return RANKS[RANKS.index(a[:-2]) - 13 + delta] + " " + a[-1]


if __name__ == "__main__":
    assert list(bot("A ♥", "3 ♦", "K ♠", "Q ♣", "J ♦")) == ["J ♦", "A ♥", "Q ♣", "K ♠"]
    assert magician("J ♦", "A ♥", "Q ♣", "K ♠") == "3 ♦"

    assert list(bot("10 ♦", "J ♣", "Q ♠", "K ♥", "7 ♦", n=2)) == [
        "Q ♠",
        "7 ♦",
        "J ♣",
        "K ♥",
    ]
    assert magician("Q ♠", "7 ♦", "J ♣", "K ♥", n=2) == "10 ♦"
