'''
"Look Stephen, here's a list of the items that need to be loaded onto the ship. We're going to need a
lot of batteries." Nikola handed him a notepad.

"What are the numbers next to the items?"

"That is the weight of each item."

"Er, why?"

"So you can see how much your trading cards and comic book collection will weigh us down during flight."
Rang Sofias voice from the phone tube.

"What is she talking about?” asked Nikola “Ooooh, nevermind, that was sarcasm. It’s important because your
load-stabilizing belt is broken and there is no way that we can find a new one right now. That’s why, when
you carry the things on the list, you’ll have to redistribute their weights in order to get the minimal
weight in each arm."

"Okay, so I have to figure out how many batteries I should hold in each hand to prevent them from breaking
when they inevitably fall to the ground. Got it."

You have been given a list of integer weights. You should help Stephen distribute these weights into two
sets, such that the difference between the total weight of each set is as low as possible.

Input data: A list of the weights as a list of integers.

Output data: The number representing the lowest possible weight difference as a positive integer.

Example:
checkio([10,10]) == 0
checkio([10]) == 10
checkio([5, 8, 13, 27, 14]) == 3
checkio([5,5,6,5]) == 1
checkio([12, 30, 30, 32, 42, 49]) == 9
checkio([1, 1, 1, 3]) == 0

How it is used: This is a combinatorial optimization version of the partition problem. The
combinatorial optimization has wide usage and you often see it when you look at automated schedules
or route calculating.

Precondition:
0 < len(weights) ≤ 10
all(0 < x < 100 for x in weights)

----------
----------

"Mira Stephen, aquí hay una lista de los artículos que necesitan ser cargados en la nave. Vamos a
necesitar muchas baterías". Nikola le entregó un bloc de notas.

"¿Qué son los números junto a los elementos?"

"Es el peso de cada artículo".

"¿Por qué?"

"Para que veas cuánto nos pesarán tus cromos y tu colección de cómics durante el vuelo". Sonó la voz de
Sofías desde el tubo del teléfono.

"¿De qué está hablando?" preguntó Nikola "Ooooh, no importa, eso fue sarcasmo. Es importante porque tu
cinturón estabilizador de carga está roto y no hay forma de que encontremos uno nuevo ahora mismo.
Por eso, cuando lleves las cosas de la lista, tendrás que redistribuir sus pesos para conseguir el peso
 mínimo en cada brazo."

"Vale, entonces tengo que calcular cuántas pilas debo llevar en cada mano para evitar que se rompan cuando
inevitablemente caigan al suelo. Entendido".

Se te ha dado una lista de pesos enteros. Debes ayudar a Stephen a distribuir estos pesos en dos conjuntos,
de forma que la diferencia entre el peso total de cada conjunto sea lo más baja posible.

Datos de entrada: Una lista de los pesos como una lista de enteros.

Datos de salida: El número que representa la menor diferencia de pesos posible como un entero positivo.

Ejemplo:
checkio([10,10]) == 0
checkio([10]) == 10
checkio([5, 8, 13, 27, 14]) == 3
checkio([5,5,6,5]) == 1
checkio([12, 30, 30, 32, 42, 49]) == 9
checkio([1, 1, 1, 3]) == 0

Cómo se utiliza: Esta es una versión de optimización combinatoria del problema de partición. La optimización
combinatoria tiene un amplio uso y se ve a menudo cuando se miran los horarios automatizados o el cálculo de rutas.

Precondición:
0 < len(pesos) ≤ 10
all(0 < x < 100 para x en pesos)
'''


def checkio(data):

    #replace this for solution
    n = len(data)
    S = sum(data)
    dp = [[False] * (S + 1) for i in range(n + 1)]
    dp[0][0] = True
    for i in range(1, n + 1):
        for j in range(S + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= data[i - 1]:
                dp[i][j] = dp[i][j] or dp[i - 1][j - data[i - 1]]
    j = S // 2
    while j >= 0 and not dp[n][j]:
        j -= 1
    return S - 2 * j


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([10, 10]) == 0, "1st example"
    assert checkio([10]) == 10, "2nd example"
    assert checkio([5, 8, 13, 27, 14]) == 3, "3rd example"
    assert checkio([5, 5, 6, 5]) == 1, "4th example"
    assert checkio([12, 30, 30, 32, 42, 49]) == 9, "5th example"
    assert checkio([1, 1, 1, 3]) == 0, "6th example"
