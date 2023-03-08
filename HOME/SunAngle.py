'''
Every true traveler must know how to do 3 things: fix the fire, find the water and extract useful information
from the nature around him. Programming won't help you with the fire and water, but when it comes to the
information extraction - it might be just the thing you need.

Your task is to find the angle of the sun above the horizon knowing the time of the day. Input data: the sun
rises in the East at 6:00 AM, which corresponds to the angle of 0 degrees. At 12:00 PM the sun reaches its
zenith, which means that the angle equals 90 degrees. 6:00 PM is the time of the sunset so the angle is 180
degrees. If the input will be the time of the night (before 6:00 AM or after 6:00 PM), your function should
return - "I don't see the sun!".

Input: The time of the day.

Output: The angle of the sun, rounded to 2 decimal places.

Example:
assert sun_angle("07:00") == 15
assert sun_angle("12:15") == 93.75

How it is used: One day it can save your life, if you'll be lost far away from civilization.

Precondition :
00:00 <= time <= 23:59

---------
---------

Todo verdadero viajero debe saber hacer 3 cosas: arreglar el fuego, encontrar el agua y extraer información
útil de la naturaleza que le rodea. La programación no te ayudará con el fuego y el agua, pero cuando se trata
de extraer información, puede ser justo lo que necesitas.

Tu tarea consiste en encontrar el ángulo del sol sobre el horizonte conociendo la hora del día. Datos de entrada:
el sol sale por el Este a las 6:00 AM, lo que corresponde al ángulo de 0 grados. A las 12:00 PM el sol alcanza su
cenit, lo que significa que el ángulo es igual a 90 grados. A las 6:00 PM es la hora de la puesta de Sol, por lo
que el ángulo es de 180 grados. Si la entrada será la hora de la noche (antes de las 6:00 AM o después de las 6:00 PM),
su función debería devolver - "¡No veo el sol!".

Entrada: La hora del día.

Salida: El ángulo del sol, redondeado a 2 decimales.

Ejemplo:
assert ángulo_del_sol("07:00") == 15
assert ángulo_del_sol("12:15") == 93.75

Cómo se utiliza: Un día puede salvarte la vida, si te pierdes lejos de la civilización.

Precondición :
00:00 <= hora <= 23:59
'''


from typing import Union


def sun_angle(time: str) -> Union[float, str]:
    # replace this for solution
    hours, minutes = map(int, time.split(':'))
    total_minutes = hours * 60 + minutes
    angle = (total_minutes - 360) * 0.25
    if 0 <= angle <= 180:
        return round(angle, 2)
    else:
        return "I don't see the sun!"


print("Example:")
print(sun_angle("07:00"))

assert sun_angle("07:00") == 15
assert sun_angle("12:15") == 93.75

print("The mission is done! Click 'Check Solution' to earn rewards!")
