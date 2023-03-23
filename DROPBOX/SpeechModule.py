'''
Stephen's speech module is broken. This module is responsible for his number pronunciation. He has to
click to input all of the numerical digits in a figure, so when there are big numbers it can take him a
long time. Help the robot to speak properly and increase his number processing speed by writing a new
speech module for him. All the words in the string must be separated by exactly one space character. Be
careful with spaces - it's hard to see if you place two spaces instead one.

Input: An integer.

Output: String.

Examples:
assert checkio(1) == "one"
assert checkio(2) == "two"
assert checkio(3) == "three"
assert checkio(4) == "four"

How it is used: This concept may be useful for the speech synthesis software or automatic reports systems.
This system can also be used when writing a chatbot by assigning words or phrases numerical values and having
a system retrieve responses based on those values.

Precondition: 0 < number < 1000

----------
----------

El módulo del habla de Stephen está roto. Este módulo se encarga de la pronunciación de los números.
Tiene que hacer clic para introducir todos los dígitos numéricos de una cifra, así que cuando hay números
grandes puede tardar mucho tiempo. Ayuda al robot a hablar correctamente y aumenta su velocidad de
procesamiento de números escribiéndole un nuevo módulo de habla. Todas las palabras de la cadena deben
estar separadas exactamente por un espacio. Ten cuidado con los espacios - es difícil de ver si colocas
dos espacios en lugar de uno.

Entrada: Un número entero.

Salida: Una cadena.

Ejemplo:
assert checkio(1) == "uno"
assert checkio(2) == "dos"
assert checkio(3) == "tres"
assert checkio(4) == "cuatro"

Cómo se utiliza: Este concepto puede ser útil para el software de síntesis de voz o sistemas de
informes automáticos. También se puede utilizar al escribir un chatbot asignando valores numéricos
a palabras o frases y haciendo que un sistema recupere respuestas basadas en esos valores.

Precondición: 0 < número < 1000
'''


def checkio(num: int) -> str:
    # replace this for solution
    # Define mappings for single and double digit numbers
    ones = ['', 'one', 'two', 'three', 'four', 'five',
            'six', 'seven', 'eight', 'nine']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
             'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty',
            'sixty', 'seventy', 'eighty', 'ninety']

    # Handle special cases of 0 and 1000
    if num == 0:
        return "zero"
    elif num == 1000:
        return "one thousand"

    # Convert the num to a string and split into digits
    num_str = str(num)
    if len(num_str) == 3:
        hundreds_place = int(num_str[0])
        tens_place = int(num_str[1])
        ones_place = int(num_str[2])
    elif len(num_str) == 2:
        hundreds_place = 0
        tens_place = int(num_str[0])
        ones_place = int(num_str[1])
    else:
        hundreds_place = 0
        tens_place = 0
        ones_place = num

    # Construct the pronunciation based on the digit values
    pronunciation = ''
    if hundreds_place > 0:
        pronunciation += ones[hundreds_place] + ' hundred '
    if tens_place == 1:
        pronunciation += teens[ones_place] + ' '
    else:
        if tens_place > 1:
            pronunciation += tens[tens_place] + ' '
        if ones_place > 0:
            pronunciation += ones[ones_place]

    # Return the final pronunciation with no leading or trailing spaces
    return pronunciation.strip()


print("Example:")
print(checkio(4))

# These "asserts" are used for self-checking
assert checkio(1) == "one"
assert checkio(2) == "two"
assert checkio(3) == "three"
assert checkio(4) == "four"
assert checkio(5) == "five"
assert checkio(6) == "six"
assert checkio(9) == "nine"
assert checkio(10) == "ten"
assert checkio(11) == "eleven"
assert checkio(12) == "twelve"
assert checkio(13) == "thirteen"
assert checkio(14) == "fourteen"
assert checkio(15) == "fifteen"
assert checkio(16) == "sixteen"
assert checkio(17) == "seventeen"
assert checkio(18) == "eighteen"
assert checkio(19) == "nineteen"
assert checkio(999) == "nine hundred ninety nine"
assert checkio(784) == "seven hundred eighty four"
assert checkio(777) == "seven hundred seventy seven"
assert checkio(88) == "eighty eight"
assert checkio(44) == "forty four"
assert checkio(20) == "twenty"
assert checkio(30) == "thirty"
assert checkio(40) == "forty"
assert checkio(50) == "fifty"
assert checkio(80) == "eighty"
assert checkio(90) == "ninety"
assert checkio(100) == "one hundred"
assert checkio(200) == "two hundred"
assert checkio(300) == "three hundred"
assert checkio(600) == "six hundred"
assert checkio(700) == "seven hundred"
assert checkio(900) == "nine hundred"
assert checkio(21) == "twenty one"
assert checkio(312) == "three hundred twelve"
assert checkio(302) == "three hundred two"
assert checkio(509) == "five hundred nine"
assert checkio(753) == "seven hundred fifty three"
assert checkio(940) == "nine hundred forty"
assert checkio(999) == "nine hundred ninety nine"

print("The mission is done! Click 'Check Solution' to earn rewards!")
