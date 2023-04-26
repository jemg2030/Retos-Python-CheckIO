'''
One day, on a typical spring afternoon, Sir Ronald has been looking around his land, riding a horse.
Nothing foretold troubles, when suddenly Sir Ronald heard a scream for help, coming from somewhere nearby:
- "Help! Help!" - shouted a piercing young girl's voice.
As a true knight, Sir Ronald couldn’t stay away and went to the lady’s rescue. Rushing in the direction
from which the cry came, he saw a carriage. The girl peered out the window hoping to see someone who
could help her.
- "Stop!"- ordered Sir Ronald to the coachman. - "By what right are you on my land?"
The coachman didn’t get a chance to open his mouth, as his master came out of the carriage.
- "My respects, noble sir. I had no idea that this land is yours. My bride and I were just going to my estate,
not wanting to give anyone any trouble. "
- "A flat-out lie! I'm not his bride!" - the girl exclaimed from the window.
- "Explain yourself, Sir. What does that mean?",- said Sir Ronald.
- "Of course. The king of a neighboring country has promised his daughter and half his kingdom to the one
who’ll save her from the outlaws who took her. I’ve defeated those bastards and now I’m taking the princess
to her father. "
- "It's not true! They were in on it together They’ve kidnapped me on his order! I saw how he paid them a
bag of gold!" - The princess didn’t stop taking for a second, trying to quickly describe the situation to
the miraculously appeared savior.
- "Such behavior is unworthy of a knight! Prepare to die!",- exclaimed Sir Ronald, drawing his sword. -
"Ha-ha-ha, simple-hearted nobleman! We’ll see about that..."
I'm sure that many of you have some experience with computer games. But have you ever wanted to change
the game so that the characters or a game world would be more consistent with your idea of the perfect
game? Probably, yes.
In this mission (and in several subsequent ones, related to it) you’ll have a chance "to sit in the
developer's chair" and create the logic of a simple game about battles.
Let's start with the simple task - one-on-one duel. You need to create the class Warrior, the instances
of which will have 2 parameters - health (equal to 50 points) and attack (equal to 5 points), and 1
property - is_alive, which can be True (if warrior's health is > 0) or False (in the other case). In
addition you have to create the second unit type - Knight, which should be the subclass of the Warrior
but have the increased attack - 7. Also you have to create a function fight(), which will initiate the
duel between 2 warriors and define the strongest of them. The duel occurs according to the following
principle:
Every turn, the first warrior will hit the second and this second will lose his health in the same value
as the attack of the first warrior. After that, if he is still alive, the second warrior will do the same
to the first one.
The fight ends with the death of one of them. If the first warrior is still alive (and thus the other one
is not anymore), the function should return True, False otherwise.

Example:
chuck = Warrior()
bruce = Warrior()
carl = Knight()
dave = Warrior()

fight(chuck, bruce) == True
fight(dave, carl) == False
chuck.is_alive == True
bruce.is_alive == False
carl.is_alive == True
dave.is_alive == False

Input: The warriors.

Output: The result of the duel (True or False).

How it is used: For computer games development.

Precondition:
2 types of units
All given fights have an end (for all missions).

----------
----------

Un día, en una típica tarde de primavera, Sir Ronald ha estado paseando por sus tierras, montado a caballo.
Nada hacía presagiar problemas, cuando de repente Sir Ronald oyó un grito de socorro, procedente de algún
lugar cercano:
- "¡Socorro! Socorro!" - gritó una penetrante voz de niña.
Como verdadero caballero, Sir Ronald no pudo mantenerse al margen y acudió al rescate de la dama. Corriendo
en la dirección de donde provenía el grito, vio un carruaje. La muchacha se asomó por la ventana con la
esperanza de ver a alguien que pudiera ayudarla.
- "¡Deténgase!"- ordenó Sir Ronald al cochero. - "¿Con qué derecho estás en mis tierras?".
El cochero no tuvo oportunidad de abrir la boca, ya que su amo salió del carruaje.
- "Mis respetos, noble señor. No tenía ni idea de que esta tierra fuera suya. Mi novia y yo sólo íbamos a
mi finca, sin querer dar problemas a nadie. "
- "¡Mentira descarada! ¡No soy su novia!" - Exclamó la muchacha desde la ventana.
- "Explíquese, señor. ¿Qué significa eso?",- dijo Sir Ronald.
- "Por supuesto. El rey de un país vecino ha prometido a su hija y la mitad de su reino a quien la salve
de los forajidos que la raptaron. He derrotado a esos bastardos y ahora me llevo a la princesa con su padre. "
- "¡No es verdad! Estaban juntos en esto ¡Me han secuestrado por orden suya! ¡Vi cómo les pagó una maleta de
oro!" - La princesa no paró de hablar ni un segundo, intentando describir rápidamente la situación al salvador
aparecido milagrosamente.
- "¡Tal comportamiento es indigno de un caballero! Prepárate para morir!",- exclamó Sir Ronald, desenvainando
su espada. - "¡Ja, ja, ja, noble de corazón sencillo! Eso ya lo veremos...".
Seguro que muchos de vosotros tenéis alguna experiencia con los juegos de ordenador. Pero, ¿alguna vez habéis
querido cambiar el juego para que los personajes o el mundo del juego fueran más coherentes con vuestra idea
del juego perfecto? Probablemente, sí.
En esta misión (y en varias posteriores, relacionadas con ella) tendrás la oportunidad de "sentarte en
la silla del desarrollador" y crear la lógica de un sencillo juego sobre batallas.
Empecemos con una tarea sencilla: un duelo uno contra uno. Necesitas crear la clase Guerrero, cuyas
instancias tendrán 2 parámetros - salud (igual a 50 puntos) y ataque (igual a 5 puntos), y 1 propiedad -
is_alive, que puede ser True (si la salud del guerrero es > 0) o False (en el otro caso). Además tienes
que crear el segundo tipo de unidad - Knight, que debe ser la subclase del Warrior pero tener el ataque
aumentado - 7. También tienes que crear una función fight(), que iniciará el duelo entre 2 guerreros y
definirá al más fuerte de ellos. El duelo ocurre de acuerdo con el siguiente principio:
En cada turno, el primer guerrero golpeará al segundo y este perderá su salud en el mismo valor que el
ataque del primer guerrero. Después, si todavía está vivo, el segundo guerrero hará lo mismo con el primero.
El combate termina con la muerte de uno de ellos. Si el primer guerrero sigue vivo (y por tanto el otro ya no),
la función debe devolver True, False en caso contrario.

Ejemplo:
chuck = Guerrero()
bruce = Guerrero()
carl = Caballero()
dave = Guerrero()

fight(chuck, bruce) == True
fight(dave, carl) == False
chuck.is_alive == True
bruce.is_alive == False
carl.is_alive == True
dave.is_alive == Falso

Entrada: Los guerreros.

Salida: El resultado del duelo (Verdadero o Falso).

Cómo se utiliza: Para el desarrollo de juegos de ordenador.

Precondición:
2 tipos de unidades.
Todos los combates dados tienen un final (para todas las misiones).
'''


class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
        self.is_alive = True

    def hit(self, other):
        other.health -= self.attack
        if other.health <= 0:
            other.is_alive = False

class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7

def fight(unit_1, unit_2):
    while unit_1.is_alive and unit_2.is_alive:
        unit_1.hit(unit_2)
        if unit_2.is_alive:
            unit_2.hit(unit_1)
    return unit_1.is_alive

if __name__ == "__main__":
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
