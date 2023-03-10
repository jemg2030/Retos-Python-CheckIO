'''
Greetings, adventurer! You are now at the beginning of a dangerous but at the same time a very exciting
journey, during which you’ll have to solve many riddles, neutralize several traps, and outrun your pursuers…
And all this for the sole purpose of finding one of the most valuable artifacts in the universe, the source
of the infinite energy - the Hypercube.

The Hypercube is located in the very center of the castle, built by the eccentric Lord Escher a couple of
centuries ago. This man built his castle on the island due to his high appreciation for the solitude. Ever
since he died (under the very mysterious circumstances), and his servants who have returned to the continent
told the world about the strange things and phenomena happening there, many of the research expeditions and
groups of treasure hunters went there. But none of them have ever returned...

Good luck, buddy! Perhaps you are bound to have more luck than others.

So, the things are packed, equipment gathered and it's high time to hit the road. Currently you are on the
continent, standing in the port. Foreseeing the danger you might be facing on the island, you’ve decided not
}to go there alone, but to recruit a team and equip 2 ships. Your only goal is to get hold of a Cube, the other
treasures that you are hoping to find will be considered the payment for the team.

And the first task is simple - you have to divide all your crew members into 2 teams (for the 2 ships).
You have to divide all your crew members into 2 teams with the next rules: those who are elder than 40 y.o. or
younger than 20, should be on the first ship and all the others - on the second. It will helps the young
sailors gain the experience of the elder collegues. The input data will be the dictionary where keys will be
the surnames of the sailors and the values will be their ages. After the crew formating, you should sort all of
the sailors in the alphabetical order in the each list of surnames.

Input: Dictionary with the sailors and their ages.

Output: List of the lists with 2 teams.

Example:
two_teams({
    'Smith': 34,
    'Wesson': 22,
    'Coleman': 45,
    'Abrahams': 19}) == [
        ['Abrahams', 'Coleman'],
        ['Smith', 'Wesson']
    ]

How it is used: For splitting objects to the few roughly equivalent groups.

Precondition :
1 <= amount of the sailors <= 100

----------
----------

¡Saludos, aventurero! Te encuentras al principio de un viaje peligroso y emocionante a la vez.
durante el cual tendrás que resolver muchos enigmas, neutralizar varias trampas y dejar atrás a tus perseguidores...
Y todo ello con el único propósito de encontrar uno de los artefactos más valiosos del universo, la fuente
de la energía infinita: el Hipercubo.

El Hipercubo se encuentra en el centro del castillo, construido por el excéntrico Lord Escher hace un par de siglos.
siglos atrás. Este hombre construyó su castillo en la isla debido a su gran aprecio por la soledad. Siempre
desde que murió (en circunstancias muy misteriosas), y sus sirvientes que han regresado al continente
contaron al mundo las extrañas cosas y fenómenos que allí ocurrían, muchas de las expediciones de investigación y
grupos de cazadores de tesoros fueron allí. Pero ninguno de ellos ha regresado jamás...

¡Buena suerte, amigo! Quizá tú tengas más suerte que otros.

Así pues, las cosas están hechas, el equipo recogido y ya es hora de ponerse en camino. En este momento estás en el
continente, de pie en el puerto. Previendo el peligro al que te podrías enfrentar en la isla, has decidido no
ir solo, sino reclutar un equipo y equipar 2 barcos. Su único objetivo es hacerse con un Cubo, los demás
tesoros que esperas encontrar se considerarán el pago del equipo.

Y la primera tarea es sencilla: tienes que dividir a todos los miembros de tu tripulación en 2 equipos (para las
2 naves).
Tienes que dividir a todos los miembros de tu tripulación en 2 equipos con las siguientes reglas: los que tengan
más de 40 años o menores de 20, deben estar en el primer barco y todos los demás - en el segundo. Esto ayudará a
los jóvenes experiencia de los compañeros mayores. Los datos de entrada serán un diccionario cuyas claves serán
los apellidos de los marineros y los valores serán sus edades. Después de la formación de la tripulación, debe
ordenar todos los marineros por orden alfabético en cada lista de apellidos.

Entrada: Diccionario con los marineros y sus edades.

Salida: Listado de las listas con 2 equipos.

Ejemplo:
dos_equipos({
    'Smith': 34,
    'Wesson': 22,
    'Coleman': 45,
    'Abrahams': 19}) == [
        ['Abrahams', 'Coleman'],
        ['Smith', 'Wesson']
    ]

Cómo se utiliza: Para dividir objetos en los pocos grupos aproximadamente equivalentes.

Precondición :
1 <= cantidad de los marineros <= 100
'''


def two_teams(sailors):
    #replace this for solution
    team1 = []
    team2 = []

    for name, age in sailors.items():
        if age > 40 or age < 20:
            team1.append(name)
        else:
            team2.append(name)

    team1.sort()
    team2.sort()

    return [team1, team2]

if __name__ == '__main__':
    print("Example:")
    print(two_teams({'Smith': 34, 'Wesson': 22, 'Coleman': 45, 'Abrahams': 19}))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert two_teams({
        'Smith': 34,
        'Wesson': 22,
        'Coleman': 45,
        'Abrahams': 19}) == [
            ['Abrahams', 'Coleman'],
            ['Smith', 'Wesson']
            ]

    assert two_teams({
        'Fernandes': 18,
        'Johnson': 22,
        'Kale': 41,
        'McCortney': 54}) == [
            ['Fernandes', 'Kale', 'McCortney'],
            ['Johnson']
            ]
    print("Coding complete? Click 'Check' to earn cool rewards!")
