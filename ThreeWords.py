'''
Let's teach the Robots to distinguish words and numbers.

You are given a string with words and numbers separated by whitespaces (one space). The words contains only letters.
You should check if the string contains three words in succession. For example, the string "start 5 one two three 7
end" contains three words in succession.

Input: A string with words.

Output: The answer as a boolean.

Example:

assert checkio("Hello World hello") == True
assert checkio("He is 123 man") == False
assert checkio("1 2 3 4") == False
assert checkio("bla bla bla bla") == True

How it is used: This teaches you how to work with strings and introduces some useful functions.

Precondition: The input contains words and/or numbers. There are no mixed words (letters and digits combined).
0 < len(words) < 100

----------
----------

Enseñemosle a los Robots a distinguir entre palabras y números.

Se te da una cadena con palabras y números separados por espacios en blanco (un espacio). Las palabars contienen solo
letras. Deberías revisar si la cadena contiene tres palabras sucesivas. Por ejemplo, la cadena "start 5 one two three
7 end" contiene tres palabras en sucesión.

Entrada: Una cadena con palabras.

Salida: La respuesta como booleano.

Ejemplo:

assert checkio("Hello World hello") == True
assert checkio("He is 123 man") == False
assert checkio("1 2 3 4") == False
assert checkio("bla bla bla bla") == True
1
2
3
4
Cómo se usa: Esto te enseña como trabajar con cadenas e introduce algunas funciones útiles.

Precondición: La entrada contiene palabras y/o números. No hay palabras combinadas (letras y digitos combinados).
0 < len(words) < 100
'''


def checkio(text: str) -> bool:
    # add your code here
    words = text.split()
    count = 0
    for word in words:
        if word.isalpha():
            count += 1
            if count == 3:
                return True
        else:
            count = 0
    return False


print("Example:")
print(checkio("Hello World hello"))

# These "asserts" are used for self-checking
assert checkio("Hello World hello") == True
assert checkio("He is 123 man") == False
assert checkio("1 2 3 4") == False
assert checkio("bla bla bla bla") == True
assert checkio("Hi") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")