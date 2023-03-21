'''
In the 4th mission of the series more light bulbs are added.

You still must determine how long the room will be lit during the observation period between
start_watching and end_watching. But now we have more than one light bulb. This means that in
the light bulb switching array can now also be passed the number of the light bulb, the button
of which is being pressed.

Each element of the button clicking array can be either a datetime object (which means the time
when the first button was pressed) or a tuple of 2 elements (where the first elements is a datetime
object, the time the button was pressed), and the second is the number of the light bulb, the button
of which is being pressed.

If the passed array will only consist of datetime elements, then we have only one light bulb and the
function should work the same way as in the previous mission of the series.

Input: Three arguments and only the first one is required. The first one is a list of datetime objects
(instead of datetime object there can be a tuple of two datetime and int), the second and the third ones
are the datetime objects.

Output: A number of seconds as an integer.

Example:
sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 0, 10),
    (datetime(2015, 1, 12, 10, 0, 0), 2),
    (datetime(2015, 1, 12, 10, 1, 0), 2),
]) == 60

sum_light([
    (datetime(2015, 1, 12, 10, 0, 10), 3),
    datetime(2015, 1, 12, 10, 0, 20),
    (datetime(2015, 1, 12, 10, 0, 30), 3),
    (datetime(2015, 1, 12, 10, 0, 30), 2),
    datetime(2015, 1, 12, 10, 0, 40),
    (datetime(2015, 1, 12, 10, 0, 50), 2),
    (datetime(2015, 1, 12, 10, 1, 0), 3),
    (datetime(2015, 1, 12, 10, 1, 20), 3),
]) == 60

sum_light([
    datetime(2015, 1, 12, 10, 0, 20),
    (datetime(2015, 1, 12, 10, 0, 30), 2),
    datetime(2015, 1, 12, 10, 0, 40),
    (datetime(2015, 1, 12, 10, 0, 50), 2),
], datetime(2015, 1, 12, 10, 0, 30)) == 20

sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 0, 10),
    (datetime(2015, 1, 12, 10, 0, 0), 2),
    (datetime(2015, 1, 12, 10, 1, 0), 2),
], datetime(2015, 1, 12, 10, 0, 20), datetime(2015, 1, 12, 10, 1, 0)) == 40

Precondition:
The array of pressing the button is always sorted in ascending order.
The array of pressing the button has no repeated elements.
The minimum possible date is 1970-01-01
The maximum possible date is 9999-12-31

----------
----------

En la 4ª misión de la serie se añaden más bombillas.

Sigues teniendo que determinar cuánto tiempo estará iluminada la habitación durante el periodo de
observación entre inicio_observación y fin_observación. Pero ahora tenemos más de una bombilla.
Esto significa que en el array de cambio de bombilla ahora también se puede pasar el número de la
bombilla cuyo botón se está pulsando.

Cada elemento del array de pulsación de botón puede ser un objeto datetime (que significa el momento
en que se pulsó el primer botón) o una tupla de 2 elementos (donde el primer elemento es un objeto
datetime, el momento en que se pulsó el botón), y el segundo es el número de la bombilla, cuyo botón
se está pulsando.

Si el array pasado sólo consta de elementos datetime, entonces sólo tenemos una bombilla y la función
debería funcionar de la misma manera que en la misión anterior de la serie.

Entrada: Tres argumentos y sólo se requiere el primero. El primero es una lista de objetos datetime
(en lugar del objeto datetime puede haber una tupla de dos datetime e int), el segundo y el tercero
son los objetos datetime.

Salida: Un número de segundos como entero.

Ejemplo:
suma_luz([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 0, 10),
    (datetime(2015, 1, 12, 10, 0, 0), 2),
    (datetime(2015, 1, 12, 10, 1, 0), 2),
]) == 60

suma_luz([
    (datetime(2015, 1, 12, 10, 0, 10), 3),
    datetime(2015, 1, 12, 10, 0, 20),
    (datetime(2015, 1, 12, 10, 0, 30), 3),
    (datetime(2015, 1, 12, 10, 0, 30), 2),
    datetime(2015, 1, 12, 10, 0, 40),
    (datetime(2015, 1, 12, 10, 0, 50), 2),
    (datetime(2015, 1, 12, 10, 1, 0), 3),
    (datetime(2015, 1, 12, 10, 1, 20), 3),
]) == 60

suma_luz([
    datetime(2015, 1, 12, 10, 0, 20),
    (datetime(2015, 1, 12, 10, 0, 30), 2),
    datetime(2015, 1, 12, 10, 0, 40),
    (datetime(2015, 1, 12, 10, 0, 50), 2),
], datetime(2015, 1, 12, 10, 0, 30)) == 20

suma_luz([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 0, 10),
    (datetime(2015, 1, 12, 10, 0, 0), 2),
    (datetime(2015, 1, 12, 10, 1, 0), 2),
], datetime(2015, 1, 12, 10, 0, 20), datetime(2015, 1, 12, 10, 1, 0)) == 40

Condición previa:
El array de pulsar el botón siempre está ordenado de forma ascendente.
El array de pulsar el botón no tiene elementos repetidos.
La fecha mínima posible es 1970-01-01
La fecha máxima posible es 9999-12-31
'''

