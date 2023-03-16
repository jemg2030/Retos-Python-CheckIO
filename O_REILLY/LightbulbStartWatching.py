'''
This is the second mission in the lightbulb series. I will try to make each following task slightly more
complex.

You have already learned how to count the amount of time a light bulb has been on, or how long a room has
been lit. Now let's add one more parameter - the counting start time.

This means that the light continues to turn on and off as before. But now, as a result of the function,
I want not only to know how long there was light in the room, but how long the room was lit, starting
from a certain moment.

One more argument is added – start_watching, and if it’s not passed, we count as in the previous version of
the program for the entire period.

Input: Two arguments and only the first one is required. The first one is a list of datetime objects and the
second one is a datetime object.

Output: A number of seconds as an integer.

Example:
sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 0, 10),
],
datetime(2015, 1, 12, 10, 0, 5)) == 5

sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 0, 10),
], datetime(2015, 1, 12, 10, 0, 0)) == 10

sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 10, 10),
    datetime(2015, 1, 12, 11, 0, 0),
    datetime(2015, 1, 12, 11, 10, 10),
], datetime(2015, 1, 12, 11, 0, 0)) == 610
1
Precondition:
The array of pressing the button is always sorted in ascending order
The array of pressing the button has no repeated elements
The amount of elements is always even (the light will eventually be off)
The minimum possible date is 1970-01-01
The maximum possible date is 9999-12-31

----------
----------

Esta es la segunda misión de la serie de la bombilla. Intentaré que cada tarea siguiente sea
ligeramente más compleja.

Ya has aprendido a contar el tiempo que lleva encendida una bombilla o el tiempo que lleva iluminada
una habitación. Ahora vamos a añadir un parámetro más: la hora de inicio del conteo.

Esto significa que la luz sigue encendiéndose y apagándose como antes. Pero ahora, como resultado de
la función, no sólo quiero saber cuánto tiempo hubo luz en la habitación, sino cuánto tiempo estuvo
iluminada la habitación, a partir de un momento determinado.

Se añade un argumento más - start_watching, y si no se pasa, contamos como en la versión anterior del
programa para todo el período.

Entrada: Dos argumentos y sólo se requiere el primero. El primero es una lista de objetos datetime y el
segundo es un objeto datetime.

Salida: Un número de segundos como entero.

Ejemplo:

suma_luz([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 0, 10),
],
datetime(2015, 1, 12, 10, 0, 5)) == 5

suma_luz([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 0, 10),
], datetime(2015, 1, 12, 10, 0, 0)) == 10

suma_luz([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 10, 10),
    datetime(2015, 1, 12, 11, 0, 0),
    datetime(2015, 1, 12, 11, 10, 10),
], datetime(2015, 1, 12, 11, 0, 0)) == 610

Condición previa:
El array de pulsar el botón siempre está ordenado de forma ascendente
La matriz de pulsar el botón no tiene elementos repetidos
La cantidad de elementos es siempre par (la luz acabará apagándose)
La fecha mínima posible es 1970-01-01
La fecha máxima posible es 9999-12-31
'''


# Taken from mission Lightbulb Intro

from datetime import datetime, timedelta
from typing import List
def sum_light(els: List[datetime]) -> int:
    """
    how long the light bulb has been turned on
    """
    total_time_on = timedelta()
    previous_time = els[0]
    for i in range(1, len(els)):
        current_time = els[i]
        time_difference = current_time - previous_time
        if i % 2 == 1:
            total_time_on += time_difference
        previous_time = current_time
    return int(total_time_on.total_seconds())
if __name__ == "__main__":
    print("Example:")
    print(
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ]
        )
    )
    # These "asserts" are used for self-checking and not for an auto-testing
    assert (
        sum_light(
            els=[
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
            ]
        )
        == 610
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ]
        )
        == 1220
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
                datetime(2015, 1, 12, 11, 10, 10),
                datetime(2015, 1, 12, 12, 10, 10),
            ]
        )
        == 4820
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 1),
            ]
        )
        == 1
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 13, 11, 0, 0),
            ]
        )
        == 86410
    )
    print(
        "The first mission in series is completed? Click 'Check' to earn cool rewards!"
    )


from datetime import datetime, timedelta
from typing import List, Optional


def sum_light(els: List[datetime], start_watching: Optional[datetime] = None) -> int:
    """
    how long the light bulb has been turned on
    """
    if not start_watching:
        start_watching = els[0]
    els = [max(start_watching, el) for el in els]
    els = iter(els)
    return sum((off - on).total_seconds() for on, off in zip(els, els))

if __name__ == "__main__":
    print("Example:")
    print(
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            datetime(2015, 1, 12, 10, 0, 5),
        )
    )

    assert (
        sum_light(
            els=[
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            start_watching=datetime(2015, 1, 12, 10, 0, 5),
        )
        == 5
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            datetime(2015, 1, 12, 10, 0, 0),
        )
        == 10
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 11, 0, 0),
        )
        == 610
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 11, 0, 10),
        )
        == 600
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 10, 10, 0),
        )
        == 620
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
                datetime(2015, 1, 12, 11, 10, 11),
                datetime(2015, 1, 12, 12, 10, 11),
            ],
            datetime(2015, 1, 12, 12, 10, 11),
        )
        == 0
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
                datetime(2015, 1, 12, 11, 10, 11),
                datetime(2015, 1, 12, 12, 10, 11),
            ],
            datetime(2015, 1, 12, 12, 9, 11),
        )
        == 60
    )

    print("The second mission in series is done? Click 'Check' to earn cool rewards!")
