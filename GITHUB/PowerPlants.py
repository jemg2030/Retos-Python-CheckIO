'''
This mission is another version of the ”Power Supply” mission originated from oduvan 's idea.
You have to properly place the given power plants and supply power to all the cities.

The intercity network and the range of each power plant are given as input values. A power plant
can provide power to the city where it’s been placed and within its range. You have to return a
dictionary, where the key is the city in which you’ll place the power plant and the value is its
range.

NOTE:
You will always be given enough or more power-plants. So it isn't always necessary to return all
power-plant placements.

Example:
power_plants({('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E')}, [2]) == {'C': 2}
power_plants({('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F')}, [1, 1]) == {'B': 1, 'E': 1}
power_plants({('A', 'B'), ('B', 'C'), ('A', 'D'), ('B', 'E')}, [1, 0]) == {'B': 1, 'D': 0}

Input:
The intercity network represented as a set of connections, where each connection is a tuple of two nodes
connected with each other.
The range of each power plant, represented as a list of integers.
Output:

A dictionary of placements, where each key is the city in which you’ll place the power plant and each
value is the corresponding range.

Precondition:
3 ≤ number of cities ≤ 50
1 ≤ number of power-plants
range of power-plant ≥ 0

----------
----------

This mission is another version of the ”Power Supply” mission originated from oduvan 's idea.
You have to properly place the given power plants and supply power to all the cities.

The intercity network and the range of each power plant are given as input values. A power plant
can provide power to the city where it’s been placed and within its range. You have to return a
dictionary, where the key is the city in which you’ll place the power plant and the value is its range.

NOTE:
You will always be given enough or more power-plants. So it isn't always necessary to return all
power-plant placements.

Example:
power_plants({('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E')}, [2]) == {'C': 2}
power_plants({('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F')}, [1, 1]) == {'B': 1, 'E': 1}
power_plants({('A', 'B'), ('B', 'C'), ('A', 'D'), ('B', 'E')}, [1, 0]) == {'B': 1, 'D': 0}

Input:
The intercity network represented as a set of connections, where each connection is a tuple of two nodes
connected with each other.
The range of each power plant, represented as a list of integers.

Output:
A dictionary of placements, where each key is the city in which you’ll place the power plant and each value
is the corresponding range.

Precondition:
3 ≤ number of cities ≤ 50
1 ≤ number of power-plants
range of power-plant ≥ 0
'''


from typing import Set, Tuple, List, Dict
from itertools import chain,combinations
from heapq import heappop, heappush


def power_plants(network: Set[Tuple[str, str]], ranges: List[int]) -> Dict[str, int]:
    powers = [(power, ranges.count(power)) for power in sorted(set(ranges), reverse=True)]
    cities = {city for edge in network for city in edge}

    def network_map(max_power: int) -> Dict[str, Dict[int, List[str]]]:
        reachable_in_one = {city: set() for city in cities}
        for city_a, city_b in network:
            reachable_in_one[city_a] |= {city_b}
            reachable_in_one[city_b] |= {city_a}
        cities_map = {city: {0: [city]} for city in cities}

        for distance in range(0, max_power):
            for city in cities:
                reachable = {city_b for city_a in cities_map[city][distance] for city_b in reachable_in_one[city_a]}
                cities_map[city][distance + 1] = list(reachable | set(cities_map[city][distance]))
        return cities_map

    cities_map = network_map(powers[0][0])
    steps = [(0, powers, cities, [])]
    while steps:
        _, ((power, nb_occurences), *powers), unpowered, plants = heappop(steps)

        if len(unpowered) <= nb_occurences:
            return dict(plants + [(city, power) for city in unpowered])

        for combination in combinations(unpowered, nb_occurences):
            new_unpowered = unpowered - set.union(*(set(cities_map[city][power]) for city in combination))
            if not new_unpowered:
                return dict(plants + [(city, power) for city in combination])
            if powers:
                heappush(steps,
                         (len(new_unpowered), powers, new_unpowered, plants + [(city, power) for city in combination]))


if __name__ == '__main__':
    assert power_plants({('A', 'B'), ('B', 'C')}, [1]) == {'B': 1}
    assert power_plants({('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E')}, [2]) == {'C': 2}
    assert power_plants({('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F')}, [1, 1]) == {'B': 1, 'E': 1}
    assert power_plants({('A', 'B'), ('B', 'C'), ('A', 'D'), ('B', 'E')}, [1, 0]) == {'B': 1, 'D': 0}

    print('The local tests are done. Click on "Check" for more real tests.')
