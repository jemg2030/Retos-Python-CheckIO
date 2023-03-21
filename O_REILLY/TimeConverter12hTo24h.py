'''
You are the modern man who prefers the 24-hour time format. But the 12-hour format is used in some places.
Your task is to convert the time from the 12-h format into 24-h by following the next rules:
- the output format should be 'hh:mm'
- if the output hour is less than 10 - write '0' before it. For example: '09:05'
Here you can find some useful information about the 12-hour format .

Input: Time in a 12-hour format (as a string).

Output: Time in a 24-hour format (as a string).

Example:
time_converter('12:30 p.m.') == '12:30'
time_converter('9:00 a.m.') == '09:00'
time_converter('11:15 p.m.') == '23:15'

How it is used: For work with the different time formats.

Precondition :
'00:00' <= time <= '23:59'

Also interesting fact about "12:00 p.m." and "12:00 a.m.". The name of this fact is "Confusion at noon and
midnight" - problem using "p.m./ a.m." with this magical time "12:00". You can find information about this in
Wikipedia or just google it.

----------
----------

Usted es el hombre moderno que prefiere el formato de 24 horas. Pero en algunos lugares se utiliza el
formato de 12 horas. Tu tarea es convertir la hora del formato de 12-h a 24-h siguiendo las siguientes reglas:
- El formato de salida debe ser 'hh:mm'.
- si la hora de salida es inferior a 10 - escriba '0' antes de ella. Por ejemplo: '09:05'.
Aquí encontrará información útil sobre el formato de 12 horas.

Entrada: Hora en formato de 12 horas (como cadena).

Salida: Hora en formato de 24 horas (como cadena).

Ejemplo:
time_converter('12:30 p.m.') == '12:30'
time_converter('9:00 a.m.') == '09:00'
time_converter('11:15 p.m.') == '23:15'

Cómo se utiliza: Para trabajar con los diferentes formatos de hora.

Precondición :
'00:00' <= hora <= '23:59'

También hecho interesante sobre "12:00 p.m." y "12:00 a.m.". El nombre de este hecho es "Confusión a
mediodía y medianoche" - problema usando "p.m./ a.m." con esta hora mágica "12:00". Puedes encontrar información
sobre esto en Wikipedia o simplemente googlearlo.
'''


def time_converter(time):
    # replace this for solution
    time = time.strip().split()
    hour, minute = time[0].split(':')
    if time[1].lower() == 'p.m.' and hour != '12':
        hour = str(int(hour) + 12)
    elif time[1].lower() == 'a.m.' and hour == '12':
        hour = '00'
    return f"{hour.zfill(2)}:{minute}"


if __name__ == "__main__":
    print("Example:")
    print(time_converter("12:30 p.m."))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter("12:30 p.m.") == "12:30"
    assert time_converter("9:00 a.m.") == "09:00"
    assert time_converter("11:15 p.m.") == "23:15"
    print("Coding complete? Click 'Check' to earn cool rewards!")
