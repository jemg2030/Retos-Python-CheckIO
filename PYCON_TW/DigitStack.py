"""
In computer science, a stack is a particular kind of data type or collection in which
the principal operations in the collection are the addition of an entity to the collection
(also known as push) and the removal of an entity (also known as pop). The relation between
the push and pop operations is such that the stack is a Last-In-First-Out (LIFO) data structure.
In a LIFO data structure, the last element added to the structure must be the first one to be
removed. Often a peek, or top operation is also implemented, returning the value of the top
element without removing it.

We will emulate the stack process with Python. You are given a sequence of commands:
- "PUSH X" -- add X in the stack, where X is a digit.
- "POP" -- look and remove the top position. If the stack is empty, then it returns 0 (zero)
and does nothing.
- "PEEK" -- look at the top position. If the stack is empty, then it returns 0 (zero).
The stack can only contain digits.

You should process all commands and sum all digits which were taken from the stack ("PEEK" or "POP").
Initial value of the sum is 0 (zero).

Let's look at an example, here's the sequence of commands:
["PUSH 3", "POP", "POP", "PUSH 4", "PEEK", "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]

Command	Stack	Sum
PUSH 3	3	0
POP		0+3
POP		3+0
PUSH 4	4	3
PEEK	4	3+4
PUSH 9	4,9	7
PUSH 0	4,9,0	7
PEEK	4,9,0	7+0
POP	4,9	7+0
PUSH 1	4,9,1	7
PEEK	4,9,1	7+1= 8
Input: A sequence of commands as a list of strings.

Output: The sum of the taken digits as an integer.

Example:
digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK", "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]) == 8
digit_stack(["POP", "POP"]) == 0
digit_stack(["PUSH 9", "PUSH 9", "POP"]) == 9
digit_stack([]) == 0

How it is used: Stacks have numerous applications. We see stacks in everyday life, from the
books in our library, to the blank sheets of paper in our printer tray. All of them follow
the Last In First Out (LIFO) logic, that is when we add a book to a pile of books, we add it
to the top of the pile, whereas when we remove a book from the pile, we generally remove it
from the top of the pile.

Precondition:
0 ≤ len( commands ) ≤ 20;
all(re.match("\APUSH \d\Z", c) or с == "POP" or c == "PEEK" for c in commands )

----------
----------

En informática, una pila es una clase particular de tipo de datos o colección en la que
las operaciones principales en la colección son la adición de una entidad a la colección
(también conocida como push) y la eliminación de una entidad (también conocida como pop).
La relación entre las operaciones push y pop es tal que la pila es una estructura de datos
LIFO (Last-In-First-Out). En una estructura de datos LIFO, el último elemento añadido a la
estructura debe ser el primero en ser eliminado. A menudo también se implementa una operación
peek, o top, que devuelve el valor del elemento superior sin eliminarlo.

Emularemos el proceso de pila con Python. Se le da una secuencia de comandos:
- "PUSH X" -- añade X en la pila, donde X es un dígito.
- "POP" -- busca y elimina la posición superior. Si la pila está vacía, entonces devuelve 0
(cero) y no hace nada.
- "PEEK" -- mira la posición superior. Si la pila está vacía, entonces devuelve 0 (cero).
La pila sólo puede contener dígitos.

Debe procesar todos los comandos y sumar todos los dígitos que se tomaron de la pila ("PEEK" o "POP").
El valor inicial de la suma es 0 (cero).

Veamos un ejemplo, esta es la secuencia de comandos:
["PUSH 3", "POP", "POP", "PUSH 4", "PEEK", "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]

Comando Pila Suma
PUSH 3 3 0
POP 0+3
POP 3+0
PUSH 4 4 3
PEEK 4 3+4
PUSH 9 4,9 7
PUSH 0 4,9,0 7
PEEK 4,9,0 7+0
POP 4,9 7+0
PUSH 1 4,9,1 7
PEEK 4,9,1 7+1= 8
Entrada: Una secuencia de comandos como una lista de cadenas.

Salida: La suma de los dígitos tomados como un entero.

Ejemplo:

digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK", "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]) == 8
digit_stack(["POP", "POP"]) == 0
digit_stack(["PUSH 9", "PUSH 9", "POP"]) == 9
digit_stack([]) == 0

Cómo se utiliza: Las pilas tienen numerosas aplicaciones. Vemos pilas en la vida cotidiana,
desde los libros de nuestra biblioteca hasta las hojas de papel en blanco de la bandeja de
nuestra impresora. Todos ellos siguen la lógica de último en entrar, primero en salir (LIFO),
es decir, cuando añadimos un libro a una pila de libros, lo añadimos a la parte superior de la
pila, mientras que cuando retiramos un libro de la pila, generalmente lo retiramos de la parte
superior de la pila.

Precondición:
0 ≤ len( comandos ) ≤ 20;
all(re.match("\APUSH \d\Z", c) or с == "POP" or c == "PEEK" for c in comandos )
"""


def digit_stack(commands):
    stack = []
    result: int = 0
    for command in commands:
        if command.startswith("PUSH"):
            stack.append(int(command.split()[1]))
        elif stack:
            result += stack.pop() if command == "POP" else stack[-1]
    return result


if __name__ == "__main__":
    print("Example:")
    print(
        digit_stack(
            [
                "PUSH 3",
                "POP",
                "POP",
                "PUSH 4",
                "PEEK",
                "PUSH 9",
                "PUSH 0",
                "PEEK",
                "POP",
                "PUSH 1",
                "PEEK",
            ]
        )
    )

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert (
        digit_stack(
            [
                "PUSH 3",
                "POP",
                "POP",
                "PUSH 4",
                "PEEK",
                "PUSH 9",
                "PUSH 0",
                "PEEK",
                "POP",
                "PUSH 1",
                "PEEK",
            ]
        )
        == 8
    ), "Example"
    assert digit_stack(["POP", "POP"]) == 0, "pop, pop, zero"
    assert digit_stack(["PUSH 9", "PUSH 9", "POP"]) == 9, "Push the button"
    assert digit_stack([]) == 0, "Nothing"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
