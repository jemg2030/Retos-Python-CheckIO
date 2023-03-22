'''
The dust from the blast has shraded away and you entered the grounds of the estate. But what is that
piercing howl you’re hearing from afar? By taking a closer look you’ve realized that a small pack of
huge black shaggy dogs, looking more like wolves, are headed your way. These are probably the wild
offsprings of the guard dogs who’ve used to protect the castle from the unwanted visitors. The good
news is that you have a rifle. The bad news is that you don’t have a lot of bullets. Therefore, your
survival depends on finding the best vantage point for shooting. Choose your location wisely and try
to make each shot count.
As input you’ll be given the coords of the dogs. Your task is to find the distance to the nearest
point from which you can kill the maximum number of animals with one shot (any number of dogs on the
same line can be killed with one shot). Your starting position is the point (0, 0).

If the calculated distance is an integer, return it as int, otherwise round it to 2 decimal places.
Don't worry about the situation when a few dogs on the line is behind your back (dog dog you dog) -
there no such situation in the tests.

Input: list of coords (tuple of two integers/float) of the dogs.

Output: distance to the best spot.

Example:
wild_dogs([(7, 122), (8, 139), (9, 156),
           (10, 173), (11, 190), (-100, 1)]) == 0.18

How it is used: For the tactical analisys and troops placement.

Precondition :
2 <= amount of the dogs <= 15
0 <= distance to the right place <= 20

----------
----------

El polvo de la explosión se ha disipado y has entrado en los terrenos de la finca. Pero, ¿qué es
ese aullido desgarrador que oyes desde lejos? Al mirar más de cerca te has dado cuenta de que una
pequeña manada de enormes perros negros desgreñados, que más bien parecen lobos, se dirigen hacia
ti. Probablemente sean los descendientes salvajes de los perros guardianes que han protegido el
castillo de los visitantes indeseados. La buena noticia es que tienes un rifle. La mala noticia es
que no tienes muchas balas. Por lo tanto, tu supervivencia depende de encontrar el mejor punto de
observación para disparar. Elige bien tu ubicación e intenta que cada disparo cuente.
Como entrada se te darán las coordenadas de los perros. Tu tarea es encontrar la distancia al punto
más cercano desde el que puedas matar el máximo número de animales con un solo disparo (cualquier número
de perros en la misma línea puede ser matado con un solo disparo). Tu posición inicial es el punto (0, 0).

Si la distancia calculada es un número entero, devuélvelo como int, de lo contrario redondéalo a 2 decimales.
No se preocupe por la situación cuando algunos perros en la línea está detrás de su espalda (perro perro que
perro) - no hay tal situación en las pruebas.

Entrada: lista de coordenadas (tupla de dos enteros/float) de los perros.

Salida: distancia al mejor punto.

Ejemplo:
perros_salvajes([(7, 122), (8, 139), (9, 156),
           (10, 173), (11, 190), (-100, 1)]) == 0.18

Cómo se utiliza: Para el análisis táctico y la colocación de tropas.

Precondición :
2 <= cantidad de los perros <= 15
0 <= distancia al lugar correcto <= 20
'''


def wild_dogs(coords):
    # replace this for solution
    dist = mx = 0
    # Loop through all pairs of coordinates in the coords list using nested for loops.
    for p1 in coords:
        for p2 in coords:
            # Check if p1 and p2 are not the same point.
            if p1 != p2:
                # Calculate the coefficients of the line that passes through p1 and p2, represented by the
                # equation ax + by + c = 0. The a, b, and c coefficients are calculated using the x and y
                # coordinates of p1 and p2.
                a, b, c = p1[1] - p2[1], p2[0] - p1[0], p1[0] * p2[1] - p2[0] * p1[1]
                # Count the number of points in coords that lie on the line passing through p1 and p2. This
                # is done using a generator expression that iterates over coords and checks if each point
                # satisfies the equation of the line ax + by + c = 0.
                count = sum(1 for p in coords if a * p[0] + b * p[1] + c == 0)
                # Calculate the distance d between the line passing through p1 and p2 and the origin
                # (0, 0). This is done using the formula d = |c| / (a^2 + b^2)^0.5. The distance is
                # rounded to 2 decimal places using the round function.
                d = round(abs(c) / (a ** 2 + b ** 2) ** 0.5, 2)
                # Check if the number of points lying on the line passing through p1 and p2 is greater than
                # the maximum count mx, or if the count is equal to mx but the distance d is less than the
                # minimum distance dist. If either of these conditions is true, update mx and dist accordingly.
                if (count > mx) or (count == mx and d < dist):
                    mx = count
                    dist = d
    return dist


if __name__ == '__main__':
    print("Example:")
    print(wild_dogs([(7, 122), (8, 139), (9, 156),
                     (10, 173), (11, 190), (-100, 1)]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert wild_dogs([(7, 122), (8, 139), (9, 156),
                      (10, 173), (11, 190), (-100, 1)]) == 0.18

    assert wild_dogs([(6, -0.5), (3, -5), (1, -20)]) == 3.63

    assert wild_dogs([(10, 10), (13, 13), (21, 18)]) == 0

    print("Coding complete? Click 'Check' to earn cool rewards!")
