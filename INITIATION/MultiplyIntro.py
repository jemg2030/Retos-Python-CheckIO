'''
This is an intro mission, the purpose of which is to explain how to solve missions on CheckiO. If you want to
know how to get the maximum out of using CheckiO, check out our blog post "From Basic to Advance usage".

This mission is the easiest one. Write a function that will receive 2 numbers as input and it should return the
multiplication of these 2 numbers.

Input: Two arguments. Both are of type int.

Output: Int.

Examples:
assert mult_two(3, 2) == 6
assert mult_two(0, 1) == 0

A series of hints below will help you to understand how to solve the mission. Start the series by clicking on
"I don’t know how to solve that mission."

---------
---------

Esta es una misión de introducción, cuyo objetivo es explicar cómo resolver misiones en CheckiO. Si quieres
saber cómo sacarle el máximo partido a CheckiO, registra la entrada de nuestro blog "Del uso básico al avanzado".

Esta misión es la más fácil. Escribe una función que reciba 2 números como entrada y que devuelva la
multiplicación de estos 2 números.

Entrada: Dos argumentos. Ambos son de tipo int.

Salida: Int.

Ejemplo:
assert mult_two(3, 2) == 6
assert mult_two(0, 1) == 0

A continuación encontrarás una serie de pistas que te ayudarán a entender cómo resolver la misión. Inicia
la serie haciendo clic en "No sé cómo resolver esa misión".
'''


def mult_two(a: int, b: int) -> int:
    # your code here
    # multiply a and b and store the result in a variable
    result = a * b

    # return the result
    return result


print("Example")
print(mult_two(1, 2))

assert mult_two(3, 2) == 6
assert mult_two(0, 1) == 0

print("The first mission is done! Click 'Check' to earn cool rewards!")
