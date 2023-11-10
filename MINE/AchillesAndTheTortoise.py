"""
In a race, the quickest runner can never overtake the slowest, since the pursuer must first
reach the point whence the pursued started, so that the slower must always hold a lead.

– as recounted by Aristotle, Physics VI:9, 239b15
"Achilles and the tortoise" is one of the famous Zeno's paradoxes . Nikola wants to check
the validity of the paradox and constructed two robots for this purpose: Achilleborg (A1 --
fast agile prototype) and Tortoimenator (T2 -- heavy slow cyborg).

A1 is faster than T2, so it has a X seconds head start on A1. For X seconds T2 will move at
t2_speed*X metres. So A1 must first reach the point whence T2 already reached. But T2 is moving
and next step for A1 is to reach the next point and so on to infinity . The paradox is correct
in theory, but in practice A1 easily outruns T2. Hm... maybe we can calculate when A1 will
catch up to T2.

A1-T2
You are given A1 and T2's speed in m/s as well as the length of the advantage T2 has in seconds.
Try to count the time when from when A1 come abreast with T2 (count from T2 start). The result
should be given in seconds with precious ±10 -8 .

Input: Three arguments. Speeds of A1 and T2 and advantage as integers.

Output: The time when A1 catch up T2 (count from T2 start) as an integer or float.

Example:
chase(6, 3, 2) == 4
chase(10, 1, 10) == 11.11111111

How it is used: Let's return to school and remember our basic math principles. Sometimes
simple arithmetic allows us to resolve difficult paradox problems easily.

Precondition:
t2_speed < a1_speed < 343
0 < advantage ≤ 60

----------
----------

En una carrera, el corredor más rápido nunca podrá superar al más lento, ya que debe
llegar primero al punto donde el corredor más lento comenzó, y por lo tanto, el corredor
más lento siempre mantendrá el liderazgo.

– Como fue narrado por Aristóteles, Física VI: 9, 239b15
"Aquiles y la tortuga" es una de las famosas paradojas de Zenón . Nikola quiere comprobar
la validez de la paradoja y construyó dos robots para este propósito: Achilleborg (A1 -
prototipo rápido y ágil) y Tortoimenator (T2 - cyborg pesado y lento).

A1 es más rápido que T2, por lo que este último empieza con una ventaja de X segundos con
respecto a A2. Durante X segundos T2 se moverá a velocidad_t2*X metros. A1 debe primero llegar
al punto de donde T2 ya llegó, pero considerando que T2 sigue en movimiento, A1 deberá entonces
alcanzar el siguiente punto por el que ya paso T2 y así hasta el infinito . La paradoja es correcta
en teoría, pero en la práctica A1 sobrepasa fácilmente T2. Hmm ... quizás podemos calcular cuando
A1 alcanzara a T2.

A1-T2
Se indican las velocidades de A1 y T2 en m / s, así como la ventaja que tiene T2 en segundos.
Trata de contar el tiempo que demora A1 en alcanzar T2 (comenzando desde el momento que arranca
T2). El resultado deberá ser dado en segundos con una precisión ±10 -8 .

Datos de Entrada: Tres argumentos. Velocidades de A1 y T2 y la ventaja, como enteros (int).

Salida: El tiempo que A1 emplea en alcanzar a T2 (comenzando desde el momento que arranca T2) como
un entero (int) o decimal (float).

Ejemplo:
chase(6, 3, 2) == 4
chase(10, 1, 10) == 11.11111111

¿Cómo se usa?: Regresemos a la escuela y recordemos nuestros principios básicos de matemáticas. A
veces, la simple aritmética nos permite resolver fácilmente problemas difíciles de paradojas.

Condiciones:
velocidad_t2 < velocidad_a1 < 343
0 < ventaja ≤ 60
"""


def chase(a1_speed, t2_speed, advantage):
    return (t2_speed * advantage) / (a1_speed - t2_speed) + advantage


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits):
        precision = 0.1**significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(chase(6, 3, 2), 4, 8), "example"
    assert almost_equal(chase(10, 1, 10), 11.111111111, 8), "long number"
