'''
Since you are here, it means that you’ve already solved 4 missions of the series. Your function can already
adopt more than one light bulb in the date array to determine if the room is lit or not. And with the second
and third elements the period we want to observe can be defined.

In the 5th mission, a fourth argument is added - the operating time of the light bulbs. By analogy with the
previous missions - if it’s not passed, then the bulb works indefinitely.

The operating time argument is passed as a timedelta object. It shows how long the light bulb can work when
it’s on. It has no cooling, which means that if our bulb can work for only one hour, then it can work for
30 minutes now and 30 minutes next year. After that it will turn itself off and will no longer respond to
the button.

We still need to calculate how long the room has been lit.

Input: Four arguments and only the first one is required. The first one (els) is a list of datetime objects
(instead of datetime object there can be a tuple of two datetime and int), the second (start_watching) and
the third ones (end_watching) is the datetime objects. The forth argument (operating) - timedelta object -
how long the lamp can work.

Output: A number of seconds as an integer.

Example:
sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 0, 30),
    (datetime(2015, 1, 12, 10, 0, 30), 2),
    (datetime(2015, 1, 12, 10, 1, 0), 2),
], operating=timedelta(seconds=20)) == 40

sum_light([
    (datetime(2015, 1, 12, 10, 0, 10), 3),
    datetime(2015, 1, 12, 10, 0, 20),
    (datetime(2015, 1, 12, 10, 0, 30), 3),
    (datetime(2015, 1, 12, 10, 0, 30), 2),
    datetime(2015, 1, 12, 10, 0, 40),
    (datetime(2015, 1, 12, 10, 0, 50), 2),
    (datetime(2015, 1, 12, 10, 1, 20), 2),
    (datetime(2015, 1, 12, 10, 1, 40), 2),
], start_watching=datetime(2015, 1, 12, 10, 0, 20), operating=timedelta(seconds=100)) == 50

sum_light([
    (datetime(2015, 1, 12, 10, 0, 10), 3),
    datetime(2015, 1, 12, 10, 0, 20),
    (datetime(2015, 1, 12, 10, 0, 30), 3),
    (datetime(2015, 1, 12, 10, 0, 30), 2),
],
start_watching=datetime(2015, 1, 12, 10, 0, 10),
end_watching=datetime(2015, 1, 12, 10, 0, 30),
operating=timedelta(seconds=5)) == 10

Precondition:
The array of pressing the button is always sorted in ascending order.
The array of pressing the button has no repeated elements.
The minimum possible date is 1970-01-01
The maximum possible date is 9999-12-31

----------
----------

Como estás aquí, significa que ya has resuelto 4 misiones de la serie. Tu función ya puede adoptar
más de una bombilla en la matriz de fechas para determinar si la habitación está iluminada o no. Y
con el segundo y tercer elemento se puede definir el periodo que queremos observar.

En la 5ª misión, se añade un cuarto argumento - el tiempo de funcionamiento de las bombillas. Por
analogía con las misiones anteriores - si no se pasa, entonces la bombilla funciona indefinidamente.

El argumento tiempo de funcionamiento se pasa como un objeto timedelta. Muestra cuánto tiempo puede
funcionar la bombilla cuando está encendida. No tiene refrigeración, lo que significa que si nuestra
bombilla puede funcionar sólo durante una hora, entonces puede funcionar durante 30 minutos ahora y
30 minutos el año que viene. Después se apagará sola y dejará de responder al botón.

Todavía tenemos que calcular cuánto tiempo ha estado iluminada la habitación.

Entrada: Cuatro argumentos y sólo se requiere el primero. El primero (els) es una lista de objetos
datetime (en lugar del objeto datetime puede haber una tupla de dos datetime e int), el segundo
(start_watching) y el tercero (end_watching) son los objetos datetime. El cuarto argumento (operating) -
objeto timedelta - cuánto tiempo puede funcionar la lámpara.

Salida: Un número de segundos como un entero.

Ejemplo:
suma_luz([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 0, 30),
    (datetime(2015, 1, 12, 10, 0, 30), 2),
    (datetime(2015, 1, 12, 10, 1, 0), 2),
], operating=timedelta(seconds=20)) == 40

suma_luz([
    (datetime(2015, 1, 12, 10, 0, 10), 3),
    datetime(2015, 1, 12, 10, 0, 20),
    (datetime(2015, 1, 12, 10, 0, 30), 3),
    (datetime(2015, 1, 12, 10, 0, 30), 2),
    datetime(2015, 1, 12, 10, 0, 40),
    (datetime(2015, 1, 12, 10, 0, 50), 2),
    (datetime(2015, 1, 12, 10, 1, 20), 2),
    (datetime(2015, 1, 12, 10, 1, 40), 2),
], start_watching=datetime(2015, 1, 12, 10, 0, 20), operating=timedelta(seconds=100)) == 50

suma_luz([
    (datetime(2015, 1, 12, 10, 0, 10), 3),
    datetime(2015, 1, 12, 10, 0, 20),
    (datetime(2015, 1, 12, 10, 0, 30), 3),
    (datetime(2015, 1, 12, 10, 0, 30), 2),
],
start_watching=datetime(2015, 1, 12, 10, 0, 10),
end_watching=datetime(2015, 1, 12, 10, 0, 30),
operating=timedelta(seconds=5)) == 10

Condición previa:

El array de pulsar el botón siempre está ordenado de forma ascendente.
El array de pulsar el botón no tiene elementos repetidos.
La fecha mínima posible es 1970-01-01
La fecha máxima posible es 9999-12-31
'''

