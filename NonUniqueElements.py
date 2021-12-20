'''

If you have 50 different plug types, appliances wouldn't be available and would be very expensive. But once an electric
outlet becomes standardized, many companies can design appliances, and competition ensues, creating variety and better
prices for consumers.
-- Bill Gates

You are given a non-empty list of integers (X). For this task, you should return a list consisting of only the
non-unique elements in this list. To do so you will need to remove all unique elements (elements which are contained
in a given list only once). When solving this task, do not change the order of the list. Example: [1, 2, 3, 1, 3] 1
and 3 non-unique elements and result will be [1, 3, 1, 3].

non-unique-elements

Input: A list of integers.

Output: An iterable of integers.

Example:
1 checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3]
2 checkio([1, 2, 3, 4, 5]) == []
3 checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
4 checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9]
5 checkio([2]) == []

How it is used: This mission will help you to understand how to manipulate arrays, something that is the basis for
solving more complex tasks. The concept can be easily generalized for real world tasks. For example: if you need to
clarify statistics by removing low frequency elements (noise).

----------
----------
Se te dará una lista no vacía de enteros (X). Para esta misión, deberás retornar una lista que consista únicamente de
elementos no únicos. Para hacerlo, necesitarás eliminar todos los elementos que sean únicos (elementos que aparezcan
una sola vez en la lista dada). Al resolver esta misión, no cambies el orden de la lista. Ejemplo: [1, 2, 3, 1, 3] 1 y
3 no son elementos únicos y el resultado será [1, 3, 1, 3].

non-unique-elements

Entrada: Una lista de enteros.

Salida: An iterable of integers.

Ejemplo:
1 checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3]
2 checkio([1, 2, 3, 4, 5]) == []
3 checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
4 checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9]

¿Cómo es usado?: Esta misión te ayudará a entender cómo manipular vectores (arrays), que es la base para resolver
tareas más complejas. El concepto puede ser fácilmente generalizado para tareas en el mundo real. Por ejemplo: si
necesitas esclarecer estadísticas removiendo elementos de baja frecuencia (ruido).

Pre-condición:
0 < |X| < 1000

'''


# Your optional code here
# You can import some modules or create additional functions


def checkio(data):
    # Your code here
    # It's main function. Don't remove this function
    # It's used for auto-testing and must return a result for check.

    size = len(data)
    copyData = []

    if ((size > 0) and (size <= 1000)):
        for i in range(size):
            element = data[i]
            repeated = data.count(element)
            if (repeated == 1):
                copyData.append(data[i])

        size1 = len(copyData)

        for i in range(size1):
            valueDel = copyData[i]
            position = data.index(valueDel)
            data.pop(position)
    else:
        print("The size of the array does not meet the conditions")

    # replace this for solution
    return data


# Some hints
# You can use list.count(element) method for counting.
# Create new list with non-unique elements
# Loop over original list


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")