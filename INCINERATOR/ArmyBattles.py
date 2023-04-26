'''
...Sir Ronald’s opponent - Umbert, has proved to be a very skillful warrior. In addition, he was a good
fifteen years younger, which gave him a certain advantage. But Sir Ronald was also very strong - he had
the experience of participation in many battles and in several major wars behind his back. And besides
that, in his youth he was known as the best duelist in this land.
Realizing that the forces are equal, each of them had followed the only course possible - to call for
help. Umbert sent for the reinforcement his coachman on a horse, and Sir Ronald used a family horn that
sounded more than once in hot battles. The knight's castle was close enough for the call to arms was
heard back there. Nobody quite knew where the Umbert's accomplices were located, and this made it
difficult to come up with a strategy for the battle ahead.
Fortunately, the reinforcements for both sides arrived almost simultaneously. Now it was more than
a question of the girl's honor. There was no peaceful solutions to this matter. One of the two armies
must be destroyed.
In the previous mission - Warriors - you've learned how to make a duel between 2 warriors happen.
Great job! But let's move to something that feels a little more epic - the armies! In this mission
your task is to add new classes and functions to the existing ones. The new class should be the Army
and have the method add_units() - for adding the chosen amount of units to the army. The first unit
added will be the first to go to fight, the second will be the second, ...
Also you need to create a Battle() class with a fight() function, which will determine the strongest army.
The battles occur according to the following principles:
at first, there is a duel between the first warrior of the first army and the first warrior of the
second army. As soon as one of them dies - the next warrior from the army that lost the fighter enters
the duel, and the surviving warrior continues to fight with his current health. This continues until
all the soldiers of one of the armies die. In this case, the fight() function should return True, if the
first army won, or False, if the second one was stronger.
Note that army 1 have the advantage to start every fight!

Example:
chuck = Warrior()
bruce = Warrior()
carl = Knight()
dave = Warrior()
mark = Warrior()

fight(chuck, bruce) == True
fight(dave, carl) == False
chuck.is_alive == True
bruce.is_alive == False
carl.is_alive == True
dave.is_alive == False
fight(carl, mark) == False
carl.is_alive == False

my_army = Army()
my_army.add_units(Knight, 3)

enemy_army = Army()
enemy_army.add_units(Warrior, 3)

army_3 = Army()
army_3.add_units(Warrior, 20)
army_3.add_units(Knight, 5)

army_4 = Army()
army_4.add_units(Warrior, 30)

battle = Battle()

battle.fight(my_army, enemy_army) == True
battle.fight(army_3, army_4) == False

Input: The warriors and armies.

Output: The result of the battle (True or False).

How it is used: For computer games development.

Precondition:
2 types of units
For all battles, each army is obviously not empty at the beginning.

----------
----------

...El oponente de Sir Ronald - Umbert, ha demostrado ser un guerrero muy hábil. Además, era unos
quince años más joven, lo que le daba cierta ventaja. Pero Sir Ronald también era muy fuerte: tenía
a sus espaldas la experiencia de haber participado en muchas batallas y en varias guerras importantes.
Y además, en su juventud era conocido como el mejor duelista de estas tierras.
Al darse cuenta de que las fuerzas son iguales, cada uno de ellos había seguido el único curso posible -
para pedir ayuda. Umbert envió como refuerzo a su cochero a caballo, y Sir Ronald utilizó un cuerno
familiar que sonó más de una vez en batallas encarnizadas. El castillo del caballero estaba lo
suficientemente cerca como para que la llamada a las armas se oyera allí. Nadie sabía muy bien dónde se
encontraban los cómplices de Umbert, y esto dificultaba la elaboración de una estrategia para la batalla
que se avecinaba.
Afortunadamente, los refuerzos de ambos bandos llegaron casi simultáneamente. Ahora era algo más que una
cuestión de honor de la chica. No había soluciones pacíficas para este asunto. Uno de los dos ejércitos debe
ser destruido.
En la misión anterior - Guerreros - has aprendido cómo hacer que se produzca un duelo entre 2 guerreros.
¡Buen trabajo! Pero pasemos a algo que parece un poco más épico: ¡los ejércitos! En esta misión tu tarea es
añadir nuevas clases y funciones a las ya existentes. La nueva clase debe ser el Ejército y tener el método
add_units() - para añadir la cantidad elegida de unidades al ejército. La primera unidad añadida será la primera
en ir a luchar, la segunda será la segunda, ...
También necesitas crear una clase Battle() con una función fight(), que determinará el ejército más fuerte.
Las batallas ocurren de acuerdo a los siguientes principios:
al principio, hay un duelo entre el primer guerrero del primer ejército y el primer guerrero del segundo ejército.
Tan pronto como uno de ellos muere - el siguiente guerrero del ejército que perdió al luchador entra en el duelo,
y el guerrero superviviente continúa luchando con su salud actual. Esto continúa hasta que todos los soldados
de uno de los ejércitos mueren. En este caso, la función fight() debería devolver True, si el primer ejército
ganó, o False, si el segundo fue más fuerte.
Ten en cuenta que el ejército 1 tiene ventaja al principio de cada combate.

Ejemplo:
chuck = Guerrero()
bruce = Guerrero()
carl = Caballero()
dave = Guerrero()
mark = Guerrero()

fight(chuck, bruce) == True
fight(dave, carl) == False
chuck.is_alive == True
bruce.is_alive == False
carl.is_alive == True
dave.is_alive == Falso
fight(carl, mark) == Falso
carl.is_alive == False

mi_ejército = Ejército()
mi_ejército.add_units(Caballero, 3)

ejército_enemigo = Ejército()
ejército_enemigo.add_units(Guerrero, 3)

ejército_3 = Ejército()
army_3.add_units(Guerrero, 20)
army_3.add_units(Caballero, 5)

army_4 = Ejército()
army_4.add_units(Guerrero, 30)

batalla = Batalla()

battle.fight(mi_ejército, enemigo_ejército) == True
battle.fight(ejército_3, ejército_4) == False

Entrada: Los guerreros y los ejércitos.

Salida: El resultado de la batalla (Verdadero o Falso).

Cómo se utiliza: Para el desarrollo de juegos de ordenador.

Precondición:
2 tipos de unidades
Para todas las batallas, cada ejército obviamente no está vacío al principio.
'''


