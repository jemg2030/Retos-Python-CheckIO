"""
Every Christmas in my family, each of us gives a present to only one other person.
To organize who should offer a gift to whom (I call it the chain of presents), we
introduced a few rules:

- There should be a single chain where every person in the family is present,
- Couples should not give to one another,
- Every person should give a gift to a different person than they had in previous years

So the problem would be to find and list the longest list of chains of presents. For
example in a family {a,b,c,d} with couples=({a,b},{c,d}): [[a,c,b,d],[a,d,b,c]].

You are given a set of family member names and a list of couples in this family. Find the
maximum number of chains with all family members. Gift chains should be represented as a
list of names where i -th gives a present to i+1 -th and the last person in the list to the
first.

Input: Names of family members as a set of strings. Couple list as a tuple of sets with two
strings in each.

Output: The longest list of gift chains as a list/tuple of lists/tuples with strings.

Example:
find_chains({'Gary', 'Jeanette', 'Hollie'}, ({'Gary', 'Jeanette'},)) # 0 chains
find_chains({'Curtis', 'Lee', 'Rachel', 'Javier'}, ({'Rachel', 'Javier'}, {'Curtis', 'Lee'})) # 2 chains

How it is used: This is a combinatorial task that can be useful for scheduling.

Precondition:

len(couples) <= 7

----------
----------

En mi familia, cada Navidad cada uno de nosotros hace un regalo a una sola persona.
Para organizar quién debe ofrecer un regalo a quién (yo lo llamo la cadena de regalos),
introdujimos algunas reglas:

- Debe haber una sola cadena en la que estén presentes todos los miembros de la familia,
- Las parejas no deben hacerse regalos mutuamente,
- Cada persona debe hacer un regalo a una persona distinta de la que le hizo en años anteriores.

Así que el problema sería encontrar y enumerar la lista más larga de cadenas de regalos. Por
ejemplo en una familia {a,b,c,d} con parejas=({a,b},{c,d}): [[a,c,b,d],[a,d,b,c]].

Se le da un conjunto de nombres de miembros de la familia y una lista de parejas de esta familia.
Encuentre el número máximo de cadenas con todos los miembros de la familia. Las cadenas de regalos
deben representarse como una lista de nombres en la que i -ésima da un regalo a i+1 -ésima y la
última persona de la lista a la primera.

Entrada: Nombres de los miembros de la familia como un conjunto de cadenas. Lista de parejas como
una tupla de conjuntos con dos cadenas en cada uno.

Salida: La lista más larga de cadenas de regalos como una lista/tupla de listas/tuplas con cadenas.

Ejemplo:
find_chains({'Gary', 'Jeanette', 'Hollie'}, ({'Gary', 'Jeanette'},)) # 0 cadenas
find_chains({'Curtis', 'Lee', 'Rachel', 'Javier'}, ({'Rachel', 'Javier'}, {'Curtis', 'Lee'})) # 2 cadenas

Cómo se utiliza: Se trata de una tarea combinatoria que puede ser útil para la programación.

Condición previa:

len(parejas) <= 7
"""


def init_pairs(family, couples):
    c = [(x[0], x[1]) for x in couples] + [(x[1], x[0]) for x in couples]
    return [x for x in __import__("itertools").permutations(family, 2) if x not in c]


def is_valid(last_chain, chains, best):
    flatten = [x for y in last_chain for x in y]
    unique = list(set(flatten))
    ret = all([flatten.count(x) <= 2 for x in unique])
    return ret and not len(chains) < len(best) - 1


def find_chains(family, couples):
    family = sorted(list(family))
    couples = [list(x) for x in couples]
    pairs = init_pairs(family, couples)
    stack, best = [([], [], pairs)], []
    while stack:
        chains, last_chain, pairs = stack.pop()
        if not last_chain:
            best = chains if len(best) < len(chains) else best
            if pairs:
                stack += [(chains, [pairs[0]], pairs[1:])]
            continue
        first, last = last_chain[0][0], last_chain[-1][1]
        if len(last_chain) == len(family) and first == last:
            stack += [(chains + [last_chain], [], pairs)]
            continue
        for i in [x for x in pairs if last in x[0]]:
            if is_valid(last_chain + [i], chains, best):
                remove = [x for x in pairs if x != i]
                stack += [(chains, last_chain + [i], remove)]
    return [[x[0] for x in y] for y in best]


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def checker(function, family, couples, total):
        user_result = function(family.copy(), tuple(c.copy() for c in couples))
        if not isinstance(user_result, (list, tuple)) or any(
            not isinstance(chain, (list, tuple)) for chain in user_result
        ):
            return False
        if len(user_result) < total:
            return False
        gifted = set()
        for chain in user_result:
            if set(chain) != family or len(chain) != len(family):
                return False
            for f, s in zip(chain, chain[1:] + [chain[0]]):
                if {f, s} in couples:
                    return False
                if (f, s) in gifted:
                    return False
                gifted.add((f, s))
        return True

    assert checker(
        find_chains, {"Gary", "Jeanette", "Hollie"}, ({"Gary", "Jeanette"},), 0
    ), "Three of us"
    assert checker(
        find_chains,
        {"Curtis", "Lee", "Rachel", "Javier"},
        ({"Rachel", "Javier"}, {"Curtis", "Lee"}),
        2,
    ), "Pairs"
    assert checker(
        find_chains,
        {"Philip", "Sondra", "Mary", "Selena", "Eric", "Phyllis"},
        ({"Philip", "Sondra"}, {"Eric", "Mary"}),
        4,
    ), "Pairs and Singles"
