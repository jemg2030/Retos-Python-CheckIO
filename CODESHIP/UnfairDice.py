'''
For this task, you're going to play a dice game, but first you must prepare for an overwhelming
victory. The game itself is very simple. Both players roll a single die and whoever rolls highest
scores a point. (On a tie, both players must reroll until someone scores.)

These aren't standard dice however. Each player can put any positive number on any side of the
die as long as the number of sides match and the total of all the chosen numbers are the same.
For example, one player might use a six sided die with the numbers [3, 3, 3, 3, 6, 6] while the
other player uses a six sided die with the numbers [4, 4, 4, 4, 4, 4]. The interesting part of
this game is that even with the same number of sides and the same total, different dice have
different chances of winning. Using the example die, the player with all 4's will win 2/3 of the
time.

To prepare for this game, you're investigating different ways of picking the numbers. To do this,
write a program that will take an opponent's die and output some die which will win against it more
than half the time. If no die satisfies the task requirements, return an empty list.

Input: An enemy's die as a sorted list of integers, one for each face of the opponent's die.

Output: Your die as a list of integers, one for each face of your die or an empty list.

Example:
winning_die([3, 3, 3, 3, 6, 6]) == [4, 4, 4, 4, 4, 4] # Or [3, 3, 4, 4, 5, 5]
winning_die([4, 4, 4, 4, 4, 4]) == [2, 2, 5, 5, 5, 5] # Or [5, 5, 2, 2, 5, 5]
winning_die([2, 2, 5, 5, 5, 5]) == [3, 3, 3, 3, 6, 6]
winning_die([1, 1, 3]) == [1, 2, 2]
winning_die([1, 2, 3, 4, 5, 6]) == [] # Any 6-sided die totaling 21 has a 50/50 chance of winning against the standard die.
winning_die([2, 3, 4, 5, 6, 7]) == [1, 1, 3, 7, 7, 8] # This can be beat though.
winning_die([1, 2, 3, 4, 5, 6]) == []

How it is used: This task illustrates some of the unintuitive results in probability. Many
people would think that two dice as similar as the ones in the description above (same number
of sides, same average roll) would have a roughly 50/50 chance against each other. Even more
unusual is that sets of dice can be created where die A beats die B, die B beats die C and yet
die C beats die A (e.g. the first three examples above). These are called nontransitive dice .

Preconditions:
3 ≤ len(die) ≤ 10
sum(die) ≤ 100
min(die) ≥ 1
max(die) ≤ 18

----------
----------

Para esta tarea, vas a jugar a un juego de dados, pero primero debes prepararte para una aplastante
victoria. El juego en sí es muy sencillo. Ambos jugadores tiran un solo dado y el que saque el más alto
gana un punto. (En caso de empate, ambos jugadores deben volver a tirar hasta que alguien puntúe).

Sin embargo, no son dados normales. Cada jugador puede poner cualquier número positivo en cualquier cara del dado
siempre que el número de caras coincida y el total de todos los números elegidos sea el mismo.
Por ejemplo, un jugador puede usar un dado de seis caras con los números [3, 3, 3, 3, 6, 6] mientras que el
otro jugador utiliza un dado de seis caras con los números [4, 4, 4, 4, 4, 4]. Lo interesante de
este juego es que, incluso con el mismo número de caras y el mismo total, dados diferentes tienen
diferentes posibilidades de ganar. Usando el dado del ejemplo, el jugador con todos los 4 estará ganando 2/3 de las
de las veces.

Para prepararte para este juego, estás investigando distintas formas de elegir los números. Para ello,
escribe un programa que tome el dado de un oponente y produzca un dado que gane más de la mitad de las veces.
más de la mitad de las veces. Si ningún dado satisface los requisitos de la tarea, devuelve una lista vacía.

Entrada: Un dado del adversario como una lista ordenada de enteros, uno por cada cara del dado del adversario.

Salida: Tu dado como una lista de enteros, uno por cada cara de tu dado o una lista vacía.

Ejemplo:
dado_ganador([3, 3, 3, 3, 6, 6]) == [4, 4, 4, 4, 4, 4] # O [3, 3, 4, 4, 5, 5]
winning_die([4, 4, 4, 4, 4, 4]) == [2, 2, 5, 5, 5, 5] # O [5, 5, 2, 2, 5, 5]
winning_die([2, 2, 5, 5, 5, 5]) == [3, 3, 3, 3, 6, 6]
dado_ganador([1, 1, 3]) == [1, 2, 2]
winning_die([1, 2, 3, 4, 5, 6]) == [] # Cualquier dado de 6 caras que sume 21 tiene una probabilidad de 50/50 de
                                      # ganar contra el dado estándar.
winning_die([2, 3, 4, 5, 6, 7]) == [1, 1, 3, 7, 7, 8] # Sin embargo, se puede ganar.
dado_ganador([1, 2, 3, 4, 5, 6]) == []

Cómo se utiliza: Esta tarea ilustra algunos de los resultados poco intuitivos en probabilidad. Muchas
gente pensaría que dos dados tan parecidos como los de la descripción anterior (mismo número
de caras, misma tirada media) tendrían una probabilidad aproximada de 50/50 el uno contra el otro. Aún más
aún más inusual es que se pueden crear juegos de dados en los que el dado A gana al dado B, el dado B gana al dado C
y, sin embargo, el dado C gana al dado A (por ejemplo, el dado C gana al dado A).
el dado C gana al dado A (por ejemplo, los tres primeros ejemplos anteriores). Son los llamados dados no transitivos.

Precondiciones:
3 ≤ len(dado) ≤ 10
sum(dado) ≤ 100
min(dado) ≥ 1
max(dado) ≤ 18
'''


def winning_die(enemy_die):
    def explore(rlen, rlist, rsum, rmin):
        if rlen:
            for one in range(rmin, 1 + rsum // rlen) if rlen > 1 else [rsum]:
                explore(rlen - 1, rlist + [one], rsum - one, one)
        elif sum((p > e)-(p < e) for p in rlist for e in enemy_die) > 0:
            raise StopIteration(rlist)
    try:
        explore(len(enemy_die), [], sum(enemy_die), 1)
    except StopIteration as found:
        return found.args[0]
    else:
        return []


if __name__ == '__main__':
    #These are only used for self-checking and not necessary for auto-testing
    def check_solution(func, enemy):
        player = func(enemy)
        total = 0
        for p in player:
            for e in enemy:
                if p > e:
                    total += 1
                elif p < e:
                    total -= 1
        return total > 0
    

    assert check_solution(winning_die, [3, 3, 3, 3, 6, 6]), "Threes and Sixes"
    assert check_solution(winning_die, [4, 4, 4, 4, 4, 4]), "All Fours"
    assert check_solution(winning_die, [1, 1, 1, 4]), "Unities and Four"
    assert winning_die([1, 2, 3, 4, 5, 6]) == [], "All in row -- No die"
