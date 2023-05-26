'''
8-puzzle-pic8 puzzle is a sliding puzzle that consists of a frame of randomly ordered,
numbered square tiles with one missing tile. The object of the puzzle is to place the tiles
in the right order (see picture) by using sliding moves to utilize the empty space. You can
read more about this kind of puzzle on Wikipedia.

Our puzzle is presented as a 3x3 matrix with numbers from 1 to 8. Zero is the empty cell.
You can "move" the empty cell in four directions: up--"U", down--"D", left--"L", and right--"R".
You need to return a sequence of moves to solve the puzzle. The solution is presented as string
of symbols ("UDLR") describing your moves.

8-puzzle

Input: A matrix with numbers from 1 to 8 as a list of lists with integers.

Output: The route of the empty cell as a string.

Example:

checkio([[1, 2, 3],
         [4, 6, 8],
         [7, 5, 0]]) == "ULDR"

How it is used: The most obvious usage for the concepts in this task lie in creating a bot
to solve slide puzzles; however, this task also is a fun way to learn something new because
the n-puzzle is a classical problem for modeling algorithms involving heuristics.

Precondition:
len(puzzle) == 3
all(len(row) == 3 for row in puzzle)

----------
----------

8-puzzle-pic“Rompecabezas 8” (o “Juego del 8”) es un rompecabezas formado por un grupo de
piezas numeradas y ordenadas de forma aleatoria, que se deslizan sobre un marco con un espacio
vacío. El objeto del rompecabezas es colocar las fichas en el orden correcto (ver imagen)
deslizando cualquier pieza adyacente al espacio disponible. Puedes leer más sobre este tipo de
rompecabezas en Wikipedia.

Nuestro rompecabezas se presenta como una matriz de 3x3 con números del 1 al 8. Cero es la celda
vacía. Es posible "moverse" hacia la celda vacía en cuatro direcciones: arriba - "U", abajo - "D",
a la izquierda - "L", y a la derecha - "R". El objetivo es necesita encontrar una secuencia de
movimientos para resolver el rompecabezas. La solución se presenta como cadena de símbolos ("DUDL")
que describen los movimientos escogidos.

8-puzzle

Datos de Entrada: una matriz con números del 1 al 8 como una lista de listas con números enteros.

Output: La ruta de la celda vacía como una cadena (str).

Example:

checkio([[1, 2, 3],
         [4, 6, 8],
         [7, 5, 0]]) == "ULDR"

¿Cómo se usa?: El uso más obvio para los conceptos en esta misión es la creación de un robot
(bot) que para resolver rompecabezas deslizantes; sin embargo, esta tarea también es una forma
divertida de aprender algo nuevo, porque este tipo de rompecabezas (n-puzzle) son utilizados
tradicionalmente como problemas a resolver por algoritmos de modelado que incluyen heurísticos.

Condiciones:
len(puzzle) == 3
all(len(row) == 3 for row in puzzle)
'''


from typing import List
import heapq

class PriorityQueue:
    def  __init__(self):
        self.heap = []

    def push(self, item, priority):
        pair = (priority,item)
        heapq.heappush(self.heap,pair)

    def pop(self):
        (priority,item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0

def locate_zero(pos):
    for x in range(0, len(pos)):
        for y in range(0, len(pos[x])):
            if pos[x][y] == 0:
                return x,y
    return -1,-1

moves = [('U', (-1,0)), ('D', (1,0)), ('L', (0,-1)), ('R', (0,1))]

def fix(move, pos, x, y):
    pos = [[y for y in x] for x in pos] # Deepcopy of pos
    d, (dx, dy) = move
    pos[x][y], pos[x+dx][y+dy] = pos[x+dx][y+dy], pos[x][y]
    return d, pos

def neighbors(pos):
    x, y = locate_zero(pos)
    m = [m for m in moves if -1 < x+m[1][0] < len(pos) and -1 < y+m[1][1] < len(pos[x])]
    return [fix(move, pos, x, y) for move in m]

def dist(a, b):
    # Hamming distance
    return sum([1 for x in a for y in b if x != y])

def astar(start, goal=None):
    """
    Notion of a state is represented as the tuple (pos, path).
    seen contains positions.
    """
    if goal is None:
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    seen = set()
    fringe = PriorityQueue()
    fringe.push((start, ''), dist(start, goal))
    while not fringe.isEmpty():
        (pos, path) = fringe.pop()
        key = ''.join([str(el) for row in pos for el in row])
        if key in seen:
            continue
        if pos == goal:
            return path
        seen.add(key)
        for n in neighbors(pos):
            move, newnews = n
            fringe.push((newnews, path + move), dist(newnews, goal) + len(path))
    return ''

def checkio(puzzle: List[List[int]]) -> str:
    """
    Solve the puzzle
      U - up
      D - down
      L - left
      R - right
    """
    return astar(puzzle)


if __name__ == '__main__':
    print("Example:")
    print(checkio([[1, 2, 3],
                   [4, 6, 8],
                   [7, 5, 0]]))

    #This part is using only for self-checking and not necessary for auto-testing
    GOAL = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    MOVES = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

    def check_solution(func, puzzle):
        size = len(puzzle)
        route = func([row[:] for row in puzzle])
        goal = GOAL
        x = y = None
        for i, row in enumerate(puzzle):
            if 0 in row:
                x, y = i, row.index(0)
                break
        for ch in route:
            swap_x, swap_y = x + MOVES[ch][0], y + MOVES[ch][1]
            if 0 <= swap_x < size and 0 <= swap_y < size:
                puzzle[x][y], puzzle[swap_x][swap_y] = puzzle[swap_x][swap_y], 0
                x, y = swap_x, swap_y
        if puzzle == goal:
            return True
        else:
            print("Puzzle is not solved")
            return False

    assert check_solution(checkio, [[1, 2, 3],
                                    [4, 6, 8],
                                    [7, 5, 0]]), "1st example"
    assert check_solution(checkio, [[7, 3, 5],
                                    [4, 8, 6],
                                    [1, 2, 0]]), "2nd example"
    print("Coding complete? Click 'Check' to earn cool rewards!")
