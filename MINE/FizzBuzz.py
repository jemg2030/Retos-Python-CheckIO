"""
"Fizz buzz" is a word game we will use to teach the robots about division. Let's learn computers.

You should write a function that will receive a positive integer and return:
"Fizz Buzz" if the number is divisible by 3 and by 5;
"Fizz" if the number is divisible by 3;
"Buzz" if the number is divisible by 5;
The number as a string for other cases.
Input: An integer (int).

Output: A string (str).

Examples:
assert checkio(15) == "Fizz Buzz"
assert checkio(6) == "Fizz"
assert checkio(10) == "Buzz"
assert checkio(7) == "7"

How it is used: Here you can learn how to write the simplest function and work with if-else statements.

Precondition: 0 < number ≤ 1000

----------
----------

"Fizz buzz" es un juego con palabras que usaremos para enseñarles a los robots acerca de la división.
Aprendamos de computadoras.

Tú deberías escribir una función que recibirá un entero positivo y devolver: "Fizz Buzz" si el
número es divisible por 3 y por 5;
"Fizz" si el número es divisible por 3;
"Buzz" si el número es divisible por 5;
El número como una cadena para los otros casos.
Entrada: Un número como un entero.

Salida: La respuesta como una cadena de caracteres.

Ejemplo:
assert checkio(15) == "Fizz Buzz"
assert checkio(6) == "Fizz"
assert checkio(10) == "Buzz"
assert checkio(7) == "7"

Cómo se usa: Aquí puedes aprender como escribir la función más simple y trabajar con las sentencias if-else.

Precondición: 0 < número ≤ 1000
"""


def checkio(number: int) -> str:
    # your code here
    if number % 3 == 0 and number % 5 == 0:
        return "Fizz Buzz"
    elif number % 3 == 0 and number % 5 != 0:
        return "Fizz"
    elif number % 5 == 0 and number % 3 != 0:
        return "Buzz"
    else:
        return str(number)


print("Example:")
print(checkio(15))

# These "asserts" are used for self-checking
assert checkio(15) == "Fizz Buzz"
assert checkio(6) == "Fizz"
assert checkio(10) == "Buzz"
assert checkio(7) == "7"

print("The mission is done! Click 'Check Solution' to earn rewards!")
