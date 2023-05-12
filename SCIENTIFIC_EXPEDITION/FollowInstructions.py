'''
You’ve received a letter from a friend whom you haven't seen or heard from for a while. In this
letter he gives you instructions on how to find a hidden treasure!

In this mission you should follow a given list of instructions which will get you to a certain
point on the map. A list of instructions is a string, each letter of this string points you in
the direction of your next step.

The letter "f" - tells you to move forward, "b" - backward, "l" - left, and "r" - right.

It means that if the list of your instructions is "fflff" then you should move forward two times,
make one step to the left and then again move two times forward.

Now, let's imagine that you are in the position (0, 0). If you move forward your position will change
to (0, 1). If you move again it will be (0, 2). If your next step is to the left then your position
will become (-1, 2). After the next two steps forward your coordinates will be (-1, 4).

Your goal is to find your final coordinates. Like in our case they are (-1, 4).

Input: A string.

Output: A tuple or list of two integers.

Examples:
assert list(follow("fflff")) == [-1, 4]
assert list(follow("ffrff")) == [1, 4]
assert list(follow("fblr")) == [0, 0]

How it is used: in games with a map.

Precondition: only chars f, b, l and r are allowed.

----------
----------

Has recibido una carta de un amigo al que hace tiempo que no ves ni sabes nada de él. En esta
carta te da instrucciones para encontrar un tesoro escondido.

En esta misión deberás seguir una lista de instrucciones que te llevarán a un punto determinado
del mapa. Una lista de instrucciones es una cadena, cada letra de esta cadena te señala la dirección
de tu siguiente paso.

La letra "f" le indica que debe avanzar, la "b" que debe retroceder, la "l" que debe ir a la izquierda
y la "r" que debe ir a la derecha.

Significa que si la lista de tus instrucciones es "fflff", entonces debes avanzar dos veces, dar un
paso a la izquierda y volver a avanzar dos veces.

Ahora, imaginemos que estás en la posición (0, 0). Si te mueves hacia delante, tu posición estará en
(0, 1). Si vuelves a moverte, estará en (0, 2). Si das otro paso hacia la izquierda, tu posición estará en
(-1, 2). Después de los dos siguientes pasos hacia delante tus coordenadas estarán en (-1, 4).

Tu objetivo es encontrar tus coordenadas finales. Como en nuestro caso son (-1, 4).

Entrada: Una cadena.

Salida: Una tupla o lista de dos enteros.

Ejemplos:
assert list(follow("fflff")) == [-1, 4]
assert list(follow("ffrff")) == [1, 4]
assert list(follow("fblr")) == [0, 0]

Cómo se usa: en juegos con mapa.

Precondición: sólo se permiten los caracteres f, b, l y r.
'''


def follow(instructions: str) -> tuple[int, int] | list[int]:
    # your code here
    x, y = 0, 0  # Initial coordinates
    for instruction in instructions:
        if instruction == "f":
            y += 1
        elif instruction == "b":
            y -= 1
        elif instruction == "l":
            x -= 1
        elif instruction == "r":
            x += 1
    return [x, y]


print("Example:")
print(list(follow("fflff")))

# These "asserts" are used for self-checking
assert list(follow("fflff")) == [-1, 4]
assert list(follow("ffrff")) == [1, 4]
assert list(follow("fblr")) == [0, 0]

print("The mission is done! Click 'Check Solution' to earn rewards!")
