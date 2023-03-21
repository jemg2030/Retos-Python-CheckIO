'''
Finding the castle with a map and a compass was a piece of cake. Moreover, when you’ve inspected the
surroundings through the spyglass, you spotted a small sailing yacht a few kilometers from the place
where you were washed ashore. It has probably belonged to other treasure hunters who have failed to
leave the island. After checking it out you’ve came to a conclusion that yacht is in a pretty good
shape and with the fair-wind you’ll have no problems returning home. Well, in any case, you’ll have
less problems - now you just have to find the Cube.

As I’ve said before, the lord who used to live here, highly appreciated the solitude, therefore it’s
not surprising that the estate was surrounded by a very high and thick stone wall. Fortunately, you’ve
foreseen this and took some explosives with you (I don’t even want to know where you got it from). However,
it’s unlikely that this modest reserve will suffice to blow up the wall just anywhere - it’d be better to
act for sure and find the most vulnerable place.
As input you'll get a multiline string consists of '0' and '#' - a view of a stone wall from above. The '#'
will show the stone part of the wall and the '0' will show the empty part. The relative location of you and
the wall is as follows: you look at the array from the bottom of it.
Your task is to find the index of the place where the wall is the narrowest (as shown at the picture below).
The width of the wall is the height of the columns of the array (multiline string). If there are several such
places, return the index of leftmost. Index starts from 0.

Input: Array represents the stone wall.

Output: Index of leftmost of all weakest spots.

Example:

stone_wall('''
##########
####0##0##
00##0###00
''') == 4

How it is used: For the architecture analisys.

Precondition :
3x3 <= array size <= 10x10

----------
----------

Encontrar el castillo con un mapa y una brújula fue pan comido. Además, cuando has inspeccionado los 
alrededores con el catalejo, has avistado un pequeño velero a pocos kilómetros del lugar donde te 
arrastró la corriente. Probablemente ha pertenecido a otros buscadores de tesoros que no han conseguido 
salir de la isla. Después de registrarlo has llegado a la conclusión de que el velero está en bastante 
buen estado y con el viento a favor no tendrás problemas para volver a casa. En cualquier caso, tendrás 
menos problemas: ahora sólo tienes que encontrar el Cubo.

Como he dicho antes, el señor que vivía aquí apreciaba mucho la soledad, por lo que no es de extrañar que 
la finca estuviera rodeada por un muro de piedra muy alto y grueso. Afortunadamente, lo ha previsto y se 
ha llevado explosivos (no quiero ni saber de dónde los ha sacado). Sin embargo, es poco probable que esta 
modesta reserva baste para volar el muro en cualquier sitio: sería mejor actuar con seguridad y encontrar 
el lugar más vulnerable.
Como entrada obtendrás una cadena multilínea formada por '0' y '#': una vista de un muro de piedra desde 
arriba. El '#' mostrará la parte de piedra del muro y el '0' mostrará la parte vacía. Tu posición relativa 
y la de la pared es la siguiente: miras la matriz desde la parte inferior de la misma.
Tu tarea es encontrar el índice del lugar donde la pared es más estrecha (como se muestra en la imagen de 
abajo). La anchura del muro es la altura de las columnas de la matriz (cadena multilínea). Si hay varios 
lugares así, devuelve el índice del más a la izquierda. El índice empieza en 0.

Entrada: Array representa el muro de piedra.

Salida: Índice del punto más a la izquierda de todos los puntos más débiles.

Ejemplo:
muro_de_piedra('''
##########
####0##0##
00##0###00
''') == 4

Cómo se utiliza: Para el análisis de la arquitectura.

Precondición :
3x3 <= tamaño del array <= 10x10
'''


def stone_wall(wall):
    #replace this for solution
    # Split the input string into a list of rows
    rows = wall.strip().split('\n')

    # Calculate the sum of each column in the wall
    col_sums = [sum(1 for row in rows if row[i] == '#') for i in range(len(rows[0]))]

    # Find the index of the minimum sum
    min_sum_index = col_sums.index(min(col_sums))

    return min_sum_index

if __name__ == '__main__':
    print("Example:")
    print(stone_wall('''
##########
####0##0##
00##0###00
'''))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert stone_wall('''
##########
####0##0##
00##0###00
''') == 4

    assert stone_wall('''
#00#######
#######0##
00######00
''') == 1

    assert stone_wall('''
#####
#####
#####
''') == 0

    print("Coding complete? Click 'Check' to earn cool rewards!")
