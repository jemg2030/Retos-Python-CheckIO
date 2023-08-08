"""
Stephan and Sophia forget about security and use simple passwords for everything. Help Nikola
develop a password security check module. The password will be considered strong enough if its
length is greater than or equal to 10 symbols, it has at least one digit, as well as containing
one uppercase letter and one lowercase letter in it. The password contains only ASCII latin letters
or digits.

Input: A password as a string (str).

Output: Is the password safe or not as a logic value (bool).

Examples:
assert checkio("ULFFunH8ni") == True
assert checkio("aaaaaaaaaaaaaaaaaaaaa") == False
assert checkio("aA1") == False
assert checkio("awzbdzkfz") == False

How it is used: If you are worried about the security of your app or service, you can check your
users' passwords for complexity. You can use these skills to require that your users passwords meet
more conditions (punctuations or unicode).

Preconditions:
re.match("[a-zA-Z0-9]+", password);
0 < len(password) ≤ 64.

----------
----------

Stephan y Sophia no se preocupan por la seguridad y usan contraseñas sencillas para todo.
Ayuda a a Nikola a desarrollar un módulo para verificar la seguridad de la contraseña o
password. La contraseña será considerada suficientemente fuerte si el largo es mayor o igual a
10 caracteres, tiene por lo menos un dígito, así como una letra en mayúscula y una letra en minúscula.
La contraseña contiene solo letras latinas o dígitos ASCII.

Entrada: La contraseña como una cadena o string.

Salida: Si la contraseña es segura o no representada mediante un booleano o cualquier otro tipo
de dato que pueda ser convertido y procesado como un booleano. En los resultados finales podrás
ver los resultados convertidos.

Ejemplo:
assert checkio("ULFFunH8ni") == True
assert checkio("aaaaaaaaaaaaaaaaaaaaa") == False
assert checkio("aA1") == False
assert checkio("awzbdzkfz") == False

¿Cómo es usado?: Si te preocupa la seguridad de tu aplicación o servicio, puedes verificar la
complejidad de las contraseñas de tus usuarios. Puedes usar estas habilidades para requerir a tus
usuarios contraseñas que cumplan con más condiciones (puntuaciones o unicode).

Pre-condición:
re.match("[a-zA-Z0-9]+", password)
0 < len(password) ≤ 64
"""


import re


def checkio(data: str) -> bool:

    # replace this for solution
    if 10 <= len(data) <= 64:
        pattern = re.compile(r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{10,}$")
        if pattern.match(data):
            return True
    return False


# Some hints
# Just check all conditions


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("A1213pokl") == False, "1st example"
    assert checkio("bAse730onE4") == True, "2nd example"
    assert checkio("asasasasasasasaas") == False, "3rd example"
    assert checkio("QWERTYqwerty") == False, "4th example"
    assert checkio("123456123456") == False, "5th example"
    assert checkio("QwErTy911poqqqq") == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
