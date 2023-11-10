"""
For the Robots the decimal format is inconvenient. If they need to count to "1", their
computer brains want to count it in the binary representation of that number. You can
read more about binary here .

You are given a number (a positive integer). You should convert it to the binary format
and count how many unities (1) are in the number spelling. For example: 5 = 0b101 contains
two unities, so the answer is 2.

Input: A number as a positive integer.

Output: The quantity of unities in the binary form as an integer.

Example:
checkio(4) == 1
checkio(15) == 4
checkio(1) == 1
checkio(1022) == 9

How it is used: How to convert a number to the binary form. It can be useful for Computer
Science purposes.

Precondition: 0 < number ≤ 2 32

----------
----------

Para los robots el formato decimal es inconveniente. Si necesitan contar hasta "1" Sus
cerebros informáticos quieren hacerlo con la representación binaria de este número. Puedes
leer más sobre números binarios aquí .

Se te proveerá número (un entero positivo), y deberás convertirlo al formato binario, para
contar cuántas unidades (1) hay en esta representación. Por ejemplo: 5 = 0b101, y contiene
dos unidades, por lo que la respuesta es 2.

Datos de Entrada: Un número, como un entero positivo (int).

Salida: La cantidad de unidades (1) de la representación binaria, como un entero (int).

Ejemplo:
checkio(4) == 1
checkio(15) == 4
checkio(1) == 1
checkio(1022) == 9

¿Cómo se usa?: La misión muestra cómo convertir un número a la forma binaria. Esto puede
ser útil para fines relacionados con Ciencias de la Computación.

Condiciones: 0 < número ≤ 2 32

Guido van Rossum, el autor de Python, es uno de nuestros jugadores más famosos. Él está
escribiendo algunas revisiones de código para las soluciones propuestas por nuestros jugadores.
"""


def checkio(number: int) -> int:
    return str(bin(number)).count("1")


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert checkio(4) == 1
    assert checkio(15) == 4
    assert checkio(1) == 1
    assert checkio(1022) == 9
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
