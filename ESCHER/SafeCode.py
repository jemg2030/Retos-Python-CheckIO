'''
Your hunch was right, in addition to the usual room stuff, such as a bookcase, wardrobe, desk and a bed,
there also was a quite sizeable vault. Your mood immediately improved - this trip very quickly became
profitable (unless, of course, the vault wasn’t empty).

A small sheet of thick paper laid on the table next to the vault. There were some kind of formulas with
wiped out figures written on it. It’s likely that a long time ago these notes were quite easy to read,
but the decades spent in the castle negatively affected the readability of some figures. By figuring
out what figures were originally written, you’ll be able to find the correct combination for opening
of the vault.
Your task is to create a function that as input receives an equation in a form of a string with digits,
erased places ('#') and one of the three arithmetic operations (+, - or *), for example - "##*##=302#".
As a result, your function should return a digit (from the interval 0-9), which when applied instead of
all #, made the equation correct. Or -1 (minus one) if this isn’t possible.

Important note - none of the figures that already are in the equation can be in place of #. Also, if after
the equal sign (=) there are 2 or more missing symbols, the answer cannot consist of zeros (00, 000, etc.).
Numbers in the format like #n, #nn and so on, where n - any digit, can't start with 0. For example, "#9+3=12" == -1.
In case there are several suitable digits - use the smallest of them. The numbers in the formula can be both
positive (for example, "1+1=#") and negative, with the "-" sign before them ("19--45=5#", "-1*-6=#").

Input: Cypher.

Output: Digit of the safe code.

Example:
safe_code("-5#*-1=5#") == 0
safe_code("##*##=302#") == 5
safe_code("19--45=5#") == -1
safe_code("#9+3=12") == -1

How it is used: In the cryptography for the important information protection.

Precondition :
answer - [0-9] or -1

----------
----------

Tu corazonada fue acertada: además de las cosas habituales de la habitación, como una librería, un armario,
un escritorio y una cama, también había una cámara acorazada bastante grande. Tu estado de ánimo mejora de
inmediato: este viaje se convierte rápidamente en rentable (a menos, claro está, que la cámara acorazada no
esté vacía).

Sobre la mesa, junto a la cámara, había una pequeña hoja de papel grueso. En ella había escritas una especie
de fórmulas con cifras borradas. Es probable que hace mucho tiempo estas notas fueran bastante fáciles de leer,
pero las décadas pasadas en el castillo afectaron negativamente a la legibilidad de algunas cifras. Si averiguas
qué cifras estaban escritas originalmente, podrás encontrar la combinación correcta para abrir la cámara acorazada.
Tu tarea consiste en crear una función que como entrada reciba una ecuación en forma de cadena con dígitos,
lugares borrados ('#') y una de las tres operaciones aritméticas (+, - o *), por ejemplo - "##*##=302#". Como
resultado, tu función debería devolver un dígito (del intervalo 0-9), que al aplicarse en lugar de todos los #,
hiciera correcta la ecuación. O -1 (menos uno) si esto no es posible.

Nota importante - ninguna de las cifras que ya están en la ecuación puede estar en lugar de #. Además, si
después del signo igual (=) faltan 2 o más símbolos, la respuesta no puede consistir en ceros (00, 000, etc.).
Los números con el formato #n, #nn, etc., donde n es un dígito cualquiera, no pueden empezar por 0. Por ejemplo,
"#9+3=12" == -1.
En caso de que haya varios dígitos adecuados, utilice el menor de ellos. Los números de la fórmula pueden ser
tanto positivos (por ejemplo, "1+1=#") como negativos, con el signo "-" delante ("19--45=5#", "-1*-6=#").

Entrada: Cifrado.

Salida: Dígito del código seguro.

Ejemplo:
safe_code("-5#*-1=5#") == 0
safe_code("##*##=302#") == 5
safe_code("19--45=5#") == -1
safe_code("#9+3=12") == -1

Cómo se utiliza: En la criptografía para la protección de información importante.

Precondición :
respuesta - [0-9] o -1
'''


def safe_code(equation):
    #replace this for solution
    temp = equation.replace('=', '==')
    if temp.index('#') and equation[equation.index('=') + 1] != '#' and '0' not in equation:
        try:
            temp_1 = temp.replace('#', '0')
            if eval(temp_1):
                return 0
        except:
            pass

    # 1-9
    for i in range(1, 10):
        if str(i) not in equation:
            try:
                temp_1 = temp.replace('#', str(i))
                if eval(temp_1):
                    return i
            except:
                pass
    return -1


if __name__ == '__main__':
    print("Example:")
    print(safe_code("-5#*-1=5#"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_code("-5#*-1=5#") == 0
    assert safe_code("##*##=302#") == 5
    assert safe_code("19--45=5#") == -1
    assert safe_code("##--11=11") == -1
    assert safe_code("#9+3=22") == 1
    assert safe_code("11*#=##") == 2
    assert safe_code("#9+3=12") == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")
