'''
The first solid-state electronic calculator was created in the early 1960s. Pocket-sized devices
became available in the 1970s, especially after the Intel 4004, the first microprocessor, was
developed by Intel for the Japanese calculator company Busicom. They later became used commonly
within the petroleum industry (oil and gas). Find more on wikipedia page...

In this series of missions you are going to build an elementary calculator.

As an input, you get a sequence of keys pressed, and, as the result of that function, you should
show what will be shown on the screen when the last key is pressed. Be attentive, it's not always
the result of the expression. Actually, playing with the physical calculator or app will really
help you to catch edge cases.

In the first mission only digits and single signs (only +, -, =) between them are used.

Expected behavior:
beginning zeros should be removed, only-zeros number - converted to single zero.

Input: String.

Output: String.

Examples:
assert calculator("000000") == "0"
assert calculator("0000123") == "123"
assert calculator("12") == "12"
assert calculator("+12") == "12"

How it’s used: Calculators are widely used. Understanding the principles of its input and output
are interesting and useful.

Precondition: Allowed characters: digits (0-9), single signs plus (+), minus (-) or equation (=)
between digit blocks. NO combinations of signs (+=, +- etc.).

----------
----------

La primera calculadora electrónica de estado sólido se creó a principios de los años sesenta. Los
dispositivos de bolsillo empezaron a estar disponibles en los años 70, sobre todo después de que
Intel desarrollara el Intel 4004, el primer microprocesador, para la empresa japonesa de calculadoras
Busicom. Más tarde, su uso se generalizó en la industria petrolera (petróleo y gas). Más información
en la página de wikipedia...

En esta serie de misiones vas a construir una calculadora elemental.

Como entrada, obtendrás una secuencia de teclas pulsadas y, como resultado de esa función, deberás
mostrar lo que aparecerá en la pantalla cuando se pulse la última tecla. Estate atento, no siempre
es el resultado de la expresión. En realidad, jugar con la calculadora física o con la aplicación
te ayudará mucho a detectar los casos extremos.

En la primera misión sólo se utilizan dígitos y signos simples (sólo +, -, =) entre ellos.

Comportamiento esperado:
Los ceros iniciales deben ser eliminados, el número de sólo ceros - convertido a un solo cero.

Entrada: Cadena.

Salida: Cadena.

Ejemplo:
assert calculadora("000000") == "0"
assert calculator("0000123") == "123"
assert calculator("12") == "12"
assert calculator("+12") == "12"

Cómo se utiliza: El uso de las calculadoras está muy extendido. Comprender los principios de su
entrada y salida es interesante y útil.

Condición previa: Caracteres permitidos: dígitos (0-9), signos simples más (+), menos (-) o ecuación
(=) entre bloques de dígitos. NO combinaciones de signos (+=, +- etc.).
'''


def calculator(log: str) -> str:
    # your code here
    prev, current, save, operation = 0, 0, False, '='

    for key in log:
        if key.isdigit():
            current, save = current * 10 * save + int(key), True
        elif key in '+-=':
            prev = current = prev + current if operation == '+' else prev - current if operation == '-' else current
            operation, save = key, False

    return str(current)


print("Example:")
print(calculator("1+2"))

# These "asserts" are used for self-checking
assert calculator("000000") == "0"
assert calculator("0000123") == "123"
assert calculator("12") == "12"
assert calculator("+12") == "12"
assert calculator("") == "0"
assert calculator("1+2") == "2"
assert calculator("2+") == "2"
assert calculator("1+2=") == "3"
assert calculator("1+2-") == "3"
assert calculator("1+2=2") == "2"
assert calculator("=5=10=15") == "15"

print("The mission is done! Click 'Check Solution' to earn rewards!")
