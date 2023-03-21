'''
"We need to fly home as cheaply as possible so that more money is left for gifts. Aunt Lidia
asked for different kinds of cheeses, and Vasia wanted a new toy car. I’ve been looking at the
schedule for quite a while and I’m starting to think that some planes are flying in vain".

As the input you get the flight schedule as an list, each element of which is the price of a direct
flight between 2 cities (list of 3 elements - 2 city names as a string, and a flight price).

Planes fly in both directions and the price in both directions is the same. There is a possibility that
there are no direct flights between cities.

Find the price of the cheapest flight between cities that are given as the 2nd and 3rd arguments. In case
the flight can not be performed, return 0.

Input: 3 arguments: the flight schedule as a list of lists, city of departure and destination city as strings.

Output: The best price as integer.

Examples:
assert (
    cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "A", "C") == 70
)
assert (
    cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "C", "A") == 70
)
assert (
    cheapest_flight(
        [
            ["A", "C", 40],
            ["A", "B", 20],
            ["A", "D", 20],
            ["B", "C", 50],
            ["D", "C", 70],
        ],
        "D",
        "C",
    )
    == 60
)
assert (
    cheapest_flight([["A", "C", 100], ["A", "B", 20], ["D", "F", 900]], "A", "F") == 0
)

How it can be used: In everyday life to find the optimal combination.

Preconditions:
price is always integer;
the flight schedule contains at least one element;
both cities are in the schedule.

----------
----------

"Tenemos que volar a casa lo más barato posible para que quede más dinero para los regalos. La tía
Lidia pidió quesos de distintos tipos y Vasia quería un coche de juguete nuevo. Llevo un buen rato
mirando el horario y empiezo a pensar que algunos aviones vuelan en vano".

Como entrada se obtiene el horario de vuelos como una lista, cada elemento de la cual es el precio de
un vuelo directo entre 2 ciudades (lista de 3 elementos - 2 nombres de ciudades como cadena, y un precio
de vuelo).

Los aviones vuelan en ambas direcciones y el precio en ambas direcciones es el mismo. Existe la posibilidad
de que no haya vuelos directos entre ciudades.

Encuentra el precio del vuelo más barato entre las ciudades que se dan como 2º y 3º argumento. En caso de
que el vuelo no pueda realizarse, devuelve 0.

Entrada: 3 argumentos: el horario del vuelo como lista de listas, ciudad de salida y ciudad de destino
como cadenas.

Salida: El mejor precio como entero.

Ejemplos:
assert (
    vuelo_más_barato([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "A", "C") == 70
)
assert (
    cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "C", "A") == 70
)
assert (
    vuelo_más_barato(
        [
            ["A", "C", 40],
            ["A", "B", 20],
            ["A", "D", 20],
            ["B", "C", 50],
            ["D", "C", 70],
        ],
        "D",
        "C",
    )
    == 60
)
assert (
    cheapest_flight([["A", "C", 100], ["A", "B", 20], ["D", "F", 900]], "A", "F") == 0
)

Cómo se puede utilizar: En la vida cotidiana para encontrar la combinación óptima.

Condiciones previas:
el precio siempre es entero
el horario de vuelos contiene al menos un elemento;
ambas ciudades están en el horario.
'''


import heapq


def cheapest_flight(costs: list, a: str, b: str) -> int:
    # your code here
    # Create a dictionary to represent the flight schedule graph
    graph = {}
    for flight in costs:
        if flight[0] not in graph:
            graph[flight[0]] = []
        if flight[1] not in graph:
            graph[flight[1]] = []
        graph[flight[0]].append((flight[1], flight[2]))
        graph[flight[1]].append((flight[0], flight[2]))

    # Initialize the priority queue and the shortest distance dictionary
    queue = [(0, a)]
    distances = {a: 0}

    # Dijkstra's algorithm
    while queue:
        current_distance, current_city = heapq.heappop(queue)
        if current_city == b:
            return current_distance
        if current_distance > distances[current_city]:
            continue
        for neighbor, price in graph[current_city]:
            distance = current_distance + price
            if neighbor not in distances or distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    # If destination city was not reached, return 0
    return 0


print("Example:")
print(cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "A", "C"))

# These "asserts" are used for self-checking
assert (
    cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "A", "C") == 70
)
assert (
    cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "C", "A") == 70
)
assert (
    cheapest_flight(
        [
            ["A", "C", 40],
            ["A", "B", 20],
            ["A", "D", 20],
            ["B", "C", 50],
            ["D", "C", 70],
        ],
        "D",
        "C",
    )
    == 60
)
assert (
    cheapest_flight([["A", "C", 100], ["A", "B", 20], ["D", "F", 900]], "A", "F") == 0
)
assert (
    cheapest_flight(
        [["A", "B", 10], ["A", "C", 15], ["B", "D", 15], ["C", "D", 10]], "A", "D"
    )
    == 25
)

print("The mission is done! Click 'Check Solution' to earn rewards!")
