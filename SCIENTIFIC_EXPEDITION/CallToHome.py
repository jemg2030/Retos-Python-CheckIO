'''
Nicola believes that Sophia calls Home too much and her phone bill is much too expensive.
He took the bills for Sophia's calls from the last few days and wants to calculate how much
did it cost.

The bill is represented as an array with information about the calls. Help Nicola to calculate
the cost for each of Sophia’s calls. Each call is represented as a string with date, time and
duration of the call in seconds in the following format:
"YYYY-MM-DD hh:mm:ss duration"
The date and time here are the start of the call.
Space-Time Communications Co. has several rules on how to calculate the cost of calls:

First 100 (one hundred) minutes in one day are priced at 1 coin per minute;
After 100 minutes in one day, each minute costs 2 coins per minute;
All calls are rounded up to the nearest minute. For example 59 sec ≈ 1 min, 61 sec ≈ 2 min;
Calls count to the day when they began. For example, if a call was started 2014-01-01 23:59:59,
then it should be counted to 2014-01-01;

For example:
2014-01-01 01:12:13 181
2014-01-02 20:11:10 600
2014-01-03 01:12:13 6009
2014-01-03 12:13:55 200
First day -- 181s≈4m -- 4 coins;
Second day -- 600s=10m -- 10 coins;
Third day -- 6009s≈101m + 200s≈4m -- 100 + 5 * 2 = 110 coins;
Total -- 124 coins.

Input: The information about calls as a tuple of strings.

Output: The total cost as an integer.

Example:
total_cost(("2014-01-01 01:12:13 181",
            "2014-01-02 20:11:10 600",
            "2014-01-03 01:12:13 6009",
            "2014-01-03 12:13:55 200")) == 124

How it is used: This mission will teach you how to parse and analyze various types of data.
Sometimes you don't need the full data and should single out only the important fragments.

Precondition: 0 < len(calls) ≤ 30
0 < call_duration ≤ 7200
The bill is sorted by datetime.

----------
----------

Nicola considera que Sophia llama demasiado a casa, y que su factura de teléfono es muy cara.
Por lo tanto, decide revisar las facturas de las últimas llamadas y se da a la tarea de calcular
exactamente cuánto le cuesta.

La factura telefónica se representa como una matriz con información sobre las llamadas.
Deberás ayudar a calcular el costo de cada llamada de Sophia, teniendo en cuenta que cada una
se representa como una cadena ( str ) con la fecha, hora y duración de la llamada (en segundos),
 usando el formato siguiente:
      "YYYY-MM-DD hh:mm:ss duration"
La fecha y la hora en esta información corresponden al inicio de la llamada.
Space-Time Communications Co. tiene varias reglas sobre cómo se calcula el costo de las llamadas:

Los primeros 100 (cien) minutos en un día tienen un precio de 1 moneda por minuto;
Después de 100 minutos en un día, cada minuto cuesta 2 monedas por minuto;
Todas las llamadas se redondean al minuto más cercano. Por ejemplo 59 sec ≈ 1 min, 61 sec ≈ 2 min;
Llamadas cuentan el día que comenzaron. Por ejemplo si la llamada se inició el 2014-01-01 23:59:59,
entonces cuenta en el 2014-01-01;

Por ejemplo:
2014-01-01 01:12:13 181
2014-01-02 20:11:10 600
2014-01-03 01:12:13 6009
2014-01-03 12:13:55 200
Primer día -- 181s≈4m -- 4 monedas;
Segundo día -- 600s=10m -- 10 monedas;
Tercer día -- 6009s≈101m + 200s≈4m -- 100 + 5 * 2 = 110 monedas;
Total -- 124 monedas.

Datos de Entrada: Información sobre las llamadas, como una tupla de cadenas ( str ).

Salida: El costo total, como un entero ( int ).

Ejemplo:
total_cost(("2014-01-01 01:12:13 181",
            "2014-01-02 20:11:10 600",
            "2014-01-03 01:12:13 6009",
            "2014-01-03 12:13:55 200")) == 124

¿Cómo se usa?: Esta misión te enseñará cómo leer y analizar diferentes tipos de datos.
En ocasiones no es necesario utilizar todos los datos proporcionados sino algunos
fragmentos importantes.

Condiciones: 0 < len(calls) ≤ 30
0 < call_duration ≤ 7200
La factura se ordena por fecha y hora.
'''


from typing import List
import math
from datetime import datetime


def total_cost(calls: List[str]) -> int:
    cost_by_day = {}
    for call in calls:
        date_str, time_str, duration_str = call.split()
        date = datetime.strptime(date_str, "%Y-%m-%d")
        duration = math.ceil(int(duration_str) / 60)  # convert to minutes and round up
        if date in cost_by_day:
            cost_by_day[date] += duration
        else:
            cost_by_day[date] = duration

    totalCost: int = 0
    for cost in cost_by_day.values():
        if cost <= 100:
            totalCost += cost
        else:
            totalCost += 100 + 2 * (cost - 100)
    return totalCost


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert total_cost(("2014-01-01 01:12:13 181",
                       "2014-01-02 20:11:10 600",
                       "2014-01-03 01:12:13 6009",
                       "2014-01-03 12:13:55 200")) == 124, "Base example"
    assert total_cost(("2014-02-05 01:00:00 1",
                       "2014-02-05 02:00:00 1",
                       "2014-02-05 03:00:00 1",
                       "2014-02-05 04:00:00 1")) == 4, "Short calls but money..."
    assert total_cost(("2014-02-05 01:00:00 60",
                       "2014-02-05 02:00:00 60",
                       "2014-02-05 03:00:00 60",
                       "2014-02-05 04:00:00 6000")) == 106, "Precise calls"
