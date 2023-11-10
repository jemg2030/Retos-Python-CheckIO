"""
This task is adapted from following video with Neil Sloane (founder of the On-Line
Encyclopedia of Integer Sequences). There are a few interesting sequences are shown in
the video (so I recommend you to watch it all), but this particular mission is dedicated
to the very first one - toothpicks sequence.

So, you have an infinite number of toothpicks of equal length and put them down on the table
according to the rule. On the first step you just put one toothpick. It has two free ends,
on which on the second step you respectively put two toothpicks perpendicularly. Now you
have four free ends and put the next four toothpicks on the step three. If two toothpicks
ends touch each other, the are not free, so after step three you again have four free end
and so on.

The playground of this and other patterns may be seen on the page. It will be easier to
solve the task and it's just a beautiful hypnotic view!)

So, your function must return the number of toothpicks, placed on the table, after step steps.

Input: Number of steps as integer.

Output: Number of toothpicks as integer.

Examples:
assert toothpicks(1) == 1
assert toothpicks(2) == 3
assert toothpicks(3) == 7
assert toothpicks(4) == 11

----------
----------

Esta tarea es una adaptación del siguiente vídeo con Neil Sloane (fundador de la
Enciclopedia en línea de secuencias de números enteros). En el vídeo se muestran algunas
secuencias interesantes (así que te recomiendo que lo veas todo), pero esta misión en
particular está dedicada a la primera de ellas: la secuencia de los palillos.

Así que tienes un número infinito de palillos de la misma longitud y los pones sobre la
mesa de acuerdo con la regla. En el primer paso que acaba de poner un palillo de dientes.
Tiene dos extremos libres, en los que en el segundo paso pones respectivamente dos palillos
perpendicularmente. Ahora usted tiene cuatro extremos libres y poner los próximos cuatro
palillos de dientes en el paso tres. Si dos palillos extremos se tocan entre sí, el no son
libres, por lo que después de que el paso tres que de nuevo tienen cuatro extremos libres y
así sucesivamente.

El campo de juego de este y otros patrones se puede ver en la página. Será más fácil resolver
la tarea y es una vista hipnótica preciosa).

Por lo tanto, su función debe devolver el número de palillos de dientes, colocados sobre la mesa,
después de los pasos de paso.

Entrada: Número de pasos como entero.

Salida: Número de palillos como entero.

Ejemplos:
assert palillos(1) == 1
assert palillos(2) == 3
assert palillos(3) == 7
assert palillos(4) == 11
"""


def toothpicks(step: int) -> int:
    # your code here
    result, edges, points, switch = 1, {(1, 0), (-1, 0)}, {(0, 0)}, False

    while step > 1:
        points |= edges
        new_edges, discard_edges = set(), set()

        for px, py in edges:
            for q in [
                (px + switch, py + (not switch)),
                (px - switch, py - (not switch)),
            ]:
                if q in points:
                    pass
                elif q in new_edges:
                    discard_edges.add(q)
                else:
                    new_edges.add(q)

        new_edges -= discard_edges

        step -= 1
        result += len(edges)
        edges = new_edges
        points |= discard_edges
        switch = not switch

    return result


print("Example:")
print(toothpicks(2))

# These "asserts" are used for self-checking
assert toothpicks(1) == 1
assert toothpicks(2) == 3
assert toothpicks(3) == 7
assert toothpicks(4) == 11
assert toothpicks(5) == 15

print("The mission is done! Click 'Check Solution' to earn rewards!")
