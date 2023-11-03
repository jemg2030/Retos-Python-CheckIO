"""
A positive integer n is a perfect power if it can be expressed as the power be for some
two integers b and e that are both greater than one. (Any positive integer n can always
be expressed as the trivial power n1, so we don't care about those.) For example, the
integers 32, 125 and 441 are perfect powers since they equal 25, 53 and 212, respectively.

This function should determine whether the positive integer n is a perfect power. Your
function needs to somehow iterate through a sufficient number of possible combinations
of b and e that could work, returning True right away when you find some b and e that
satisfy be == n, and returning False when all relevant possibilities for b and e have
been tried and found wanting.

Since n can get pretty large, your function should not examine too many combinations
above and beyond those that are both necessary and sufficient to reliably determine
the answer. Achieving this efficiency is the central educational point of this problem.

Input: Integer (int).

Output: Logic value (bool).

Examples:
assert perfect_power(8) == True
assert perfect_power(42) == False
assert perfect_power(441) == True
assert perfect_power(469097433) == True

Preconditions:

n > 0.
Related to the mission, you may be interested at Catalan's conjecture, these days a
proven mathematical theorem that says that after the special case of the two consecutive
perfect powers 8 and 9, whenever a positive integer n is a perfect power, n – 1 is never
a perfect power. For example, we don't have to slog through all potential ways to express
the number as an integer power to know from the get-go that 1234567890-1 is not a perfect
power. This also illustrates the common asymmetry between performing a computation to
opposite directions. Given some big chungus integer such as 4922235242952026704037113243122008064,
but not the formula that originally produced it, it is not quite easy to tell whether that integer
is a perfect power, or some perfect power plus minus one.

The mission was taken from Python CCPS 109. It is taught for Ryerson Chang School of Continuing
Education by Ilkka Kokkarinen

----------
----------

Un entero positivo n es una potencia perfecta si se puede expresar como la potencia be de
dos enteros b y e mayores que uno. (Cualquier entero positivo n siempre puede expresarse como
la potencia trivial n1, así que no nos preocupamos por ellas). Por ejemplo, los enteros 32,
125 y 441 son potencias perfectas ya que son iguales a 25, 53 y 212, respectivamente.

Esta función debe determinar si el entero positivo n es una potencia perfecta. Su función
necesita iterar de alguna manera a través de un número suficiente de posibles combinaciones
de b y e que podrían funcionar, devolviendo True de inmediato cuando encuentre algunas b y e
que satisfagan be == n, y devolviendo False cuando todas las posibilidades relevantes para b
y e hayan sido probadas y encontradas deficientes.

Dado que n puede ser muy grande, la función no debe examinar demasiadas combinaciones más
allá de las necesarias y suficientes para determinar la respuesta de forma fiable. Lograr esta
eficiencia es el punto educativo central de este problema.

Entrada: Entero (int).

Salida: Valor lógico (bool).

Ejemplos:
assert potencia_perfecta(8) == True
assert potencia_perfecta(42) == Falso
assert potencia_perfecta(441) == True
assert perfect_power(469097433) == True

Precondiciones:
n > 0.
En relación con la misión, puede que te interese la conjetura de Catalán, un teorema
matemático demostrado que dice que, después del caso especial de las dos potencias
perfectas consecutivas 8 y 9, siempre que un número entero positivo n es una potencia
perfecta, n - 1 nunca es una potencia perfecta. Por ejemplo, no tenemos que buscar todas
las formas posibles de expresar el número como una potencia entera para saber desde el
principio que 1234567890-1 no es una potencia perfecta. Esto también ilustra la asimetría
común entre realizar un cálculo en direcciones opuestas. Dado algún gran número entero
chungus como 4922235242952026704037113243122008064, pero no la fórmula que lo produjo
originalmente, no es muy fácil decir si ese número entero es una potencia perfecta, o
alguna potencia perfecta más menos uno.

La misión fue tomada de Python CCPS 109. Se enseña para Ryerson Chang Escuela de
Educación Continua por Ilkka Kokkarinen

https://en.wikipedia.org/wiki/Perfect_power
https://en.wikipedia.org/wiki/Catalan's_conjecture
https://github.com/ikokkari
"""


perfect_power = lambda n: any(
    round(n**e**-1) ** e == n for e in range(n.bit_length(), 1, -1)
)


print("Example:")
print(perfect_power(9))

# These "asserts" are used for self-checking
assert perfect_power(8) == True
assert perfect_power(42) == False
assert perfect_power(441) == True
assert perfect_power(469097433) == True
assert perfect_power(4922235242952026704037113243122008064) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
