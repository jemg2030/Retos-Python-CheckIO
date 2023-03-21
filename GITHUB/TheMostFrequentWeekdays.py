'''
What’s your favourite day of the week? Check if it's the most common day of the week in a year.

You are given a year as an integer (e. g. 2001). You should return the most frequent day(s) of
the week in that particular year. The result has to be a list of days sorted by the order of days
in a week (e. g. ['Monday', 'Tuesday']). Week starts with Monday.

Input: Year as an int .

Output: The list of most common days sorted by the order of days in a week (from Monday to Sunday).

Example:
most_frequent_days(1084) == ['Tuesday', 'Wednesday']
most_frequent_days(1167) == ['Sunday']

Preconditions: Year is between 1 and 9999. Week starts with Monday.

----------
----------

¿Cuál es su día favorito de la semana? Registra si es el día de la semana más común en un año.

Se le da un año como número entero (por ejemplo, 2001). Debe devolver el día o los días de la
semana más frecuentes en ese año concreto. El resultado debe ser una lista de días ordenados según
el orden de los días de la semana (p. ej. ['lunes', 'martes']). La semana empieza por el lunes.

Entrada: Año como int .

Salida: La lista de los días más comunes ordenados por el orden de los días de la semana (de lunes a domingo).

Ejemplo:
días_más_frecuentes(1084) == ['martes', 'miércoles']
días_más_frecuentes(1167) == ['Domingo']

Precondiciones: El año está comprendido entre 1 y 9999. La semana empieza por lunes.
'''


import datetime


def most_frequent_days(a):
    # your code here
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    counts = [0] * 7
    for month in range(1, 13):
        for day in range(1, 32):
            try:
                weekday = datetime.date(a, month, day).weekday()
                counts[weekday] += 1
            except ValueError:
                pass
    max_count = max(counts)
    return [days[i] for i in range(7) if counts[i] == max_count]


if __name__ == '__main__':
    print("Example:")
    print(most_frequent_days(1084))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert most_frequent_days(1084) == ['Tuesday', 'Wednesday']
    assert most_frequent_days(1167) == ['Sunday']
    assert most_frequent_days(1216) == ['Friday', 'Saturday']
    assert most_frequent_days(1492) == ['Friday', 'Saturday']
    assert most_frequent_days(1770) == ['Monday']
    assert most_frequent_days(1785) == ['Saturday']
    assert most_frequent_days(212) == ['Wednesday', 'Thursday']
    assert most_frequent_days(1) == ['Monday']
    assert most_frequent_days(2135) == ['Saturday']
    assert most_frequent_days(3043) == ['Sunday']
    assert most_frequent_days(2001) == ['Monday']
    assert most_frequent_days(3150) == ['Sunday']
    assert most_frequent_days(3230) == ['Tuesday']
    assert most_frequent_days(328) == ['Monday', 'Sunday']
    assert most_frequent_days(2016) == ['Friday', 'Saturday']
    print("Coding complete? Click 'Check' to earn cool rewards!")