# Taken from mission Multiple Lightbulbs

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
from datetime import datetime
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

from datetime import datetime, timedelta
from typing import List, Optional, Union
from itertools import zip_longest


SECONDS_IN_DAY = 60 * 60 * 24


def get_periods(start_watching, end_watching, els, operating):
    for start, end in zip_longest(els[::2], els[1::2], fillvalue=end_watching):
        if start_watching > end:
            continue

        period = (min(max(start, start_watching), end_watching), min(end, end_watching))

        if operating is None:
            yield period
        else:
            period = (period[0], min(period[1], period[0] + operating))

            yield period

            operating -= period[1] - period[0]
            if not operating:
                break


def unite_timelines(timelines):
    periods = sum(timelines, [])
    periods = sorted(periods, key=lambda a: a[0])
    central = periods.pop(0)
    while periods:
        cur = periods.pop(0)
        if cur[0] > central[1]:
            yield central
            central = cur
            continue

        central = (min(central[0], cur[0]), max(central[1], cur[1]))

    yield central


def periods_to_seconds(periods):
    return sum([(t[1] - t[0]).seconds + (t[1] - t[0]).days * SECONDS_IN_DAY for t in periods])



def get_timelines(els):
    from collections import defaultdict
    timelines = defaultdict(list)
    for el in els:
        if isinstance(el, datetime):
            timelines[0].append(el)
        else:
            timelines[el[1]].append(el[0])
    return timelines.values()


def sum_light(els: List[Union[datetime,tuple[datetime, int]]],
                start_watching: datetime = datetime.min,
                end_watching: datetime = datetime.max,
                operating: Optional[timedelta] = None) -> int:
    """
    how long the light bulb has been turned on
    """
    timelines = get_timelines(els)
    periods = [list(get_periods(start_watching, end_watching, els, operating)) for els in timelines]
    periods = unite_timelines(periods)
    return periods_to_seconds(periods)


if __name__ == "__main__":
    print("Example:")

    print(
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
            ],
            start_watching=datetime(2015, 1, 12, 10, 0, 10),
            end_watching=datetime(2015, 1, 12, 10, 0, 30),
            operating=timedelta(seconds=5),
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

    assert (
            sum_light(
                [
                    datetime(2015, 1, 12, 10, 0, 0),
                    datetime(2015, 1, 12, 10, 0, 10),
                ],
                operating=timedelta(seconds=100),
            )
            == 10
    )

    assert (
            sum_light(
                [
                    datetime(2015, 1, 12, 10, 0, 0),
                    datetime(2015, 1, 12, 10, 0, 10),
                ],
                operating=timedelta(seconds=5),
            )
            == 5
    )

    assert (
            sum_light(
                [
                    datetime(2015, 1, 12, 10, 0, 0),
                    datetime(2015, 1, 12, 10, 0, 10),
                    (datetime(2015, 1, 12, 10, 0, 0), 2),
                    (datetime(2015, 1, 12, 10, 1, 0), 2),
                ],
                operating=timedelta(seconds=100),
            )
            == 60
    )

    assert (
            sum_light(
                [
                    datetime(2015, 1, 12, 10, 0, 0),
                    datetime(2015, 1, 12, 10, 0, 30),
                    (datetime(2015, 1, 12, 10, 0, 30), 2),
                    (datetime(2015, 1, 12, 10, 1, 0), 2),
                ],
                operating=timedelta(seconds=100),
            )
            == 60
    )

    assert (
            sum_light(
                [
                    datetime(2015, 1, 12, 10, 0, 0),
                    datetime(2015, 1, 12, 10, 0, 30),
                    (datetime(2015, 1, 12, 10, 0, 30), 2),
                    (datetime(2015, 1, 12, 10, 1, 0), 2),
                ],
                operating=timedelta(seconds=20),
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
                ],
                operating=timedelta(seconds=10),
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
                start_watching=datetime(2015, 1, 12, 10, 0, 20),
                operating=timedelta(seconds=100),
            )
            == 50
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
                start_watching=datetime(2015, 1, 12, 10, 0, 20),
                operating=timedelta(seconds=10),
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
                ],
                start_watching=datetime(2015, 1, 12, 10, 0, 10),
                end_watching=datetime(2015, 1, 12, 10, 0, 30),
                operating=timedelta(seconds=20),
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
                ],
                start_watching=datetime(2015, 1, 12, 10, 0, 10),
                end_watching=datetime(2015, 1, 12, 10, 0, 30),
                operating=timedelta(seconds=10),
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
                ],
                start_watching=datetime(2015, 1, 12, 10, 0, 10),
                end_watching=datetime(2015, 1, 12, 10, 0, 30),
                operating=timedelta(seconds=5),
            )
            == 10
    )

    print(
        "The forth mission in series is completed? Click 'Check' to earn cool rewards!"
    )