# Taken from mission Lightbulb End Watching

# Taken from mission Lightbulb Start Watching
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
from datetime import datetime
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
from datetime import datetime, timedelta
from typing import List, Optional


def sum_light(
        els: List[datetime],
        start_watching: Optional[datetime] = None,
        end_watching: Optional[datetime] = None,
) -> int:
    """
    how long the light bulb has been turned on
    """
    if len(els) == 0:
        return 0
    if end_watching and end_watching <= els[0]:
        return 0
    if len(els) == 1:
        return int((end_watching - max(els[0], start_watching)).total_seconds())

    if start_watching and els[1] <= start_watching:
        return sum_light(els[2:], start_watching, end_watching)

    start_point = max(els[0], start_watching) if start_watching else els[0]
    end_point = min(els[1], end_watching) if end_watching else els[1]
    return int((end_point - start_point).total_seconds()) + sum_light(els[2:], start_watching, end_watching)


if __name__ == "__main__":
    print("Example:")
    print(
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            datetime(2015, 1, 12, 10, 0, 0),
            datetime(2015, 1, 12, 10, 0, 10),
        )
    )
    assert (
            sum_light(
                els=[
                    datetime(2015, 1, 12, 10, 0, 0),
                    datetime(2015, 1, 12, 10, 0, 10),
                ],
                start_watching=datetime(2015, 1, 12, 10, 0, 0),
                end_watching=datetime(2015, 1, 12, 10, 0, 10),
            )
            == 10
    )
    assert (
            sum_light(
                [
                    datetime(2015, 1, 12, 10, 0, 0),
                    datetime(2015, 1, 12, 10, 0, 10),
                ],
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 7),
            )
            == 7
    )
    assert (
            sum_light(
                [
                    datetime(2015, 1, 12, 10, 0, 0),
                    datetime(2015, 1, 12, 10, 0, 10),
                ],
                datetime(2015, 1, 12, 10, 0, 3),
                datetime(2015, 1, 12, 10, 0, 10),
            )
            == 7
    )
    assert (
            sum_light(
                [
                    datetime(2015, 1, 12, 10, 0, 0),
                    datetime(2015, 1, 12, 10, 0, 10),
                ],
                datetime(2015, 1, 12, 10, 0, 10),
                datetime(2015, 1, 12, 10, 0, 20),
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
                ],
                datetime(2015, 1, 12, 10, 30, 0),
                datetime(2015, 1, 12, 11, 0, 0),
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
                ],
                datetime(2015, 1, 12, 10, 10, 0),
                datetime(2015, 1, 12, 11, 0, 0),
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
                datetime(2015, 1, 12, 10, 10, 0),
                datetime(2015, 1, 12, 11, 0, 10),
            )
            == 20
    )
    assert (
            sum_light(
                [
                    datetime(2015, 1, 12, 10, 0, 0),
                    datetime(2015, 1, 12, 10, 10, 10),
                    datetime(2015, 1, 12, 11, 0, 0),
                    datetime(2015, 1, 12, 11, 10, 10),
                ],
                datetime(2015, 1, 12, 9, 50, 0),
                datetime(2015, 1, 12, 10, 0, 10),
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
                datetime(2015, 1, 12, 9, 0, 0),
                datetime(2015, 1, 12, 10, 5, 0),
            )
            == 300
    )
    assert (
            sum_light(
                [
                    datetime(2015, 1, 12, 10, 0, 0),
                    datetime(2015, 1, 12, 10, 10, 10),
                    datetime(2015, 1, 12, 11, 0, 0),
                    datetime(2015, 1, 12, 11, 10, 10),
                ],
                datetime(2015, 1, 12, 11, 5, 0),
                datetime(2015, 1, 12, 12, 0, 0),
            )
            == 310
    )
    assert (
            sum_light(
                [
                    datetime(2015, 1, 12, 10, 0, 0),
                    datetime(2015, 1, 12, 10, 10, 10),
                    datetime(2015, 1, 12, 11, 0, 0),
                ],
                datetime(2015, 1, 12, 11, 5, 0),
                datetime(2015, 1, 12, 11, 10, 0),
            )
            == 300
    )
    assert (
            sum_light(
                [
                    datetime(2015, 1, 12, 10, 0, 0),
                    datetime(2015, 1, 12, 10, 10, 10),
                    datetime(2015, 1, 12, 11, 0, 0),
                ],
                datetime(2015, 1, 12, 10, 10, 0),
                datetime(2015, 1, 12, 11, 0, 10),
            )
            == 20
    )
    assert (
            sum_light(
                [
                    datetime(2015, 1, 12, 10, 0, 0),
                    datetime(2015, 1, 12, 10, 10, 10),
                    datetime(2015, 1, 12, 11, 0, 0),
                ],
                datetime(2015, 1, 12, 9, 10, 0),
                datetime(2015, 1, 12, 10, 20, 20),
            )
            == 610
    )
    assert (
            sum_light(
                [
                    datetime(2015, 1, 12, 10, 0, 0),
                ],
                datetime(2015, 1, 12, 9, 10, 0),
                datetime(2015, 1, 12, 10, 20, 20),
            )
            == 1220
    )
    assert (
            sum_light(
                [
                    datetime(2015, 1, 12, 10, 0, 0),
                ],
                datetime(2015, 1, 12, 9, 9, 0),
                datetime(2015, 1, 12, 10, 0, 0),
            )
            == 0
    )
    assert (
            sum_light(
                [
                    datetime(2015, 1, 12, 10, 0, 0),
                ],
                datetime(2015, 1, 12, 9, 9, 0),
                datetime(2015, 1, 12, 10, 0, 10),
            )
            == 10
    )
    print(
        "The third mission in series is completed? Click 'Check' to earn cool rewards!"
    )

