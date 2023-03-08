'''
Computer date and time format consists only of numbers, for example: 21.05.2018 16:30.
Humans prefer to see something like this: 21 May 2018 year, 16 hours 30 minutes.
Your task is simple - convert the input date and time from computer format into a "human" format.

Input: Date and time as a string

Output: The same date and time, but in a more readable format as a string

Example:
assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
assert date_time("09.05.1945 06:07") == "9 May 1945 year 6 hours 7 minutes"
assert date_time('20.11.1990 03:55') == "20 November 1990 year 3 hours 55 minutes"
assert date_time('09.07.1995 16:01') == "9 July 1995 year 16 hours 1 minute"

How it is used: To improve the understanding between computers and humans.

Precondition :
0 < day <= 31
0 < month <= 12
1900 < year <= 3000
0 <= hours < 24
0 <= minutes < 60

---------
---------

El formato informático de fecha y hora consiste únicamente en números, por ejemplo: 21.05.2018 16:30.
Los humanos preferimos ver algo como esto 21 de mayo de 2018 año, 16 horas 30 minutos.
Su tarea es simple - convertir la fecha y la hora de entrada de formato de ordenador a un formato "humano".

Entrada: Fecha y hora como cadena

Salida: La misma fecha y hora, pero en un formato más legible como cadena de caracteres

Ejemplo:
assert fecha_hora("01.01.2000 00:00") == "1 de enero de 2000 año 0 horas 0 minutos"
assert date_time("09.05.1945 06:07") == "9 de mayo de 1945 año 6 horas 7 minutos"
assert date_time('20.11.1990 03:55') == "20 de noviembre de 1990 año 3 horas 55 minutos"
assert date_time('09.07.1995 16:01') == "9 de julio de 1995 año 16 horas 1 minuto"

Cómo se utiliza: Para mejorar el entendimiento entre ordenadores y humanos.

Precondición :
0 < día <= 31
0 < mes <= 12
1900 < año <= 3000
0 <= horas < 24
0 <= minutos < 60
'''


def date_time(time: str) -> str:
    # your code here
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
    date_time_parts = time.split()
    date_parts = date_time_parts[0].split('.')
    time_parts = date_time_parts[1].split(':')
    day = int(date_parts[0])
    month = int(date_parts[1])
    year = int(date_parts[2])
    hour = int(time_parts[0])
    minute = int(time_parts[1])
    month_name = months[month - 1]
    year_string = f"{year} year"
    hour_string = f"{hour} hours" if hour != 1 else "1 hour"
    minute_string = f"{minute} minutes" if minute != 1 else "1 minute"
    return f"{day} {month_name} {year_string} {hour_string} {minute_string}"


print("Example:")
print(date_time("01.01.2000 00:00"))

assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
assert date_time("09.05.1945 06:07") == "9 May 1945 year 6 hours 7 minutes"
assert date_time('20.11.1990 03:55') == "20 November 1990 year 3 hours 55 minutes"
assert date_time('09.07.1995 16:01') == "9 July 1995 year 16 hours 1 minute"

print("The mission is done! Click 'Check Solution' to earn rewards!")
