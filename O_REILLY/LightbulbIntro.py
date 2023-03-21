'''
With this mission I want to start a series of missions with light bulbs. They will help you understand
the concept of processes and evaluation of the processes’ performance. Instead of light bulbs, in real
life, there may be equipment, the effectiveness of which must be calculated, or workers who go to work,
and their wages must be calculated.

The first mission is quite simple. There is a light bulb, which by default is off, and a button, by pressing
which the light bulb switches its state. This means that if the light bulb is off and the button is pressed,
the light turns on, and if you press it again, it turns off.

(Everything is easy. I am sure that if you’ve got to this mission, you should understand, but just in case I’m
adding a visual.)

The function input is an array of datetime objects - this is the date and time of pressing the button.
Your task is to determine how long the light bulb has been turned on.

Input: A list of datetime objects

Output: A number of seconds as an integer.

Example:
sum_light([
    datetime(2015, 1, 12, 10, 0 , 0),
    datetime(2015, 1, 12, 10, 10 , 10),
]) == 610

sum_light([
    datetime(2015, 1, 12, 10, 0 , 0),
    datetime(2015, 1, 12, 10, 10 , 10),
    datetime(2015, 1, 12, 11, 0 , 0),
    datetime(2015, 1, 12, 11, 10 , 10),
]) == 1220

sum_light([
    datetime(2015, 1, 12, 10, 0 , 0),
    datetime(2015, 1, 12, 10, 0 , 1),
]) == 1

Precondition:
The array of pressing the button is always sorted in ascending order
The array of pressing the button has no repeated elements (which means the result should always be bigger than 0)
The amount of elements is always even (the light will eventually be off)
The minimum possible date is 1970-01-01
The maximum possible date is 9999-12-31

----------
----------

Con esta misión quiero iniciar una serie de misiones con bombillas. Te ayudarán a comprender
el concepto de procesos y la evaluación del rendimiento de los procesos. En lugar de bombillas, en la vida
En lugar de bombillas, en la vida real puede haber equipos, cuya eficacia debe calcularse, o trabajadores que
van a trabajar, y hay que calcular su salario.

La primera misión es bastante sencilla. Hay una bombilla, que por defecto está apagada, y un botón, pulsando
con el que la bombilla cambia de estado. Esto significa que si la bombilla está apagada y se pulsa el botón
la luz se enciende, y si se vuelve a pulsar, se apaga.

(Todo es fácil. Estoy seguro de que si has llegado hasta esta misión, deberías entenderlo, pero por si acaso
añado una imagen).

La entrada de la función es un array de objetos datetime - esta es la fecha y la hora de pulsar el botón.
Tu tarea es determinar cuánto tiempo ha estado encendida la bombilla.

Entrada: Una lista de objetos datetime

Salida: Un número de segundos como un entero.

Ejemplo:
suma_luz([
    datetime(2015, 1, 12, 10, 0 , 0),
    datetime(2015, 1, 12, 10, 10 , 10),
]) == 610

sum_light([
    datetime(2015, 1, 12, 10, 0 , 0),
    datetime(2015, 1, 12, 10, 10 , 10),
    datetime(2015, 1, 12, 11, 0 , 0),
    datetime(2015, 1, 12, 11, 10 , 10),
]) == 1220

suma_luz([
    datetime(2015, 1, 12, 10, 0 , 0),
    datetime(2015, 1, 12, 10, 0 , 1),
]) == 1

Precondición:
La matriz de pulsar el botón siempre se ordena en orden ascendente
La matriz de pulsar el botón no tiene elementos repetidos (lo que significa que el resultado siempre debe ser mayor que 0)
La cantidad de elementos es siempre par (la luz se apagará eventualmente)
La fecha mínima posible es 1970-01-01
La fecha máxima posible es 9999-12-31
'''


from datetime import datetime, timedelta
from typing import List


def sum_light(els: List[datetime]) -> float:
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
