'''
Sofia cracks open the treasure chest. Inside are slips of paper with six digit numbers on each slip.

“What’s this?” She asks, quizzed. “Nikola, are these what I think they are?”

“They look like lucky tickets! Look at how many there are, there must be hundreds! Any of them could be
a winner!”

“Oh man! We could turn them into the lucky ticket commission and collect the reward! I could pay my dad
back for the spaceship!”

“Er, you didn’t buy it yourself?” Stephen asked Sofia.

“Well, not as such. I borrowed the money from my dad on the condition that I’d pay him back. Now maybe I can!”

Stephen sighed. “Well, let’s check the tickets to see if we have a winner.”

“I have an idea. I brought my Number Cruncher 5000 along. I’ll just write a quick function to find out if
we won so we don’t have to do it all manually.” Nikola interjected.

“Quickly, quickly!” Sofia said. “I’m so excited!”

The "Mathematically lucky tickets" concept is similar to the idea of the Russian "Lucky tickets". It refers
to the old public transport tickets that had 6-digit numbers printed on them.

You are given a ticket number and the combination of its digits can become a mathematical expression by
following these rules.

    1. The digits of the number can be split into groups of numbers.
    2. You cannot change the order of groups or digits.
    3. Each group is treated as a one integer number (1 and 2 would become 12, etc.).
    4. Operational signs (+, -, * and /) are placed between the groups.
    5. Parenthesis are placed around subexpressions to eliminate any ambiguity
    in the evaluation order.
For example:
    * 238756 -> (2 * (38 + ((7 + 5) * 6)))
    * 000859 -> (0 + (00 + (8 + (5 + 9))))
    * 561403 -> (5 * (6 + (1 + (40 / 3))))
The ticket is considered mathematically lucky if no combination of its digits evaluates to 100. For example:
    * 000000 is obviously lucky, no matter which combination you construct it always
    evaluates to zero;
    * 707409 and 561709 are also lucky because they cannot evaluate to 100;
    * 595347 is not lucky: (5 + ((9 * 5) + (3 + 47))) = 100;
    * 593347 is not lucky: (5 + ((9 / (3 / 34)) - 7)) = 100;
    * 271353 is not lucky: (2 - (7 * (((1 / 3) - 5) * 3))) = 100.
The combination has to evaluate to 100 exactly to be counted as unlucky. Fractions can occur in intermediate
calculations (like in above examples for 593347 and 271353) but the result must be an integer.

Task: Given a 6-digit number of the ticket, the program should determine whether it is mathematically lucky or not.

Input: 6-digits as a string.

Output: Is it mathematically lucky or not as a boolean.

Examples:
assert checkio("000000") == True
assert checkio("707409") == True
assert checkio("595347") == False
assert checkio("271353") == False

How it is used: This is a nice game to improve mind-calculation skills. If you have coder or math-geek
friends, then you can give them this as a challenge. Who’s code will check digits faster than the others?
After solving this task you will have the skills to cheat! ;-)

Precondition: |digits| == 6

----------
----------

números de seis cifras.

"¿Qué es esto?" Pregunta, interrogada. "Nikola, ¿son lo que creo que son?".

"¡Parecen boletos de la suerte! Mira cuántos hay, ¡debe de haber cientos! Cualquiera de ellos podría
ser el ganador".

"¡Oh tío! ¡Podríamos convertirlos en la comisión de los boletos de la suerte y cobrar la recompensa!
¡Podría pagarle a mi padre la nave espacial!"

"Eh, ¿no la compraste tú?" preguntó Stephen a Sofía.

"Bueno, no como tal. Le pedí prestado el dinero a mi padre con la condición de que se lo devolvería.
Ahora quizá pueda".

Stephen suspiró. "Bueno, vamos a registrar los boletos para ver si tenemos un ganador".

"Tengo una idea. He traído mi Number Cruncher 5000. Escribiré una función rápida para saber si hemos
ganado y así no tendremos que hacerlo todo manualmente". Nikola intervino.

"¡Rápido, rápido!" dijo Sofía. "¡Estoy tan emocionada!"

El concepto de "boletos matemáticamente afortunados" es similar a la idea de los "boletos de la suerte"
rusos. Se refiere a los antiguos billetes de transporte público que llevaban impresos números de 6 cifras.

Te dan un número de billete y la combinación de sus dígitos puede convertirse en una expresión matemática
siguiendo estas reglas.

    1. Las cifras del número se pueden dividir en grupos de cifras.
    2. No se puede cambiar el orden de los grupos ni de los dígitos.
    3. Cada grupo se trata como un número de un entero (1 y 2 se convertirían en 12, etc.).
    4. Los signos operativos (+, -, * y /) se colocan entre los grupos.
    5. 5. Se colocan paréntesis alrededor de las subexpresiones para eliminar cualquier ambigüedad
    en el orden de evaluación.

Por ejemplo
    * 238756 -> (2 * (38 + ((7 + 5) * 6)))
    * 000859 -> (0 + (00 + (8 + (5 + 9))))
    * 561403 -> (5 * (6 + (1 + (40 / 3))))

El billete se considera matemáticamente afortunado si ninguna combinación de sus dígitos se evalúa a 100.
Por ejemplo:
    * 000000 es obviamente afortunado, no importa la combinación que construyas siempre
    siempre es igual a cero;
    * 707409 y 561709 también son afortunados porque no pueden evaluarse a 100;
    * 595347 no es afortunado: (5 + ((9 * 5) + (3 + 47))) = 100;
    * 593347 no tiene suerte: (5 + ((9 / (3 / 34)) - 7)) = 100;
    * 271353 no tiene suerte: (2 - (7 * (((1 / 3) - 5) * 3))) = 100.

La combinación debe evaluarse exactamente en 100 para que se considere no afortunada. En los cálculos
intermedios pueden aparecer fracciones (como en los ejemplos anteriores de 593347 y 271353), pero el
resultado debe ser un número entero.

Tarea: Dado un número de 6 dígitos del boleto, el programa debe determinar si es matemáticamente afortunado o no.

Entrada: 6-dígitos como cadena.

Salida: Es matemáticamente afortunado o no como booleano.

Ejemplos:
assert checkio("000000") == True
assert checkio("707409") == True
assert checkio("595347") == False
assert checkio("271353") == False

Cómo se utiliza: Este es un buen juego para mejorar las habilidades de cálculo mental. Si tienes amigos
programadores o aficionados a las matemáticas, puedes proponérselo como reto. ¿Quién registrará los
dígitos más rápido que los demás? Después de resolver esta tarea estarás capacitado para hacer trampas ;-)

Precondición: |digits| == 6
'''


def combine(x, y):
    return [x+y, x-y, x*y] + ([x/y] if y != 0 else [])


def checkio(value: str) -> bool:
    # your code here
    N = len(value)
    gen = {}
    for l in range(1, N + 1):
        for i in range(0, N + 1 - l):
            gen[i, l] = {int(value[i:i + l])}
            for k in range(1, l):
                gen[i, l] |= set(g for x in gen[i, k] for y in gen[i + k, l - k]
                                 for g in combine(x, y))
    return 100 not in gen[0, N]


print("Example:")
print(checkio("000000"))

# These "asserts" are used for self-checking
assert checkio("000000") == True
assert checkio("707409") == True
assert checkio("595347") == False
assert checkio("271353") == False
assert checkio("000955") == False
assert checkio("100478") == True
assert checkio("100479") == False
assert checkio("725126") == True
assert checkio("836403") == False
assert checkio("240668") == False
assert checkio("082140") == True
assert checkio("574699") == False
assert checkio("324347") == False
assert checkio("064377") == True
assert checkio("111111") == False
assert checkio("555555") == False
assert checkio("777777") == False
assert checkio("392039") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
