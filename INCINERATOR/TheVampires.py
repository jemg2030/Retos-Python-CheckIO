"""
The flocks of crows circled over the battlefield. Many brave warriors have fallen in this battle,
many have continued to fight.
"If this goes on, we’ll simply kill each other, and there will be no winners - we’ll all lose." -
reflected Sir Ronald, watching a bleak picture in front of him.
"I have to make an important decision. I know what it’ll cost, but now that’s the only thing that
can save us all..."
A long time ago, when he was often in search of trouble and adventure, he went to hunt a witch who
had a huge bounty on her head. The bloody creature was able to save her life by persuading the knight
to take a gift from her - a vial of vampire blood. This blood poured into the dying man’s mouth could
bring him back to life in vampire form.
Is it really the day when he has to use it?..
It seemed to be the only way to win this battle.
Sir Ronald began to lean over the barely living bodies of his knights, who were lying beside him. To
each of them he said:
- "Drink. You’ll be given a new life..."
So we have 3 types of units: the Warrior, Knight and Defender. Let's make the battles even more epic
and add another type - the Vampire!
Vampire should be the subclass of the Warrior class and have the additional vampirism parameter, which
helps him to heal himself. When the Vampire hits the other unit, he restores his health by +50% of the
dealt damage (enemy defense makes the dealt damage value lower).
The basic parameters of the Vampire:
health = 40
attack = 4
vampirism = 50%
You should store vampirism attribute as an integer (50 for 50%). It will be needed to make this solution
evolutes to fit one of the next challenges of this saga.

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
eric = Vampire()
adam = Vampire()
richard = Defender()
ogre = Warrior()

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
fight(eric, richard) == False
fight(ogre, adam) == True

my_army = Army()
my_army.add_units(Defender, 2)
my_army.add_units(Vampire, 2)
my_army.add_units(Warrior, 1)

enemy_army = Army()
enemy_army.add_units(Warrior, 2)
enemy_army.add_units(Defender, 2)
enemy_army.add_units(Vampire, 3)

army_3 = Army()
army_3.add_units(Warrior, 1)
army_3.add_units(Defender, 4)

army_4 = Army()
army_4.add_units(Vampire, 3)
army_4.add_units(Warrior, 2)

battle = Battle()

battle.fight(my_army, enemy_army) == False
battle.fight(army_3, army_4) == True

Input: The warriors and armies.

Output: The result of the battle (True or False).

How it is used: For the computer games development.

Precondition: 4 types of units

----------
----------

Las bandadas de cuervos volaban en círculos sobre el campo de batalla. Muchos valientes
guerreros han caído en esta batalla, muchos han seguido luchando.
"Si esto sigue así, simplemente nos mataremos unos a otros, y no habrá vencedores: todos
perderemos". - reflexionó Sir Ronald, observando un panorama desolador frente a él.
"Tengo que tomar una decisión importante. Sé lo que costará, pero ahora es lo único que
puede salvarnos a todos..."
Hace mucho tiempo, cuando solía buscar problemas y aventuras, fue a cazar a una bruja que
tenía una enorme recompensa por su cabeza. La sangrienta criatura consiguió salvar su vida
convenciendo al caballero para que aceptara un regalo de ella: un frasco de sangre de vampiro.
Esta sangre vertida en la boca del moribundo podría devolverle a la vida en forma de vampiro.
¿Será realmente el día en que tenga que usarla?.
Parecía ser la única manera de ganar esta batalla.
Sir Ronald comenzó a inclinarse sobre los cuerpos apenas vivos de sus caballeros, que yacían a
su lado. A cada uno de ellos le dijo:
- "Bebed. Se os dará una nueva vida..."
Así que tenemos 3 tipos de unidades: el Guerrero, el Caballero y el Defensor. Hagamos las batallas
aún más épicas y añadamos otro tipo: ¡el Vampiro!
El Vampiro debería ser la subclase de la clase Guerrero y tener el parámetro adicional Vampirismo,
que le ayuda a curarse a sí mismo. Cuando el Vampiro golpea a la otra unidad, restaura su salud en un
+50% del daño infligido (la defensa enemiga hace que el valor del daño infligido sea menor).
Los parámetros básicos del Vampiro
salud = 40
ataque = 4
vampirismo = 50%
Debes almacenar el atributo vampirismo como un número entero (50 para 50%). Será necesario para que
esta solución evolucione y se adapte a uno de los próximos retos de esta saga.

Ejemplo:
chuck = Guerrero()
bruce = Guerrero()
carl = Caballero()
dave = Guerrero()
mark = Guerrero()
bob = Defensor()
mike = Caballero()
rog = Guerrero()
lancelot = Defensor()
eric = Vampiro()
adam = Vampiro()
richard = Defensor()
ogre = Guerrero()

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
fight(eric, richard) == Falso
fight(ogre, adam) == True

mi_ejército = Ejército()
mi_ejército.add_units(Defensor, 2)
mi_ejército.add_units(Vampiro, 2)
mi_ejército.add_units(Guerrero, 1)

ejército_enemigo = Ejército()
ejército_enemigo.add_units(Guerrero, 2)
ejército_enemigo.add_units(Defensor, 2)
ejército_enemigo.add_units(Vampiro, 3)

ejército_3 = Ejército()
army_3.add_units(Guerrero, 1)
ejército_3.add_units(Defensor, 4)

army_4 = Ejército()
army_4.add_units(Vampiro, 3)
army_4.add_units(Guerrero, 2)

batalla = Batalla()

battle.fight(mi_ejército, enemigo_ejército) == False
battle.fight(ejercito_3, ejercito_4) == True

Entrada: Los guerreros y ejércitos.

Salida: El resultado de la batalla (Verdadero o Falso).

Cómo se utiliza: Para el desarrollo de juegos de ordenador.

Precondición: 4 tipos de unidades
"""


# Taken from mission The Defenders


class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
        self.defence = 0
        self.vampirism = 0

    @property
    def is_alive(self):
        return self.health > 0

    def attacked(self, enemy):
        damage = enemy.attack - self.defence
        if damage > 0:
            self.health -= damage
            enemy.health += damage * enemy.vampirism / 100


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7


class Defender(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 60
        self.attack = 3
        self.defence = 2


class Vampire(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 40
        self.attack = 4
        self.vampirism = 50


class Rookie(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 1


def fight(unit_1, unit_2):
    if unit_1.health * unit_2.health > 0:
        unit_2.attacked(unit_1)
        fight(unit_2, unit_1)
    return unit_1.is_alive


class Army:
    def __init__(self):
        self.warriors = []

    def add_units(self, Warrior, n):
        self.warriors.extend([Warrior() for _ in range(n)])


class Battle:
    def fight(self, army1, army2):
        if len(army1.warriors) * len(army2.warriors) > 0:
            if fight(army1.warriors[0], army2.warriors[0]):
                army2.warriors.pop(0)
            else:
                army1.warriors.pop(0)
            self.fight(army1, army2)
        return army1.warriors != []


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing

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
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()

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
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Warrior, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 4)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")
