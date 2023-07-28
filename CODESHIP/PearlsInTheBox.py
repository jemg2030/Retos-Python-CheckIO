'''
To start the game they put several black and white pearls in one of the boxes. Each robot has N
moves, after which the initial set is being restored for the next game. Each turn, the robot takes
a pearl out of the box and puts one of the opposite color back. The winner is the one who takes the
white pearl on the Nth move.

Our robots don't like uncertainty, that's why they want to know the probability of drawing a white
pearl on the Nth move. The probability is a value between 0 (0% chance or will not happen) and 1
(100% chance or will happen). The result is a float from 0 to 1 with two decimal digits of precision
(±0.01).

You are given a start set of pearls as a string that contains "b" (black) and "w" (white) and the
number of the move (N). The order of the pearls does not matter.

Input: The start sequence of the pearls as a string and the move number as an integer.

Output: The probability for a white pearl as a float.

Example:
checkio('bbw', 3) == 0.48
checkio('wwb', 3) == 0.52
checkio('www', 3) == 0.56
checkio('bbbb', 1) == 0
checkio('wwbb', 4) == 0.5
checkio('bwbwbwb', 5) == 0.48

How it is used: This task introduces you to the basics of probability theory and statistics. Fun
fact: regardless of the initial state, as the number of moves increases, the probability approaches 0.5!

Precondition: 0 < N ≤ 20
0 < |pearls| ≤ 20

----------
----------

Para empezar el juego se ponen varias perlas blancas y negras en una de las cajas. Cada robot
dispone de N movimientos, tras los cuales se restablece el conjunto inicial para la siguiente partida.
En cada turno, el robot saca una perla de la caja y vuelve a poner una del color opuesto. El ganador
es el que coge la perla blanca en el enésimo movimiento.

A nuestros robots no les gusta la incertidumbre, por eso quieren saber la probabilidad de sacar
una perla blanca en el enésimo movimiento. blanca en el enésimo movimiento. La probabilidad es
un valor entre 0 (0% de posibilidades o no sucederá) y 1 (100% de posibilidades o sucederá).
El resultado es un valor flotante de 0 a 1 con dos dígitos decimales de precisión (±0.01).

Se le da un conjunto inicial de perlas como una cadena que contiene "b" (negro) y "w" (blanco) y el
número de la jugada (N). El orden de las perlas no importa.

Entrada: La secuencia de inicio de las perlas como una cadena y el número de movimiento como un entero.

Salida: La probabilidad de una perla blanca como un flotador.

Ejemplo:
checkio('bbw', 3) == 0.48
checkio('wwb', 3) == 0.52
checkio('www', 3) == 0.56
checkio('bbbb', 1) == 0
checkio('wwbb', 4) == 0,5
checkio('bwbwbwb', 5) == 0,48

Cómo se utiliza: Esta tarea le introduce en los fundamentos de la teoría de la probabilidad
y la estadística. Diversión dato curioso: independientemente del estado inicial, a medida que
aumenta el número de movimientos, ¡la probabilidad se aproxima a 0,5!

Condición previa: 0 < N ≤ 20
0 < |perlas| ≤ 20
'''


from itertools import product


def checkio(marbles: str, step: int) -> float:
    def calc_prob(binary_choice):
        num_white = marbles.count('w')
        denominator = len(marbles)
        multiplier = 1
        for choice in binary_choice:
            if choice == 'w':
                multiplier *= num_white / denominator
                num_white -= 1
            else:
                multiplier *= 1 - num_white / denominator
                num_white += 1

        return multiplier * (num_white / denominator)

    possible_choices = product(['b', 'w'], repeat=step - 1)
    return round(sum(calc_prob(choices) for choices in possible_choices), 2)


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio('bbw', 3))

    assert checkio('bbw', 3) == 0.48, "1st example"
    assert checkio('wwb', 3) == 0.52, "2nd example"
    assert checkio('www', 3) == 0.56, "3rd example"
    assert checkio('bbbb', 1) == 0, "4th example"
    assert checkio('wwbb', 4) == 0.5, "5th example"
    assert checkio('bwbwbwb', 5) == 0.48, "6th example"
    print("Coding complete? Click 'Check' to earn cool rewards!")