# Taken from mission The Warriors

class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
        self.is_alive = True


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 50
        self.attack = 7
        self.is_alive = True


class Army:
    def __init__(self):
        self.warriors = 0
        self.knights = 0

    def add_units(self, unit, numbers):
        if unit == Warrior:
            self.warriors += numbers
        elif unit == Knight:
            self.knights += numbers


class Battle:
    pass

    def fight(self, army1, army2):
        if army1.warriors > 0:
            fighter1 = Warrior()
            army1.warriors -= 1
        else:
            fighter1 = Knight()
            army1.knights -= 1
        if army2.warriors > 0:
            fighter2 = Warrior()
            army2.warriors -= 1
        else:
            fighter2 = Knight()
            army2.knights -= 1
        while True:
            if fight(fighter1, fighter2):
                if army2.warriors > 0:
                    fighter2 = Warrior()
                    army2.warriors -= 1
                elif army2.knights > 0:
                    fighter2 = Knight()
                    army2.knights -= 1
                else:
                    return True
            else:
                if army1.warriors > 0:
                    fighter1 = Warrior()
                    army1.warriors -= 1
                elif army1.knights > 0:
                    fighter1 = Knight()
                    army1.knights -= 1
                else:
                    return False


def fight(unit_1, unit_2):
    while True:
        unit_2.health -= unit_1.attack
        if unit_2.health <= 0:
            unit_2.is_alive = False
            return True
        unit_1.health -= unit_2.attack
        if unit_1.health <= 0:
            unit_1.is_alive = False
            return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()

    bruce = Warrior()

    carl = Knight()

    dave = Warrior()

    mark = Warrior()

    assert fight(chuck, bruce) == True

    assert fight(dave, carl) == False

    assert chuck.is_alive == True

    assert bruce.is_alive == False

    assert carl.is_alive == True

    assert dave.is_alive == False

    assert fight(carl, mark) == False

    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    # battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)

    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")