from datetime import datetime, timedelta
from typing import List, Optional, Union, Tuple


def sum_light(
        els: List[Union[datetime, Tuple[datetime, int]]],
        start_watching: Optional[datetime] = None,
        end_watching: Optional[datetime] = None,
) -> int:
    """
    how long the light bulb has been turned on
    """
    # replace elements with no bulb index
    els, switch = [(e, 0) if type(e) is datetime else e for e in els], [False] * 10
    sw, ew, on = start_watching or els[0][0], end_watching or els[-1][0], []

    # determine what intervals any lamp is on
    for idx, e in enumerate(els):
        switch[e[1]], els[idx] = not switch[e[1]], min(ew, max(e[0], sw))
        on.append(any(switch))

    # then summ all intervals where any lamp is on
    els += [ew]
    return sum(on[i] * (els[i + 1] - els[i]).total_seconds() for i in range(len(on)))


if __name__ == "__main__":
    print("Example:")

    print(
        sum_light(
            els=[
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ],
            start_watching=datetime(2015, 1, 12, 10, 0, 0),
            end_watching=datetime(2015, 1, 12, 10, 1, 0),
        )
    )

    assert (
            sum_light(
                [
                    datetime(2015, 1, 12, 10, 0, 0),
                    (datetime(2015, 1, 12, 10, 0, 0), 2),
                    datetime(2015, 1, 12, 10, 0, 10),
                    (datetime(2015, 1, 12, 10, 1, 0), 2),
                ]
            )
            == 60
    )

    assert (
            sum_light(
                [
                    datetime(2015, 1, 12, 10, 0, 0),
                    datetime(2015, 1, 12, 10, 0, 10),
                    (datetime(2015, 1, 12, 11, 0, 0), 2),
                    (datetime(2015, 1, 12, 11, 1, 0), 2),
                ]
            )
            == 70
    )

    assert (
            sum_light(
                [
                    datetime(2015, 1, 12, 10, 0, 20),
                    (datetime(2015, 1, 12, 10, 0, 30), 2),
                    datetime(2015, 1, 12, 10, 0, 40),
                    (datetime(2015, 1, 12, 10, 0, 50), 2),
                ]
            )
            == 30
    )

    assert (
            sum_light(
                [
                    (datetime(2015, 1, 12, 10, 0, 10), 3),
                    datetime(2015, 1, 12, 10, 0, 20),
                    (datetime(2015, 1, 12, 10, 0, 30), 3),
                    (datetime(2015, 1, 12, 10, 0, 30), 2),
                    datetime(2015, 1, 12, 10, 0, 40),
                    (datetime(2015, 1, 12, 10, 0, 50), 2),
                ]
            )
            == 40
    )

    assert (
            sum_light(
                [
                    (datetime(2015, 1, 12, 10, 0, 10), 3),
                    datetime(2015, 1, 12, 10, 0, 20),
                    (datetime(2015, 1, 12, 10, 0, 30), 3),
                    (datetime(2015, 1, 12, 10, 0, 30), 2),
                    datetime(2015, 1, 12, 10, 0, 40),
                    (datetime(2015, 1, 12, 10, 0, 50), 2),
                    (datetime(2015, 1, 12, 10, 1, 0), 3),
                    (datetime(2015, 1, 12, 10, 1, 20), 3),
                ]
            )
            == 60
    )

    assert (
            sum_light(
                [
                    datetime(2015, 1, 12, 10, 0, 0),
                    (datetime(2015, 1, 12, 10, 0, 0), 2),
                    datetime(2015, 1, 12, 10, 0, 10),
                    (datetime(2015, 1, 12, 10, 1, 0), 2),
                ],
                datetime(2015, 1, 12, 10, 0, 50),
            )
            == 10
    )

    assert (
            sum_light(
                [
                    datetime(2015, 1, 12, 10, 0, 20),
                    (datetime(2015, 1, 12, 10, 0, 30), 2),
                    datetime(2015, 1, 12, 10, 0, 40),
                    (datetime(2015, 1, 12, 10, 0, 50), 2),
                ],
                datetime(2015, 1, 12, 10, 0, 30),
            )
            == 20
    )

    assert (
            sum_light(
                [
                    datetime(2015, 1, 12, 10, 0, 20),
                    (datetime(2015, 1, 12, 10, 0, 30), 2),
                    datetime(2015, 1, 12, 10, 0, 40),
                    (datetime(2015, 1, 12, 10, 0, 50), 2),
                ],
                datetime(2015, 1, 12, 10, 0, 20),
            )
            == 30
    )

    assert (
            sum_light(
                [
                    datetime(2015, 1, 12, 10, 0, 20),
                    (datetime(2015, 1, 12, 10, 0, 30), 2),
                    datetime(2015, 1, 12, 10, 0, 40),
                    (datetime(2015, 1, 12, 10, 0, 50), 2),
                ],
                datetime(2015, 1, 12, 10, 0, 10),
            )
            == 30
    )

    assert (
            sum_light(
                [
                    datetime(2015, 1, 12, 10, 0, 20),
                    (datetime(2015, 1, 12, 10, 0, 30), 2),
                    datetime(2015, 1, 12, 10, 0, 40),
                    (datetime(2015, 1, 12, 10, 0, 50), 2),
                ],
                datetime(2015, 1, 12, 10, 0, 50),
            )
            == 0
    )

    assert (
            sum_light(
                [
                    (datetime(2015, 1, 12, 10, 0, 10), 3),
                    datetime(2015, 1, 12, 10, 0, 20),
                    (datetime(2015, 1, 12, 10, 0, 30), 3),
                    (datetime(2015, 1, 12, 10, 0, 30), 2),
                    datetime(2015, 1, 12, 10, 0, 40),
                    (datetime(2015, 1, 12, 10, 0, 50), 2),
                ],
                datetime(2015, 1, 12, 10, 0, 30),
            )
            == 20
    )

    assert (
            sum_light(
                [
                    (datetime(2015, 1, 12, 10, 0, 10), 3),
                    datetime(2015, 1, 12, 10, 0, 20),
                    (datetime(2015, 1, 12, 10, 0, 30), 3),
                    (datetime(2015, 1, 12, 10, 0, 30), 2),
                    datetime(2015, 1, 12, 10, 0, 40),
                    (datetime(2015, 1, 12, 10, 0, 50), 2),
                ],
                datetime(2015, 1, 12, 10, 0, 20),
            )
            == 30
    )

    assert (
            sum_light(
                [
                    (datetime(2015, 1, 12, 10, 0, 10), 3),
                    datetime(2015, 1, 12, 10, 0, 20),
                    (datetime(2015, 1, 12, 10, 0, 30), 3),
                    (datetime(2015, 1, 12, 10, 0, 30), 2),
                    datetime(2015, 1, 12, 10, 0, 40),
                    (datetime(2015, 1, 12, 10, 0, 50), 2),
                    (datetime(2015, 1, 12, 10, 1, 20), 2),
                    (datetime(2015, 1, 12, 10, 1, 40), 2),
                ],
                datetime(2015, 1, 12, 10, 0, 20),
            )
            == 50
    )

    assert (
            sum_light(
                [
                    datetime(2015, 1, 12, 10, 0, 0),
                    (datetime(2015, 1, 12, 10, 0, 0), 2),
                    datetime(2015, 1, 12, 10, 0, 10),
                    (datetime(2015, 1, 12, 10, 1, 0), 2),
                ],
                datetime(2015, 1, 12, 10, 0, 30),
                datetime(2015, 1, 12, 10, 1, 0),
            )
            == 30
    )

    assert (
            sum_light(
                [
                    datetime(2015, 1, 12, 10, 0, 0),
                    (datetime(2015, 1, 12, 10, 0, 0), 2),
                    datetime(2015, 1, 12, 10, 0, 10),
                    (datetime(2015, 1, 12, 10, 1, 0), 2),
                ],
                datetime(2015, 1, 12, 10, 0, 20),
                datetime(2015, 1, 12, 10, 1, 0),
            )
            == 40
    )

    assert (
            sum_light(
                [
                    datetime(2015, 1, 12, 10, 0, 0),
                    (datetime(2015, 1, 12, 10, 0, 0), 2),
                    datetime(2015, 1, 12, 10, 0, 10),
                ],
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 30),
            )
            == 30
    )

    assert (
            sum_light(
                [
                    (datetime(2015, 1, 12, 10, 0, 10), 3),
                    datetime(2015, 1, 12, 10, 0, 20),
                    (datetime(2015, 1, 12, 10, 0, 30), 3),
                    (datetime(2015, 1, 12, 10, 0, 30), 2),
                    datetime(2015, 1, 12, 10, 0, 40),
                    (datetime(2015, 1, 12, 10, 0, 50), 2),
                ],
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 1, 0),
            )
            == 40
    )

    assert (
            sum_light(
                [
                    (datetime(2015, 1, 12, 10, 0, 10), 3),
                    datetime(2015, 1, 12, 10, 0, 20),
                    (datetime(2015, 1, 12, 10, 0, 30), 3),
                    (datetime(2015, 1, 12, 10, 0, 30), 2),
                    datetime(2015, 1, 12, 10, 0, 40),
                    (datetime(2015, 1, 12, 10, 0, 50), 2),
                ],
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
            )
            == 0
    )

    assert (
            sum_light(
                [
                    (datetime(2015, 1, 12, 10, 0, 10), 3),
                    datetime(2015, 1, 12, 10, 0, 20),
                    (datetime(2015, 1, 12, 10, 0, 30), 3),
                    (datetime(2015, 1, 12, 10, 0, 30), 2),
                    datetime(2015, 1, 12, 10, 0, 40),
                    (datetime(2015, 1, 12, 10, 0, 50), 2),
                ],
                datetime(2015, 1, 12, 10, 0, 10),
                datetime(2015, 1, 12, 10, 0, 20),
            )
            == 10
    )

    assert (
            sum_light(
                [
                    (datetime(2015, 1, 12, 10, 0, 10), 3),
                    datetime(2015, 1, 12, 10, 0, 20),
                    (datetime(2015, 1, 12, 10, 0, 30), 3),
                    (datetime(2015, 1, 12, 10, 0, 30), 2),
                ],
                datetime(2015, 1, 12, 10, 0, 10),
                datetime(2015, 1, 12, 10, 0, 20),
            )
            == 10
    )

    assert (
            sum_light(
                [
                    (datetime(2015, 1, 12, 10, 0, 10), 3),
                    datetime(2015, 1, 12, 10, 0, 20),
                    (datetime(2015, 1, 12, 10, 0, 30), 3),
                    (datetime(2015, 1, 12, 10, 0, 30), 2),
                ],
                datetime(2015, 1, 12, 10, 0, 10),
                datetime(2015, 1, 12, 10, 0, 30),
            )
            == 20
    )

    assert (
            sum_light(
                els=[
                    (datetime(2015, 1, 11, 0, 0, 0), 3),
                    datetime(2015, 1, 12, 0, 0, 0),
                    (datetime(2015, 1, 13, 0, 0, 0), 3),
                    (datetime(2015, 1, 13, 0, 0, 0), 2),
                    datetime(2015, 1, 14, 0, 0, 0),
                    (datetime(2015, 1, 15, 0, 0, 0), 2),
                ],
                start_watching=datetime(2015, 1, 10, 0, 0, 0),
                end_watching=datetime(2015, 1, 16, 0, 0, 0),
            )
            == 345600
    )

    print(
        "The forth mission in series is completed? Click 'Check' to earn cool rewards!"
    )
