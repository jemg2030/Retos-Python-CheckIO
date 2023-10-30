"""
Gerrymandering is a practice intended to establish a political advantage for a
particular party or group by manipulating district boundaries. The resulting district
is known as a gerrymander (/ˈdʒɛriˌmændər/); however, that word can also refer to
the process. The term gerrymandering has negative connotations. Two principal tactics
are used in gerrymandering: "cracking" (i.e. diluting the voting power of the opposing
party's supporters across many districts) and "packing" (concentrating the opposing party's
voting power in one district to reduce their voting power in other districts).

In addition to its use achieving desired electoral results for a particular party,
gerrymandering may be used to help or hinder a particular demographic, such as a political,
ethnic, racial, linguistic, religious, or class group, such as in U.S. federal voting district
boundaries that produce a majority of constituents representative of African-American or other
racial minorities, known as "majority-minority districts". Gerrymandering can also be used to
protect incumbents.

Read more about it on wikipedia or watch this episode Gerrymandering: Last Week Tonight
with John Oliver (HBO)

You have a map of units. Every unit has two elements (amount of people voted for candidate
Yellow and amount of people voted for candidate Blue). Your mission is to split the given
area on X amount of districts in such a way so candidate Yellow gets more districts voted
for him than candidate Blue.

There are two main rules of building districts:

all districts should have same amount of people;
all units should be connected inside of one district.
The output is essentially labelling each unit with a letter, units with the same letter
would become a post-gerrymander district. The population of the original units with the
same label would be merged into the new post-gerrymander district. The goal of the gerrymandering
is to make sure that if the election were to be held on these new districts, Yellow candidate
would win.

Input: Two arguments. Amount of people for each district (as integer), grid of all electoral
zone as list of lists of units (each unit is [Yellow-voters, Blue-voters])).

Output: A list of strings. The same letters of string represents units of the same district.
If candidate Yellow can not win, return empty list [].

Examples:

unfair_districts(5, [[[2, 1], [1, 1], [1, 2]],
                     [[2, 1], [1, 1], [0, 2]]]) == ['AAC',
                                                    'BBC']


unfair_districts(9, [[[0, 3], [3, 3], [1, 1]],
                     [[1, 2], [1, 0], [1, 1]],
                     [[0, 3], [2, 1], [2, 2]]]) == ['ABB',
                                                    'ABC',
                                                    'ACC']

Here is the explanation of the first example. "A", "B", "C" are districts names
(you may use any: 'a', 'b', 'c'... or '1', '2', '3'... - the checker just regards
the same letter as one district). We have 3 united districts, each of them has 2 units
inside with following coordinates (row, column): "A" = 0,0 and 0,1; "B" = 1,0
and 1,1; "C" = 0,2 and 1,2. Every district has the same total amount of people - 5
and all units belonging to the same district are connected. Districts "A" and "B" are
yellow, since there are more people in each district voted for Yellow candidate (3:2).
The same is with district "C" (more for Blue candidate - 1:4). So there are two districts
for Yellow and one for Blue - this splitting variant is a valid solution.

Preconditions:
2 ≤ grid_rows, grid_columns ≤ 6;
4 ≤ grid_rows * grid_columns ≤ 25;
Total_population % amount_of_people == 0;
Total_population == sum(sum(unit) for unit in chain(*grid));
0 ≤ each_votes ≤ 9.

----------
----------

El gerrymandering es una práctica que pretende establecer una ventaja política para un
partido o grupo concreto manipulando los límites de los distritos. El distrito resultante
se conoce como gerrymander (/ˈdʒɛriˌmændər/); sin embargo, esa palabra también puede referirse
al proceso. El término gerrymandering tiene connotaciones negativas. En el gerrymandering se
utilizan dos tácticas principales: "cracking" (es decir, diluir el poder de voto de los partidarios
del partido contrario en muchos distritos) y "packing" (concentrar el poder de voto del partido
contrario en un distrito para reducir su poder de voto en otros distritos).

Además de para lograr los resultados electorales deseados para un partido concreto, el gerrymandering
puede utilizarse para ayudar o perjudicar a un grupo demográfico concreto, como un grupo político,
étnico, racial, lingüístico, religioso o de clase, como en el caso de los distritos electorales
federales de EE.UU. que producen una mayoría de electores afroamericanos o de otras minorías raciales,
conocidos como "distritos de minorías mayoritarias". El gerrymandering también puede utilizarse para
proteger a los titulares.

Más información en wikipedia o en el episodio Gerrymandering: Last Week Tonight con John Oliver (HBO)

Tienes un mapa de unidades. Cada unidad tiene dos elementos (cantidad de personas que han votado al
candidato amarillo y cantidad de personas que han votado al candidato azul). Tu misión es dividir el
área dada en X cantidad de distritos de tal manera que el candidato Amarillo obtenga más distritos
votados a su favor que el candidato Azul.

Hay dos reglas principales para construir distritos

todos los distritos deben tener la misma cantidad de habitantes;
todas las unidades deben estar conectadas dentro de un mismo distrito.
El resultado consiste esencialmente en etiquetar cada unidad con una letra, las unidades con la
misma letra se convertirían en un distrito post-gerrymander. La población de las unidades originales
con la misma etiqueta se fusionaría en el nuevo distrito post-gerrymander. El objetivo del
gerrymandering es asegurarse de que si las elecciones se celebrasen en estos nuevos distritos,
ganaría el candidato amarillo.

Entrada: Dos argumentos. Cantidad de personas para cada distrito (como entero), cuadrícula de
toda la zona electoral como lista de listas de unidades (cada unidad es [Votantes-Amarillos,
Votantes-Azules]).

Salida: Una lista de cadenas. Las mismas letras de cadena representan unidades del mismo
distrito. Si el candidato Amarillo no puede ganar, devuelve una lista vacía [].

Ejemplos:

distritos_injustos(5, [[[2, 1], [1, 1], [1, 2]],
                     [[2, 1], [1, 1], [0, 2]]) == ['AAC',
                                                    'BBC']


distritos_injustos(9, [[[0, 3], [3, 3], [1, 1]],
                     [[1, 2], [1, 0], [1, 1]],
                     [[0, 3], [2, 1], [2, 2]]) == ['ABB',
                                                    'ABC',
                                                    'ACC']

He aquí la explicación del primer ejemplo. "A", "B", "C" son nombres de distritos
(puede utilizar cualquiera: 'a', 'b', 'c'... o '1', '2', '3'... - el corrector sólo
considera la misma letra como un distrito). Tenemos 3 distritos unidos, cada uno de
ellos tiene 2 unidades dentro con las siguientes coordenadas (fila, columna): "A" = 0,0 y 0,1;
"B" = 1,0 y 1,1; "C" = 0,2 y 1,2. Cada distrito tiene la misma cantidad total de personas: 5,
y todas las unidades que pertenecen al mismo distrito están conectadas. Los distritos "A" y "B"
son amarillos, ya que hay más personas en cada distrito que han votado al candidato amarillo (3:2).
Lo mismo ocurre con el distrito "C" (más para el candidato Azul - 1:4). Así que hay dos distritos
para el amarillo y uno para el azul: esta variante de división es una solución válida.

Precondiciones:
2 ≤ cuadrícula_filas, cuadrícula_columnas ≤ 6;
4 ≤ filas_rejilla * columnas_rejilla ≤ 25;
Población_total % cantidad_de_personas == 0;
Población_total == sum(sum(unidad) for unidad in cadena(*rejilla));
"""


