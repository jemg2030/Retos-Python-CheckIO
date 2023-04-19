'''
In mathematics and mathematical logic, Boolean algebra is a sub-area of algebra in which the values of
the variables are true or false, typically denoted with 1 or 0 respectively. Instead of elementary
algebra where the values of the variables are numbers and the main operations are addition and
multiplication, the main operations of Boolean algebra are the conjunction (denoted ∧), the disjunction
(denoted ∨) and the negation (denoted ¬).

In this mission you should implement some boolean operations:
- "conjunction" denoted x ∧ y, satisfies x ∧ y = 1 if x = y = 1 and x ∧ y = 0 otherwise.
- "disjunction" denoted x ∨ y, satisfies x ∨ y = 0 if x = y = 0 and x ∨ y = 1 otherwise.
- "implication" (material implication) denoted x→y and can be described as ¬ x ∨ y. If x is true then
the value of x → y is taken to be that of y. But if x is false then the value of y can be ignored; however
the operation must return some truth value and there are only two choices, so the return value is the one
that entails less, namely true.
- "exclusive" (exclusive or) denoted x ⊕ y and can be described as (x ∨ y)∧ ¬ (x ∧ y). It excludes the
possibility of both x and y. Defined in terms of arithmetic it is addition mod 2 where 1 + 1 = 0.
- "equivalence" denoted x ≡ y and can be described as ¬ (x ⊕ y). It's true just when x and y have the same value.
Here you can see the truth table for these operations:

 x | y | x∧y | x∨y | x→y | x⊕y | x≡y |
--------------------------------------
 0 | 0 |  0  |  0  |  1  |  0  |  1  |
 1 | 0 |  0  |  1  |  0  |  1  |  0  |
 0 | 1 |  0  |  1  |  1  |  1  |  0  |
 1 | 1 |  1  |  1  |  1  |  0  |  1  |
--------------------------------------
You are given two boolean values x and y as 1 or 0 and you are given an operation name as described
earlier. You should calculate the value and return it as 1 or 0.

Input: Three arguments. X and Y as 0 or 1. An operation name as a string.

Output: The result as 1 or 0.

Example:
assert boolean(0, 0, "conjunction") == 0
assert boolean(0, 1, "conjunction") == 0
assert boolean(1, 0, "conjunction") == 0
assert boolean(1, 1, "conjunction") == 1

How it is used: Here you will learn how to work with boolean values and operators. You even get to
think about numbers as booleans.

Precondition: x in (0, 1)
y in (0, 1)
operation in ("conjunction", "disjunction", "implication", "exclusive", "equivalence")
----------
----------

En matemáticas y lógica matemática, el algebra booleana es una parte del algebra en la cual los valores
de las variables son verdadero o falso, comunmente denotados con 1 o 0 respectivamente. En vez del
algebra elemental dónde los valores de las variables son números y las operaciones principales son
adición y multiplicación, las operaciones principales del algebra booleana son la conjunción (denotado ∧),
la disyunción (denotado ∨) y la negación (denotado ¬).

En esta misión debes implementar algunas operaciones booleanas:
- "conjunction" (conjunción) denotado x ∧ y, satisface x ∧ y = 1 si x = y = 1 y x ∧ y = 0 si no.
- "disjunction" (disyunción) denotado x ∨ y, satisface x ∨ y = 0 si x = y = 0 y x ∨ y = 1 si no.
- "implication" (implicación material) denotado x→y y puede ser descrito como ¬ x ∨ y. Si x es
verdadera entonces el valor de x → y se toma como el de y. Pero si x es falso entonces el valor de
y puede ser ignorado; sin embargo la operación debe retornar algún valor de verdad t sólo hay dos opciones.
entonces el valor de retorno es el que implica menos, es decir, verdadera.
- "exclusive" (o exclusivo) denotado x ⊕ y y puede ser descrito como (x ∨ y)∧ ¬ (x ∧ y). Excluye la
posibilidad de ambos x y y. Definido en términos aritméticos es la adición módulo 2 dónde 1 + 1 = 0.
- "equivalence" (equivalencia) denotado x ≡ y y puede ser descrito como ¬ (x ⊕ y). Es verdadero sólo
cuándo x y y tienen el mismo valor.
Ésta es la taabla de verdad para esas operaciones:

 x | y | x∧y | x∨y | x→y | x⊕y | x≡y |
--------------------------------------
 0 | 0 |  0  |  0  |  1  |  0  |  1  |
 1 | 0 |  0  |  1  |  0  |  1  |  0  |
 0 | 1 |  0  |  1  |  1  |  1  |  0  |
 1 | 1 |  1  |  1  |  1  |  0  |  1  |
--------------------------------------
Se te dan dos valores booleanos x y y como 1 o 0 y se te da un nombre de operación como fue descrito
anteriormente. Debes calcular el valor y retornarlo como 1 o 0.

Entrada: Tres argumentos. X y Y como 0 o 1. Un nombre de operación como una cadena de carácteres.

Salida: El resultado 1 o 0.

Ejemplo:
assert boolean(0, 0, "conjunction") == 0
assert boolean(0, 1, "conjunction") == 0
assert boolean(1, 0, "conjunction") == 0
assert boolean(1, 1, "conjunction") == 1

Cómo se usa: Con esto comprenderás como trabajar con valores y operaciones booleanos. Incluso podrás
pensar en números cómo booleanos.

Precondición: x in (0, 1)
y in (0, 1)
operation in ("conjunction", "disjunction", "implication", "exclusive", "equivalence")
'''


OPERATION_NAMES = (
    "conjunction",
    "disjunction",
    "implication",
    "exclusive",
    "equivalence",
)


def boolean(x: bool, y: bool, operation: str) -> bool:
    if operation == "conjunction":
        return x and y
    elif operation == "disjunction":
        return x or y
    elif operation == "implication":
        return (not x) or y
    elif operation == "exclusive":
        return (x or y) and not (x and y)
    elif operation == "equivalence":
        return not (x or y) or (x and y)
    else:
        raise ValueError("Invalid operation")


print("Example:")
print(boolean(1, 0, "conjunction"))

assert boolean(0, 0, "conjunction") == 0
assert boolean(0, 1, "conjunction") == 0
assert boolean(1, 0, "conjunction") == 0
assert boolean(1, 1, "conjunction") == 1
assert boolean(0, 0, "disjunction") == 0
assert boolean(0, 1, "disjunction") == 1
assert boolean(1, 0, "disjunction") == 1
assert boolean(1, 1, "disjunction") == 1

print("The mission is done! Click 'Check Solution' to earn rewards!")
