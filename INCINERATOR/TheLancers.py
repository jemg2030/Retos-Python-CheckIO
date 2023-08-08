"""
... the vampires fought fiercely. Judging by the course of the battle, Sir Ronald made the right
decision, although not very ethically ambiguous.
Suddenly, new soldiers joined the Umbert’s ranks - has he really got an ace up his sleeve?
Lancers presented the fresh forces, which made Sir Ronald’s position increasingly difficult,
lancers could attack two soldiers at once with their long spears. Something needed to be done with that…
It seems that the Warrior, Knight, Defender and Vampire are not enough to win the battle. Let's add
one more powerful unit type - the Lancer.
Lancer should be the subclass of the Warrior class and should attack in a specific way - when he hits
the other unit, he also deals a 50% of the deal damage to the enemy unit, standing behind the firstly
assaulted one (enemy defense makes the deal damage value lower - consider this).
The basic parameters of the Lancer:
health = 50
attack = 6

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
freelancer = Lancer()
vampire = Vampire()

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
fight(freelancer, vampire) == True
freelancer.is_alive == True

my_army = Army()
my_army.add_units(Defender, 2)
my_army.add_units(Vampire, 2)
my_army.add_units(Lancer, 4)
my_army.add_units(Warrior, 1)

enemy_army = Army()
enemy_army.add_units(Warrior, 2)
enemy_army.add_units(Lancer, 2)
enemy_army.add_units(Defender, 2)
enemy_army.add_units(Vampire, 3)

army_3 = Army()
army_3.add_units(Warrior, 1)
army_3.add_units(Lancer, 1)
army_3.add_units(Defender, 2)

army_4 = Army()
army_4.add_units(Vampire, 3)
army_4.add_units(Warrior, 1)
army_4.add_units(Lancer, 2)

battle = Battle()

battle.fight(my_army, enemy_army) == True
battle.fight(army_3, army_4) == False

Input: The warriors and armies.

Output: The result of the battle (True or False).

How it is used: For computer games development.

Precondition: 5 types of units

----------
----------

... los vampiros lucharon ferozmente. A juzgar por el curso de la batalla, Sir Ronald tomó
la decisión correcta, aunque no muy ambigua desde el punto de vista ético.
De repente, nuevos soldados se unieron a las filas de Umbert - ¿realmente tiene un as bajo la
manga? Los lanceros presentaban las fuerzas frescas, lo que dificultaba cada vez más la posición
de Sir Ronald, los lanceros podían atacar a dos soldados a la vez con sus largas lanzas. Había que
hacer algo con eso...
Parece que el Guerrero, el Caballero, el Defensor y el Vampiro no son suficientes para ganar la
batalla. Añadamos un tipo de unidad más poderoso: el Lancer.
El Lancero debería ser la subclase de la clase Guerrero y debería atacar de una manera específica -
cuando golpea a la otra unidad, también inflige un 50% del daño infligido a la unidad enemiga, que se
encuentra detrás de la primera asaltada (la defensa enemiga hace que el valor del daño infligido sea
menor - tenlo en cuenta).
Los parámetros básicos del Lancer:
salud = 50
ataque = 6

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
freelancer = Lancer()
vampiro = Vampiro()

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
fight(ogro, adam) == True
fight(freelancer, vampiro) == True
freelancer.is_alive == True

mi_ejército = Ejército()
mi_ejército.add_units(Defensor, 2)
mi_ejército.add_units(Vampiro, 2)
mi_ejército.add_units(Lancer, 4)
mi_ejército.add_units(Guerrero, 1)

ejército_enemigo = Ejército()
ejército_enemigo.add_units(Guerrero, 2)
ejército_enemigo.add_units(Lancer, 2)
ejército_enemigo.add_units(Defensor, 2)
ejército_enemigo.add_units(Vampiro, 3)

ejército_3 = Ejército()
army_3.add_units(Guerrero, 1)
army_3.add_units(Lancer, 1)
army_3.add_units(Defensor, 2)

army_4 = Ejército()
army_4.add_units(Vampiro, 3)
army_4.add_units(Guerrero, 1)
army_4.add_units(Lancer, 2)

batalla = Batalla()

battle.fight(mi_ejército, enemigo_ejército) == True
battle.fight(ejercito_3, ejercito_4) == False

Entrada: Los guerreros y ejércitos.

Salida: El resultado de la batalla (Verdadero o Falso).

Cómo se utiliza: Para el desarrollo de juegos de ordenador.

Precondición: 5 tipos de unidades
"""


class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5

    @property
    def is_alive(self):
        return self.health > 0

    def take_hit(self, hit):
        self.health -= hit
        return hit

    def do_attack(self, other1, other2=None, **options):
        hit = options.get("hit", self.attack)
        return other1.take_hit(hit)


class Lancer(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 50
        self.attack = 6

    def do_attack(self, other1, other2=None, **options):
        damage = super().do_attack(other1)
        damage2 = super().do_attack(other2, None, hit=damage / 2) if other2 else 0
        return damage + damage2


class Vampire(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 40
        self.attack = 4
        self.vampirism = 0.5

    def do_attack(self, other1, other2=None, **options):
        damage = super().do_attack(other1)
        self.health += damage * self.vampirism
        return damage


class Defender(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 60
        self.attack = 3
        self.defense = 2

    def take_hit(self, hit):
        return super().take_hit(max(0, hit - self.defense))


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7


def fight(unit_1, unit_2):
    while True:
        unit_1.do_attack(unit_2)
        if not unit_2.is_alive:
            return True
        unit_2.do_attack(unit_1)
        if not unit_1.is_alive:
            return False


class Army:
    def __init__(self):
        self.units = []

    def add_units(self, klass, count):
        for i in range(count):
            self.units.append(klass())

    def cleanup(self):
        front_warrior_dead = self.units and not self.units[0].is_alive
        self.units = [u for u in self.units if u.is_alive]
        return front_warrior_dead

    def all_dead(self):
        return self.units == []


class Battle:
    def fight(self, army1, army2):
        army1_turn = True
        while not army1.all_dead() and not army2.all_dead():
            if army1_turn:
                army1.units[0].do_attack(*army2.units[:2])
            else:
                army2.units[0].do_attack(*army1.units[:2])
            army1_turn = not army1_turn

            front_warrior_dead1 = army1.cleanup()
            front_warrior_dead2 = army2.cleanup()
            if front_warrior_dead1 or front_warrior_dead2:
                # If front warrior died, always restart battle with first army.
                army1_turn = True

        return army2.all_dead()


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
    freelancer = Lancer()
    vampire = Vampire()

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
    assert fight(freelancer, vampire) == True
    assert freelancer.is_alive == True

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Lancer, 4)
    my_army.add_units(Warrior, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Lancer, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Lancer, 1)
    army_3.add_units(Defender, 2)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 1)
    army_4.add_units(Lancer, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False

    print("Coding complete? Let's try tests!")
