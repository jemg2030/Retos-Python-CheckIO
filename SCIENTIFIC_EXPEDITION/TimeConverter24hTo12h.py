'''
You prefer a good old 12-hour time format. But the modern world we live in would rather use the
24-hour format and you see it everywhere. Your task is to convert the time from the 24-h format
into 12-h format by following the next rules:

- the output format should be 'hh:mm a.m.' (for hours before midday) or 'hh:mm p.m.' (for hours after midday);
- if hours is less than 10 - don't write a '0' before it. For example: '9:05 a.m.'.
Here you can find some useful information about the 12-hour format.

Input: Time in the 24-hour format (as a string).

Output: Time in the 12-hour format (as a string).

Examples:
assert time_converter("12:30") == "12:30 p.m."
assert time_converter("09:00") == "9:00 a.m."

How it is used: For work with the different time formats.

Precondition: '00:00' <= time <= '23:59'

Also interesting fact about "12:00 p.m." and "12:00 a.m.". The name of this fact is "Confusion at
noon and midnight" - problem using "p.m./ a.m." with this magical time "12:00". You can find information
about this in Wikipedia or just google it.

----------
----------

Prefieres el formato de 12 horas. Pero el mundo moderno en el que vivimos prefiere el formato de
24 horas y lo ves por todas partes. Tu tarea es convertir la hora del formato de 24 horas al formato
de 12 horas siguiendo las siguientes reglas:

- el formato de salida debe ser 'hh:mm a.m.'. (para las horas anteriores al mediodía) o "hh:mm p.m."
(para las horas posteriores al mediodía). (para las horas posteriores al mediodía);
- si las horas son inferiores a 10, no escriba un "0" delante. Por ejemplo: '9:05 a.m.'.
Aquí encontrará información útil sobre el formato de 12 horas.

Introducir: Hora en el formato de 24 horas (como cadena).

Salida: Hora en el formato de 12 horas (como cadena).

Ejemplo:
assert convertidor_horario("12:30") == "12:30 p.m."
assert time_converter("09:00") == "9:00 a.m."

Cómo se utiliza: Para trabajar con los diferentes formatos de hora.

Precondición: '00:00' <= hora <= '23:59'

También es interesante el hecho de "12:00 p.m." y "12:00 a.m.". El nombre de este hecho es "Confusión
a mediodía y medianoche" - problema usando "p.m./ a.m." con esta hora mágica "12:00". Puedes encontrar
información sobre esto en Wikipedia o simplemente googlearlo.
'''


def time_converter(time):
    #replace this for solution
    # Split the input string into hours and minutes
    hours, minutes = time.split(":")

    # Convert hours and minutes to integers
    hours = int(hours)
    minutes = int(minutes)

    # Determine whether it's before midday or after midday
    if hours < 12:
        suffix = "a.m."
    else:
        suffix = "p.m."

    # Convert hours to the 12-hour format
    if hours == 0:
        hours = 12
    elif hours > 12:
        hours -= 12

    # Format the output string
    if hours < 10:
        return f"{hours}:{minutes:02d} {suffix}"
    else:
        return f"{hours}:{minutes:02d} {suffix}"


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
