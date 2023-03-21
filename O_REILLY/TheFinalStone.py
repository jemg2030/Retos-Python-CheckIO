'''
You have a list of stones with different weights. The result of hitting two stones will be a
new stone with a weight difference between the two stones.

Your goal is to find the weight of the final stone. If no stones left, the result is 0.

The algorith is very simple:

get the two biggest stones in the batch
hit and get the resulting stone
put the resulting stone back in the batch.
For the Speedy category, you can think about your solution for a million stones

Input: List of stones as list of ints

Output: Int.

Example:
assert final_stone([3, 5, 1, 1, 9]) == 1
assert final_stone([1, 2, 3]) == 0
assert final_stone([1, 2, 3, 4]) == 0
assert final_stone([1, 2, 3, 4, 5]) == 1

Precondition: only positive, non-zero values. The list of stones can be empty

----------
----------

Tienes una lista de piedras con pesos diferentes. El resultado de golpear dos piedras será una
nueva piedra con una diferencia de peso entre las dos piedras.

Tu objetivo es encontrar el peso de la última piedra. Si no quedan piedras, el resultado es 0.

El algoritmo es muy sencillo

obtener las dos piedras más grandes del lote
golpear y obtener la piedra resultante
poner la piedra resultante de nuevo en el lote.
Para la categoría Speedy, puede pensar en su solución para un millón de piedras

Entrada: Lista de piedras como lista de ints

Salida: Int.

Ejemplo:
assert piedra_final([3, 5, 1, 1, 9]) == 1
assert piedra_final([1, 2, 3]) == 0
assert piedra_final([1, 2, 3, 4]) == 0
assert piedra_final([1, 2, 3, 4, 5]) == 1

Precondición: sólo valores positivos, distintos de cero. La lista de piedras puede estar vacía
'''


import heapq


def final_stone(stones: list[int]) -> int:
    # your code here
    # Use a max-heap to keep track of stones
    heap = [-stone for stone in stones]
    heapq.heapify(heap)

    # Repeatedly hit the two biggest stones until only one is left
    while len(heap) > 1:
        stone1 = -heapq.heappop(heap)
        stone2 = -heapq.heappop(heap)
        diff = abs(stone1 - stone2)
        heapq.heappush(heap, -diff)

    # Return the weight of the final stone, or 0 if none are left
    return -heap[0] if heap else 0


print('Example:')
print(final_stone([1,2,3]))

assert final_stone([3, 5, 1, 1, 9]) == 1
assert final_stone([1, 2, 3]) == 0
assert final_stone([1, 2, 3, 4]) == 0
assert final_stone([1, 2, 3, 4, 5]) == 1
assert final_stone([1, 1, 1, 1]) == 0
assert final_stone([1, 1, 1]) == 1
assert final_stone([1, 10, 1]) == 8
assert final_stone([1, 10, 1, 8]) == 0
assert final_stone([]) == 0
assert final_stone([1]) == 1
assert final_stone([10, 20, 30, 50, 100, 10, 20, 10]) == 10

print("The mission is done! Click 'Check Solution' to earn rewards!")
