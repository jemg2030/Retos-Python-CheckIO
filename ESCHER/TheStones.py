'''
Your backpack with all of the equipment and treasures got real heavy, but you welcomed this burden - with
this money you'll be able to compensate for the broken ships and celebrate the successfulness of the
expedition. Of course, for this you first need to get home, but your gut has been telling you that you are
gonna make it.

After leaving the room with a vault, you've headed toward the dungeon. What you've seen next, turned down your
optimism a few notches - the two skeletons laid right behind the entrance to the dungeon. Everything in their
appearance indicated that they were the treasure hunters and, judging by the pallor of the bones sticking out
of the pants and sleeves, they have laid here for many years. But how did they die?

"Сlick ..." - a barely audible sound of the dungeon door closing. You immediately rushed to it, but it was too
late. Of course, it has no keyhole, and no other suggestions that it can be opened, for that matter. You tried
to kick it down but it was too strong. Well, if you aren't planning to keep company to those two skeletons and
starve to death, you have no choice but to find a way out. Perhaps you can find something useful near the
skeletons - they should be examined more closely.

Approaching them, you've heard a voice coming out of nowhere: "... finish ... the game ...". There were only
three options: either there was someone alive in the castle, or these were the ghosts that haunted it, or
you've started to lose your mind and it was the first hallucination. Nope of those options has been too
encouraging, but there were no way back. Finish the game and keep looking for Hypercube.
You most likely know the game where two players are in turn taking from a pile from 1 to 3 stones, and loses
the one who took the last stone. We'll slightly generalize this task. Let's assume that both players can take
not 1, 2, 3 stones, but k1, k2, …, km of stones. Here we are interested which player wins under the right
circumstances (the game played properly and both players use the best strategy).
As the input you will get the number of stones in the pile at the beginning of the game and an amounts of
stones you can take from pile at each move. For example - (10, [1, 2, 3]).
If the current amount of the stones in the pile is lower than lowest number in the "moves" list or equal to
it - current player takes them all and lose.

Input: An amount of the rocks in the pile and the numbers you can take from it.

Output: Winner's number (1 or 2)

Example:
stones(17, [1, 3, 4]) == 2
stones(17, [1, 3, 4, 6, 9]) == 1

How it is used: For the game AI development.

Precondition :
2 players - 1 winner

----------
----------

Tu mochila con todo el equipo y los tesoros se ha vuelto realmente pesada, pero has acogido con
satisfacción esta carga: con este dinero podrás compensar los barcos rotos y celebrar el éxito de la
expedición. Por supuesto, para ello primero necesitas llegar a casa, pero tu instinto te dice que lo
conseguirás.

Tras salir de la sala con una cámara acorazada, te has dirigido hacia la mazmorra. Lo que has visto a
continuación, ha bajado tu optimismo unos cuantos grados: los dos esqueletos yacían justo detrás de la
entrada de la mazmorra. Todo en su aspecto indicaba que eran los buscadores de tesoros y, a juzgar por la
palidez de los huesos que sobresalían de los pantalones y las mangas, llevaban aquí tumbados muchos años.
Pero, ¿cómo murieron?

"Сlick ..." - un sonido apenas audible de la puerta de la mazmorra cerrándose. Inmediatamente se apresuró a ella,
pero era demasiado tarde. Por supuesto, no tiene ojo de cerradura, y ninguna otra sugerencia de que se puede abrir,
para el caso. Intentaste derribarla, pero era demasiado fuerte. Bueno, si no piensas hacer compañía a esos dos
esqueletos y morir de hambre, no te queda más remedio que encontrar una salida. Tal vez puedas encontrar algo
útil cerca de los esqueletos, habría que examinarlos más de cerca.

Al acercarte a ellos, oyes una voz que sale de la nada: "... termina... el juego...". Sólo había tres opciones:
o había alguien vivo en el castillo, o estos eran los fantasmas que lo rondaban, o has empezado a perder la
cabeza y era la primera alucinación. Ninguna de esas opciones ha sido demasiado alentadora, pero no había vuelta
atrás. Termina el juego y sigue buscando Hypercube.
Lo más probable es que conozcas el juego en el que dos jugadores van cogiendo por turnos de un montón de 1 a 3
piedras, y pierde el que haya cogido la última piedra. Vamos a generalizar ligeramente esta tarea. Supongamos que
ambos jugadores pueden tomar no 1, 2, 3 piedras, sino k1, k2, ..., km de piedras. Aquí nos interesa saber qué
jugador gana en las circunstancias adecuadas (el juego se desarrolla correctamente y ambos jugadores utilizan la
mejor estrategia).
Como entrada obtendrás el número de piedras que hay en el montón al principio de la partida y una cantidad de
piedras que puedes coger del montón en cada movimiento. Por ejemplo - (10, [1, 2, 3]).
Si la cantidad actual de piedras en el montón es menor que el número más bajo de la lista de "movimientos" o
igual - el jugador actual las coge todas y pierde.

Entrada: La cantidad de piedras en el montón y los números que puedes coger de él.

Salida: Número del ganador (1 o 2)

Ejemplo:

piedras(17, [1, 3, 4]) == 2
piedras(17, [1, 3, 4, 6, 9]) == 1

Cómo se utiliza: Para el desarrollo de la IA del juego.

Precondición :
2 jugadores - 1 ganador
'''


def stones(pile, moves):
    #replace this for solution
    # True if 1st player wins if x rocks in pile
    game = {x: False for x in range(1, moves[0] + 1)}
    for stone in range(moves[0] + 1, pile + 1):
        game[stone] = any(not game[stone - m] for m in moves if stone > m)
    return 1 if game[pile] else 2


if __name__ == '__main__':
    print("Example:")
    print(stones(17, [1, 3, 4]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert stones(17, [1, 3, 4]) == 2
    assert stones(17, [1, 3, 4, 6, 9]) == 1
    assert stones(99, [1]) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
