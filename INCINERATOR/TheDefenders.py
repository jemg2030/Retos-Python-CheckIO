"""
...the clashes between different soldiers occurred here and there, and the new troops kept
coming. The conflict gradually was starting to look more like a small war.
"Knights, hear my command! Take your shields! Strengthen the armor! We are taking too much
beating," - Sir Ronald shouted.
Nobody’s expected that Umbert's soldiers could compete with the well-trained knights, so at
the beginning of the battle the knights used exclusively two-handed swords - no one even thought
of being on the defensive. But it seems that it's time to back down and take one-handed swords
and shields instead of the former deadly weapons. This will slightly reduce the assault capacity
of knights, but will allow them to better defend themselves against the dangerous attacks of enemy
soldiers.
In the previous mission - Army battles, you've learned how to make a battle between 2 armies. But we
have only 2 types of units - the Warriors and Knights. Let's add another one - the Defender. It should
be the subclass of the Warrior class and have an additional defense parameter, which helps him to survive
longer. When another unit hits the defender, he loses a certain amount of his health according to the
next formula: enemy attack - self defense (if enemy attack > self defense). Otherwise, the defender
doesn't lose his health.

The basic parameters of the Defender:
health = 60
attack = 3
defense = 2

Example:
chuck = Warrior()
bruce = Warrior()
carl = Knight()
dave = Warrior()
mark = Warrior()
bob = Defender()
mike = Knight()
rog = Warrior()
lancelot = Defender()

fight(chuck, bruce) == True
fight(dave, carl) == False
chuck.is_alive == True
bruce.is_alive == False
carl.is_alive == True
dave.is_alive == False
fight(carl, mark) == False
carl.is_alive == False
fight(bob, mike) == False
fight(lancelot, rog) == True

my_army = Army()
my_army.add_units(Defender, 1)

enemy_army = Army()
enemy_army.add_units(Warrior, 2)

army_3 = Army()
army_3.add_units(Warrior, 1)
army_3.add_units(Defender, 1)

army_4 = Army()
army_4.add_units(Warrior, 2)

battle = Battle()

battle.fight(my_army, enemy_army) == False
battle.fight(army_3, army_4) == True

Input: The warriors and armies.

Output: The result of the battle (True or False).

How it is used: For the computer games development.

Note: From now on, the tests from "check" part will use another type of warrior: the rookie. Its code is

class Rookie(Warrior):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.health = 50
        self.attack = 1

Precondition: 3 types of units

----------
----------

...los enfrentamientos entre diferentes soldados se sucedían aquí y allá, y las nuevas tropas
seguían llegando. El conflicto poco a poco empezaba a parecerse más a una pequeña guerra.
"¡Caballeros, escuchad mi orden! ¡Coged vuestros escudos! ¡Reforzad las armaduras! Estamos
recibiendo demasiados golpes", gritó Sir Ronald.
Nadie esperaba que los soldados de Umbert pudieran competir con los bien entrenados caballeros,
así que al principio de la batalla los caballeros usaron exclusivamente espadas de dos manos -
nadie pensó siquiera en estar a la defensiva. Pero parece que ha llegado el momento de dar marcha
atrás y tomar espadas de una mano y escudos en lugar de las anteriores armas mortíferas. Esto
reducirá ligeramente la capacidad de asalto de los caballeros, pero les permitirá defenderse mejor
de los peligrosos ataques de los soldados enemigos.
En la misión anterior - Batallas de ejércitos, has aprendido cómo hacer una batalla entre 2 ejércitos.
Pero sólo tenemos 2 tipos de unidades - los Guerreros y Caballeros. Vamos a añadir otro - el Defensor.
Debería ser la subclase de la clase Guerrero y tener un parámetro de defensa adicional, que le ayude a
sobrevivir más tiempo. Cuando otra unidad golpea al defensor, éste pierde una cierta cantidad de su salud
según la siguiente fórmula: ataque enemigo - defensa propia (si ataque enemigo > defensa propia). En
caso contrario, el defensor no pierde su salud.
Los parámetros básicos del Defensor
salud = 60
ataque = 3
defensa = 2

Ejemplo
chuck = Guerrero()
bruce = Guerrero()
carl = Caballero()
dave = Guerrero()
mark = Guerrero()
bob = Defensor()
mike = Caballero()
rog = Guerrero()
lancelot = Defensor()

fight(chuck, bruce) == True
fight(dave, carl) == False
chuck.is_alive == True
bruce.is_alive == False
carl.is_alive == True
dave.is_alive == Falso
fight(carl, mark) == Falso
carl.is_alive == Falso
fight(bob, mike) == Falso
fight(lancelot, rog) == True

mi_ejército = Ejército()
mi_ejército.add_units(Defensor, 1)

ejército_enemigo = Ejército()
ejército_enemigo.add_units(Guerrero, 2)

ejército_3 = Ejército()
army_3.add_units(Guerrero, 1)
army_3.add_units(Defensor, 1)

army_4 = Ejército()
army_4.add_units(Guerrero, 2)

batalla = Batalla()

battle.fight(mi_ejército, enemigo_ejército) == False
battle.fight(ejercito_3, ejercito_4) == True

Entrada: Los guerreros y ejércitos.

Salida: El resultado de la batalla (Verdadero o Falso).

Cómo se utiliza: Para el desarrollo de juegos de ordenador.

Nota: A partir de ahora, las pruebas de la parte "comprobar" utilizarán otro tipo de guerrero:
el novato. Su código es

clase Novato(Guerrero):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        auto.salud = 50
        auto.ataque = 1

Condición previa: 3 tipos de unidades
"""


class Warrior:
    def __init__(self, health=50, attack=5, defense=0):
        self.health = health
        self.attack = attack
        self.defense = defense

    @property
    def is_alive(self):
        return self.health > 0

    def hit_by(self, other):
        self.health -= max(0, other.attack - self.defense)
        return self


class Knight(Warrior):
    def __init__(self):
        super().__init__(attack=7)


class Defender(Warrior):
    def __init__(self):
        super().__init__(health=60, attack=3, defense=2)


def fight(unit1, unit2):
    attacker, defender = unit1, unit2
    while attacker.is_alive:
        attacker, defender = defender.hit_by(attacker), attacker
    return unit1.is_alive


class Army:
    def __init__(self):
        self._troops = []

    def add_units(self, unit_type, number):
        for _ in range(number):
            self._troops.append(unit_type())

    def __bool__(self):
        return any(fighter.is_alive for fighter in self._troops)

    def get_fighter(self):
        while self._troops:
            if self._troops[-1].is_alive:
                return self._troops[-1]
            else:
                self._troops.pop()  # remove dead
        return None


class Battle:
    @staticmethod
    def fight(attacker_army, defender_army):
        while attacker_army:
            attacker = attacker_army.get_fighter()
            defender = defender_army.get_fighter()
            if defender is None:
                return True
            fight(attacker, defender)
        return False


if __name__ == "__main__":
    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 1)

    army_4 = Army()
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")