import numpy as np
from copy import deepcopy

record = 0
row = 0
column = 0
people = 0
groups = 0
units = []
it = 0
record = 0


class unit:
    def __init__(self, x, y, win, loss):
        self.x = x
        self.y = y
        self.win = win
        self.loss = loss
        self.t = self.win + self.loss


class group:
    def __init__(self):
        self.l = []
        self.wins = 0
        self.losses = 0
        self.state = 0
        self.t = 0

    def add(self, unit):
        self.l.append(unit)
        self.wins += unit.win
        self.losses += unit.loss
        self.t += unit.t
        if self.wins > self.losses:
            self.state = 1
        elif self.wins == self.losses:
            self.state = 0
        else:
            self.state = -1


def search(group, record):
    if group.t == people:
        return [[group, record]]

    temp_list = []
    result = []
    for i in group.l:
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            if i.x + dx >= 0 and i.x + dx < row and i.y + dy >= 0 and i.y + dy < column:
                if (not record[(i.x + dx, i.y + dy)]) and (
                    (i.x + dx, i.y + dy) not in temp_list
                ):
                    temp_list.append((i.x + dx, i.y + dy))

    for x, y in temp_list:
        if group.t + units[x][y].t > people:
            continue
        else:
            temp_group = deepcopy(group)
            temp_group.add(units[x][y])
            temp_record = deepcopy(record)
            temp_record[(x, y)] = 1
            result += search(temp_group, temp_record)

    return result


