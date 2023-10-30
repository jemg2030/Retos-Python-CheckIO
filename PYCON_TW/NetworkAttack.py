"""
Nicola regularly inspects the local networks for security issues. He uses a smart and aggressive
program which takes control of computers on the network. This program attacks all connected computers
simultaneously, then uses the captured computers for further attacks. Nicola started the virus program
in the first computer and took note of the time it took to completely capture the network. We can help
him improve his process by modeling and improving his inspections.

We are given information about the connections in the network and the security level for each computer.
Security level is the time (in minutes) that is required for the virus to capture a machine. Capture
time is not related to the number of infected computers attacking the machine. Infection start from
the 0th computer (which is already infected). Connections in the network are undirected. Security
levels are not equal to zero (except infected).

Information about a network is represented as a matrix NxN size, where N is a number of
computers. If i th computer connected with j th computer, then matrix[i][j] == matrix[j][i] == 1, else 0.
Security levels are placed in the main matrix diagonal, so matrix[i][i] is the security level
for the i th computer.

attack

You should calculate how much time is required to capture the whole network in minutes.

Input: Network information as a list of lists with integers.

Output: The total time of taken to capture the network as an integer.

Example:

capture([[0, 1, 0, 1, 0, 1],
         [1, 8, 1, 0, 0, 0],
         [0, 1, 2, 0, 0, 1],
         [1, 0, 0, 1, 1, 0],
         [0, 0, 0, 1, 3, 1],
         [1, 0, 1, 0, 1, 2]]) == 8
capture([[0, 1, 0, 1, 0, 1],
         [1, 1, 1, 0, 0, 0],
         [0, 1, 2, 0, 0, 1],
         [1, 0, 0, 1, 1, 0],
         [0, 0, 0, 1, 3, 1],
         [1, 0, 1, 0, 1, 2]]) == 4
capture([[0, 1, 1],
         [1, 9, 1],
         [1, 1, 9]]) == 9

How it is used: This concept shows how to model and examine various network configurations.
The idea does not only apply to computer networks however, it can also be a model for the
spread of disease or dissemination of rumors.

Precondition:
3 ≤ len(matrix) ≤ 10
matrix[0][0] == 0
all(len(row) == len(matrix[0]) for row in matrix)
all(matrix[i][j] == matrix[j][i] for i in range(len(matrix)) for j in range(len(matrix)))
all(0 < matrix[i][i] < 10 for i in range(1, len(matrix)))
all(0 ≤ matrix[i][j] ≤ 1 for i in range(len(matrix)) for j in range(len(matrix)) if i != j)

----------
----------

Nicola inspecciona regularmente las redes locales en busca de problemas de seguridad. Utiliza un programa inteligente y agresivo que toma el control de los ordenadores de la red. Este programa ataca simultáneamente a todos los ordenadores conectados y luego utiliza los ordenadores capturados para otros ataques. Nicola inició el programa antivirus en el primer ordenador y tomó nota del tiempo que tardó en capturar completamente la red. Podemos ayudarle a mejorar su proceso modelando y mejorando sus inspecciones.

Se nos da información sobre las conexiones de la red y el nivel de seguridad de cada ordenador. El nivel de seguridad es el tiempo (en minutos) que necesita el virus para capturar una máquina. El tiempo de captura no está relacionado con el número de ordenadores infectados que atacan la máquina. La infección comienza en el ordenador 0 (que ya está infectado). Las conexiones en la red son no dirigidas. Los niveles de seguridad no son iguales a cero (excepto infectado).

La información sobre una red se representa como una matriz de tamaño NxN, donde N es el número de ordenadores. Si el ordenador i está conectado con el ordenador j, entonces matrix[i][j] == matrix[j][i] == 1, si no 0. Los niveles de seguridad se colocan en la diagonal principal de la matriz, por lo que matrix[i][i] es el nivel de seguridad del ordenador i.

ataque

Debes calcular cuánto tiempo se necesita para capturar toda la red en minutos.

Entrada: Información de la red como una lista de listas con números enteros.

Salida: El tiempo total necesario para capturar la red como un entero.

Ejemplo:
capture([[0, 1, 0, 1, 0, 1],
         [1, 8, 1, 0, 0, 0],
         [0, 1, 2, 0, 0, 1],
         [1, 0, 0, 1, 1, 0],
         [0, 0, 0, 1, 3, 1],
         [1, 0, 1, 0, 1, 2]]) == 8
capture([[0, 1, 0, 1, 0, 1],
         [1, 1, 1, 0, 0, 0],
         [0, 1, 2, 0, 0, 1],
         [1, 0, 0, 1, 1, 0],
         [0, 0, 0, 1, 3, 1],
         [1, 0, 1, 0, 1, 2]]) == 4
capture([[0, 1, 1],
         [1, 9, 1],
         [1, 1, 9]]) == 9

Cómo se utiliza: Este concepto muestra cómo modelizar y examinar diversas configuraciones de red.
Sin embargo, la idea no sólo se aplica a las redes informáticas, sino que también puede servir
de modelo para la propagación de enfermedades o la difusión de rumores.

Precondition:
3 ≤ len(matrix) ≤ 10
matrix[0][0] == 0
all(len(row) == len(matrix[0]) for row in matrix)
all(matrix[i][j] == matrix[j][i] for i in range(len(matrix)) for j in range(len(matrix)))
all(0 < matrix[i][i] < 10 for i in range(1, len(matrix)))
all(0 ≤ matrix[i][j] ≤ 1 for i in range(len(matrix)) for j in range(len(matrix)) if i != j)
"""


def capture(matrix):
    free = list(range(1, len(matrix)))
    infected = [0]
    t = 0
    while free:
        t += 1
        underattack = []
        for i in infected:
            for j in free:
                if matrix[i][j] == 1 and j not in underattack:
                    underattack.append(j)
        for j in underattack:
            matrix[j][j] -= 1
            if matrix[j][j] == 0:
                free.remove(j)
                infected.append(j)
    return t


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert (
        capture(
            [
                [0, 1, 0, 1, 0, 1],
                [1, 8, 1, 0, 0, 0],
                [0, 1, 2, 0, 0, 1],
                [1, 0, 0, 1, 1, 0],
                [0, 0, 0, 1, 3, 1],
                [1, 0, 1, 0, 1, 2],
            ]
        )
        == 8
    ), "Base example"
    assert (
        capture(
            [
                [0, 1, 0, 1, 0, 1],
                [1, 1, 1, 0, 0, 0],
                [0, 1, 2, 0, 0, 1],
                [1, 0, 0, 1, 1, 0],
                [0, 0, 0, 1, 3, 1],
                [1, 0, 1, 0, 1, 2],
            ]
        )
        == 4
    ), "Low security"
    assert capture([[0, 1, 1], [1, 9, 1], [1, 1, 9]]) == 9, "Small"
