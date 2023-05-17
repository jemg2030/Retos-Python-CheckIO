'''
Quadratic Equation may be expressed as a product
a(x-x1)(x-x2) = 0,
where x1 and x2 are the solutions of equation, so called roots. After opening the brackets you
receive well known form
a*x**2 + b*x + c = 0.
This is what you should do in this mission. You have input list with integers - a, x1 [, x2]. If
it has length 2, it means, x1 == x2: equation has two equal roots (one distinct root). Your function
should return quadratic equation as a string. Pay attention to specific cases. Use Quadratic Formula
Calculator for recheck. Good luck!

Input: List with 2-3 integers.

Output: String.

Examples:
assert quadr_equation([2, 4, 6]) == "2*x**2 - 20*x + 48 = 0"
assert quadr_equation([-2, 4, 6]) == "-2*x**2 + 20*x - 48 = 0"
assert quadr_equation([2, 4, -4]) == "2*x**2 - 32 = 0"
assert quadr_equation([2, 4, 0]) == "2*x**2 - 8*x = 0"

How it’s used: Practice of automatic representing human-friendly view of equations.

Preconditions:
a != 0; abs(a) == 1 -> '[-]x**2'; a != abs(1) - > '[-]a*x**2'
exactly one whitespace around signs: [-]a*x**2 sign b*x sign c = 0
abs(b) == 1 -> [-]a*x**2 sign x sign c = 0
keep correct view and spacing when x1=x2=0, x1 or x2 = 0, x1=-x2

----------
----------

La ecuación cuadrática puede expresarse como un producto
a(x-x1)(x-x2) = 0,
donde x1 y x2 son las soluciones de la ecuación, las llamadas raíces. Tras abrir los
paréntesis se obtiene la conocida forma
a*x**2 + b*x + c = 0.
Esto es lo que debes hacer en esta misión. Usted tiene la lista de entrada con números
enteros - a, x1 [, x2]. Si tiene longitud 2, significa, x1 == x2: la ecuación tiene dos
raíces iguales (una raíz distinta). Su función debe devolver la ecuación cuadrática como
una cadena. Presta atención a los casos específicos. Utiliza la Calculadora de Fórmulas
Cuadráticas para volver a comprobarlo. Que tengas suerte.

Entrada: Lista con 2-3 enteros.

Salida: Cadena.

Ejemplo:
assert quadr_equation([2, 4, 6]) == "2*x**2 - 20*x + 48 = 0"
assert ecuación_cuadrada([-2, 4, 6]) == "-2*x**2 + 20*x - 48 = 0"
assert quadr_equation([2, 4, -4]) == "2*x**2 - 32 = 0"
assert quadr_equation([2, 4, 0]) == "2*x**2 - 8*x = 0"

Cómo se utiliza: Práctica de la representación automática de la vista amigable de ecuaciones.

Precondiciones:
a != 0; abs(a) == 1 -> '[-]x**2'; a != abs(1) - > '[-]a*x**2'
exactamente un espacio en blanco alrededor de los signos: [-]a*x**2 signo b*x signo c = 0
abs(b) == 1 -> [-]a*x**2 signo x signo c = 0
mantener la vista y el espaciado correctos cuando

Traducción realizada con la versión gratuita del traductor www.DeepL.com/Translator
'''


def quadr_equation(data: list[int]) -> str:
    # your code here
    if len(data) == 2: data.append(data[1])

    a, x1, x2 = data
    b = -a * (x1 + x2)
    c = a * x1 * x2

    terms = []

    for coefficient, pwr in zip([a, b, c], ['x**2', 'x', '']):
        if not coefficient: continue
        terms.append('-' if coefficient < 0 else '+')
        coefficient = abs(coefficient)
        term = str(coefficient) if coefficient > 1 or not pwr else ''
        terms.append(term + ('*' if pwr and term else '') + pwr)

    return ('-' if terms[0] == '-' else '') + ' '.join(terms[1:]) + ' = 0'


print("Example:")
print(quadr_equation([2, 4, 6]))

# These "asserts" are used for self-checking
assert quadr_equation([2, 4, 6]) == "2*x**2 - 20*x + 48 = 0"
assert quadr_equation([-2, 4, 6]) == "-2*x**2 + 20*x - 48 = 0"
assert quadr_equation([2, 4, -4]) == "2*x**2 - 32 = 0"
assert quadr_equation([2, 4, 0]) == "2*x**2 - 8*x = 0"
assert quadr_equation([2, 0]) == "2*x**2 = 0"
assert quadr_equation([2, 4]) == "2*x**2 - 16*x + 32 = 0"

print("The mission is done! Click 'Check Solution' to earn rewards!")