def solve(solution):
    temp_solution = []

    for [temp_groups, record] in solution:
        temp_group = group()
        for j, k in zip(it[0].flatten(), it[1].flatten()):
            if not record[(j, k)]:
                temp_group.add(units[j][k])
                temp_record = deepcopy(record)
                temp_record[(j, k)] = 1
                break
        for i in search(temp_group, temp_record):
            temp_solution.append([temp_groups + [i[0]], i[1]])

    return temp_solution


def unfair_districts(amount_of_people, grid):
    global record, row, column, people, units, groups, it
    row = len(grid)
    column = len(grid[0])
    it = np.mgrid[0:row, 0:column]
    record = np.zeros((row, column), dtype=int)
    people = amount_of_people
    units = []

    # build grid of units
    for i in range(row):
        units.append([])
        for j in range(column):
            units[-1].append(unit(i, j, grid[i][j][0], grid[i][j][1]))

    # calculate number of groups
    s = 0
    for i, j in zip(it[0].flatten(), it[1].flatten()):
        s += units[i][j].t
    groups = int(s / people)

    result = [[[], record]]
    for i in range(groups):
        result = solve(result)

    for [solution, record] in result:
        if len(solution) == groups:
            win = 0
            loss = 0
            for i in solution:
                if i.state == 1:
                    win += 1
                elif i.state == -1:
                    loss += 1
            if win > loss:
                final = ["0" * column] * row
                for i in range(groups):
                    for j in solution[i].l:
                        final[j.x] = final[j.x][: j.y] + str(i) + final[j.x][j.y + 1 :]
                return final

    return []


if __name__ == "__main__":
    from itertools import chain
    from collections import defaultdict

    def checker(solution, amount_of_people, grid, win_flg=True):
        w, h = len(grid[0]), len(grid)
        size = w * h
        cell_dic = {}

        # make cell_dic
        def adj_cells(cell):
            result = []
            if cell % w != 1 and cell - 1 > 0:
                result.append(cell - 1)
            if cell % w and cell + 1 <= size:
                result.append(cell + 1)
            if (cell - 1) // w:
                result.append(cell - w)
            if (cell - 1) // w < h - 1:
                result.append(cell + w)
            return set(result)

        for i, v in enumerate(chain(*grid)):
            cell_dic[i + 1] = {"vote": v, "adj": adj_cells(i + 1)}

        answer = solution(amount_of_people, grid)

        if answer == [] and not win_flg:
            return True

        if not isinstance(answer, list):
            print("wrong data type :", answer)
            return False
        else:
            if len(answer) != h:
                print("wrong data length", answer)
                return False
            for an in answer:
                if len(an) != w:
                    print("wrong data length", an)
                    return False

        ds_dic = defaultdict(list)
        for i, r in enumerate("".join(answer), start=1):
            ds_dic[r].append(i)

        # answer check
        def district_check(d):
            all_cells = set(d[1:])
            next_cells = cell_dic[d[0]]["adj"] & set(d)
            for _ in range(len(d)):
                all_cells -= next_cells
                next_cells = set(
                    chain(*[list(cell_dic[nc]["adj"]) for nc in next_cells])
                ) & set(d)
            return not all_cells

        for ch, cells in ds_dic.items():
            dist_people = sum(sum(cell_dic[c]["vote"]) for c in cells)
            if not district_check(cells):
                print("wrong district: ", ch)
                return False
            if dist_people != amount_of_people:
                print("wrong people:", ch)
                return False

        # win check
        win, lose = 0, 0
        for part in ds_dic.values():
            vote_a, vote_b = 0, 0
            for p in part:
                a, b = cell_dic[p]["vote"]
                vote_a += a
                vote_b += b
            win += vote_a > vote_b
            lose += vote_a < vote_b

        return win > lose

    assert checker(
        unfair_districts, 5, [[[2, 1], [1, 1], [1, 2]], [[2, 1], [1, 1], [0, 2]]]
    ), "3x2grid"

    assert checker(
        unfair_districts,
        9,
        [[[0, 3], [3, 3], [1, 1]], [[1, 2], [1, 0], [1, 1]], [[0, 3], [2, 1], [2, 2]]],
    ), "3x3gid"

    assert checker(
        unfair_districts,
        8,
        [
            [[1, 1], [2, 0], [2, 0], [3, 3]],
            [[1, 1], [1, 2], [1, 1], [0, 3]],
            [[1, 1], [1, 1], [1, 2], [0, 3]],
            [[1, 1], [1, 1], [1, 1], [2, 0]],
        ],
    ), "4x4gid"

    print("check done")
