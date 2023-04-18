'''
The solid door slowly opened after the painted key was accepted and ... Here it is - the Main Warehouse!
You’ve come a long and hard way to get here. There is very little left and the artifact will be yours.

The pedestal upon which stood the Hypercube didn’t fit into the castle’s interiors. It was a high-tech column
above which hovered the Cube in a cylinder of bluish light without any visible support. Most likely, the
cylinder is a force field, which has to be turned off in order to take the Cube.
"Did Lord Escher actually die? What if he just went back to his home planet?", - the thought has involuntarily
entered your mind. But there was no time for reflection. You can’t rule out the possibility of the owner’s ghost
trying to stop you on your way back, so you have got to hurry.

When you took a few steps closer to the Cube and were getting ready to reach out, you suddenly felt like you’ve
bumped into something invisible, yet impenetrable. Was the Hypercube surrounded by another force field?!
Well, you have to find a way to turn it off.
When you’ve touched an outer invisible force field, a rectangle consisting of letters appeared on it. While
you were looking at these letters, their set had changed. It seems that every 10 seconds the letter box
automatically reboots. You need to wait for the moment when you can clearly read 'Hypercube' on the field -
this will be the short window during which the field is deactivated and you can pass.
Your function receives an array of letters as an argument. Your task is to return True if it’s possible
to read the word 'Hypercube' in this array, and False if otherwise. The 'Hypercube' is in the array only
if the word "hypercube" can be read/compiled from an unbroken letter line. In addition, the line can bend
at a 90-degree angle, but can’t go diagonally. It’s completely case insensitive.

Input: Array of the letters.

Output: True or False.

Example:
hypercube([
              ['g', 'f', 'H', 'Y', 'v'],
              ['z', 'e', 'a', 'P', 'u'],
              ['s', 'B', 'T', 'e', 'y'],
              ['k', 'u', 'c', 'R', 't'],
              ['l', 'O', 'k', 'p', 'r']]) == True
hypercube([
              ['H', 'a', 't', 's', 'E'],
              ['a', 'Y', 'p', 'u', 'B'],
              ['a', 'a', 'P', 'y', 'U'],
              ['x', 'x', 'x', 'E', 'C'],
              ['z', 'z', 'z', 'z', 'R']]) == False

How it is used: For the lexicographic analisys.

Precondition :
3x3 <= array size <= 5x5

----------
----------

La sólida puerta se abrió lentamente después de aceptar la llave pintada y ... Aquí está: ¡el Almacén
Principal! Has recorrido un largo y duro camino para llegar hasta aquí. Queda muy poco y el artefacto
estará en tus manos.

El pedestal sobre el que se alzaba el Hipercubo no encajaba en los interiores del castillo. Era una columna de
alta tecnología sobre la que flotaba el Cubo en un cilindro de luz azulada sin ningún soporte visible. Lo más
probable es que el cilindro sea un campo de fuerza, que hay que desactivar para poder coger el Cubo.
"¿Murió realmente Lord Escher? ¿Y si simplemente volvió a su planeta natal?", - el pensamiento ha entrado
involuntariamente en tu mente. Pero no había tiempo para reflexionar. No puedes descartar la posibilidad
de que el fantasma del propietario intente detenerte en tu camino de vuelta, así que tienes que darte prisa.

Cuando diste unos pasos más cerca del Cubo y te disponías a extender la mano, de repente sentiste que te
habías topado con algo invisible, pero impenetrable. ¡¿Estaba el Hipercubo rodeado por otro campo de fuerza?!
Pues tienes que encontrar la forma de desactivarlo.
Cuando has tocado un campo de fuerza invisible exterior, ha aparecido en él un rectángulo formado por letras.
Mientras mirabas estas letras, su conjunto había cambiado. Parece que cada 10 segundos el buzón se reinicia
automáticamente. Tienes que esperar al momento en que puedas leer claramente "Hipercubo" en el campo - esta
será la breve ventana durante la cual el campo se desactiva y puedes pasar.
Tu función recibe un array de letras como argumento. Tu tarea es devolver True si es posible leer la palabra
'Hipercubo' en esta matriz, y False en caso contrario. El 'Hipercubo' está en el array sólo si la palabra
"hipercubo" puede ser leída/compilada desde una línea de letras ininterrumpida. Además, la línea puede doblarse
en un ángulo de 90 grados, pero no puede ir en diagonal. No distingue entre mayúsculas y minúsculas.

Entrada: Array de las letras.

Salida: Verdadero o Falso.

Ejemplo:
hipercubo([
              ['g', 'f', 'H', 'Y', 'v'],
              ['z', 'e', 'a', 'P', 'u'],
              ['s', 'B', 'T', 'e', 'y'],
              ['k', 'u', 'c', 'R', 't'],
              ['l', 'O', 'k', 'p', 'r']]) == True
hipercubo([
              ['H', 'a', 't', 's', 'E'],
              ['a', 'Y', 'p', 'u', 'B'],
              ['a', 'a', 'P', 'y', 'U'],
              ['x', 'x', 'x', 'E', 'C'],
              ['z', 'z', 'z', 'z', 'R']]) == False

Cómo se utiliza: Para el análisis lexicográfico.

Precondición :
3x3 <= tamaño de la matriz <= 5x5

Traducción realizada con la versión gratuita del traductor www.DeepL.com/Translator
'''


def hypercube(grid):
    #replace this for solution
    word = "hypercube"
    rows = len(grid)
    cols = len(grid[0])

    # Define a helper function to check if a given coordinate is within the bounds of the grid
    def in_bounds(row, col):
        return 0 <= row < rows and 0 <= col < cols

    # Define a helper function to perform depth-first search from a given starting coordinate
    def dfs(row, col, i):
        if i == len(word):
            return True
        if not in_bounds(row, col) or grid[row][col].lower() != word[i]:
            return False
        temp = grid[row][col]
        grid[row][col] = "#"  # Mark the current cell as visited
        result = any(dfs(row + dr, col + dc, i + 1) for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)))
        grid[row][col] = temp  # Restore the cell value
        return result

    # Perform depth-first search from each cell in the grid
    return any(dfs(row, col, 0) for row in range(rows) for col in range(cols))


if __name__ == '__main__':
    print("Example:")
    print(hypercube([
              ['g', 'f', 'H', 'Y', 'v'],
              ['z', 'e', 'a', 'P', 'u'],
              ['s', 'B', 'T', 'e', 'y'],
              ['k', 'u', 'c', 'R', 't'],
              ['l', 'O', 'k', 'p', 'r']]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert hypercube([
              ['g', 'f', 'H', 'Y', 'v'],
              ['z', 'e', 'a', 'P', 'u'],
              ['s', 'B', 'T', 'e', 'y'],
              ['k', 'u', 'c', 'R', 't'],
              ['l', 'O', 'k', 'p', 'r']]) == True
    assert hypercube([
              ['H', 'a', 't', 's', 'E'],
              ['a', 'Y', 'p', 'u', 'B'],
              ['a', 'a', 'P', 'y', 'U'],
              ['x', 'x', 'x', 'E', 'C'],
              ['z', 'z', 'z', 'z', 'R']]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
