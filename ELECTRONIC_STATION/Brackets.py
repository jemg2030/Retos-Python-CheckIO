'''
“Great!” Exclaimed Sofia. “Now we have the password.”

“To what exactly?” Quipped Nikola.

“Untold treasures, vast riches beyond belief! Gold! Silver! Silicon! Hydraulic Fluid! Anything your heart desires!”

“And you’re going to do what with a password to absolutely nothing?” Nikola smirked.

“Oh... Right...”

Stephen spoke up. “Well, this door back here has a keypad. Only thing is the brackets look pretty
busted up. We could try fixing it and then punching in the password?”

“YES! That!” Sofia exclaimed.

You are given an expression with numbers, brackets and operators. For this task only the
brackets matter. Brackets come in three flavors: "{}" "()" or "[]". Brackets are used to determine
scope or to restrict some expression. If a bracket is open, then it must be closed with a closing
bracket of the same type. The scope of a bracket must not intersected by another bracket. In this
task you should make a decision, whether to correct an expression or not based on the brackets.
Do not worry about operators and operands.

Input: An expression with different of types brackets as a string (unicode).

Output: A verdict on the correctness of the expression in boolean (True or False).

Example:

assert checkio("((5+3)*2+1)") == True
assert checkio("{[(3+1)+2]+}") == True
assert checkio("(3+{1-1)}") == False
assert checkio("[1+1]+(2*2)-{3/3}") == True
assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False
assert checkio("[(3)+(-1)]*{3}") == True
assert checkio("(((([[[{{{3}}}]]]]))))") == False
assert checkio("[1+202]*3*({4+3)}") == False
assert checkio("({[3]})-[4/(3*{1001-1000}*3)/4]") == True
assert checkio("[[[1+[1+1]]])") == False
assert checkio("(((1+(1+1))))]") == False
assert checkio("2+3") == True

How it is used: When you write code or complex expressions in a mathematical package, you can get a
huge headache when it comes to excess or missing brackets. This concept can be useful for your own IDE.

Precondition:
There are only brackets ("{}" "()" or "[]"), digits or operators ("+" "-" "*" "/").
0 < len(expression) < 10 3

----------
----------

Genial!", exclamó Sofía. "Ahora tenemos la contraseña."

"¿De qué exactamente?", bromeó Nikola.

““¡Tesoros increíbles. Vastas riquezas más allá de la imaginación! ¡Oro, Plata y Silicio! ¡Fluido
hidráulico! ¡Cualquier cosa que tu corazón desee!”

“¿Y qué es lo que vas a hacer con una contraseña?” Nikola sonrió.

“Oh, eso...”

Stephen habló. "Bueno, esta puerta de aquí tiene un teclado. Lo único es que los paréntesis están en muy
mal estado. ¿Podríamos intentar arreglarlo y luego de ingresar la contraseña? "

"¡SÍ! ¡Exactamente! ", exclamó Sofía..

Se te dará una expresión con números, paréntesis y operadores. Para esta tarea sólo los paréntesis importan.
Recuerda que paréntesis es una designación general que usamos para varios tipos: "{}" "()" o "[]" (corchetes,
paréntesis y llaves). Estos signos se utilizan para determinar el alcance o restringir alguna expresión. Si
un paréntesis, corchete o llave se abre, entonces deberá cerrarse en algún punto con un signo de cierre del
mismo tipo. El alcance de un paréntesis no deberá ser intersectado por el de otro. En esta tarea deberás
decidir si se debe corregir o no una expresión, basándose en los paréntesis (o corchetes o llaves) que
incluye. No te preocupes por los operadores y los operandos.

Datos de Entrada: Una expresión con diferentes tipos de paréntesis (corchetes, paréntesis y/o llaves) como una cadena (unicode)..

Salida: Un veredicto indicando si la expresión es correcta, como un booleano (v erdadero o falso ).

Ejemplo:
assert checkio("((5+3)*2+1)") == True
assert checkio("{[(3+1)+2]+}") == True
assert checkio("(3+{1-1)}") == False
assert checkio("[1+1]+(2*2)-{3/3}") == True
assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False
assert checkio("[(3)+(-1)]*{3}") == True
assert checkio("(((([[[{{{3}}}]]]]))))") == False
assert checkio("[1+202]*3*({4+3)}") == False
assert checkio("({[3]})-[4/(3*{1001-1000}*3)/4]") == True
assert checkio("[[[1+[1+1]]])") == False
assert checkio("(((1+(1+1))))]") == False
assert checkio("2+3") == True

¿Cómo se usa?: Al escribir código o expresiones complejas en paquetes matemáticos, puedes tener enormes
dolores de cabeza cuando se trata de paréntesis en exceso o faltantes. Este concepto puede ser útil para
tu propio IDE.

Condiciones:
Sólo hay paréntesis ("{}" "()" or "[]"), dígitos u operadores ("+" "-" "*" "/").
0 < len(expression) < 10 3
'''


def checkio(expression: str) -> bool:
    stack = []
    bracket_pairs = {'(': ')', '{': '}', '[': ']'}
    for char in expression:
        if char in bracket_pairs.keys():
            stack.append(char)
        elif char in bracket_pairs.values():
            if not stack:
                return False
            opening_bracket = stack.pop()
            if bracket_pairs[opening_bracket] != char:
                return False
    return not stack


# These "asserts" using only for self-checking and not necessary for auto-testing

print("Example:")
print(checkio("((5+3)*2+1)"))

assert checkio("((5+3)*2+1)") == True
assert checkio("{[(3+1)+2]+}") == True
assert checkio("(3+{1-1)}") == False
assert checkio("[1+1]+(2*2)-{3/3}") == True
assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False
assert checkio("[(3)+(-1)]*{3}") == True
assert checkio("(((([[[{{{3}}}]]]]))))") == False
assert checkio("[1+202]*3*({4+3)}") == False
assert checkio("({[3]})-[4/(3*{1001-1000}*3)/4]") == True
assert checkio("[[[1+[1+1]]])") == False
assert checkio("(((1+(1+1))))]") == False
assert checkio("2+3") == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
