'''
Before solving this mission, you can try to solve the "Brackets" mission.

Your task is to restore the balance of open and closed brackets by removing the unnecessary ones, while
trying to use the minimum number of deletions.

Only 3 types of brackets (), [] and {} can be used in the given string.

Only a parenthesis can close a parenthesis. That is, in this expression "(}" - the brackets aren’t balanced.
In an empty string, i.e., in a string that doesn’t contain any brackets - the brackets are balanced, but
removing all of the brackets isn’t considered to be an optimal solution.

If there are more than one correct answer, then you should choose the one where the character that can be
removed is closer to the beginning. For example, in this case "[(])", the correct answer will be "()",
since the removable brackets are closer to the beginning of the line.

Input: A string of characters () {} [].

Output: A string of characters () {} [].

Examples:

assert remove_brackets("(()()") == "()()"
assert remove_brackets("[][[[") == "[]"
assert remove_brackets("[[(}]]") == "[[]]"
assert remove_brackets("[[{}()]]") == "[[{}()]]"

----------
----------

Antes de resolver esta misión, puedes intentar resolver la misión "Paréntesis".

Tu tarea consiste en restablecer el equilibrio de corchetes abiertos y cerrados eliminando los innecesarios,
a la vez que intentas utilizar el mínimo número de eliminaciones.

Sólo se pueden utilizar 3 tipos de corchetes (), [] y {} en la cadena dada.

Sólo un paréntesis puede cerrar un paréntesis. Es decir, en esta expresión "(}" - los paréntesis no
están equilibrados. En una cadena vacía, es decir, en una cadena que no contiene ningún paréntesis,
los paréntesis están equilibrados, pero eliminar todos los paréntesis no se considera una solución óptima.

Si hay más de una respuesta correcta, debe elegir aquella en la que el carácter que se puede eliminar esté
más cerca del principio. Por ejemplo, en este caso "[(])", la respuesta correcta será "()", ya que los
corchetes eliminables están más cerca del principio de la línea.

Entrada: Una cadena de caracteres () {} [].

Salida: Una cadena de caracteres () {} [].

Ejemplo:

assert remove_brackets("(()()") == "()()"
assert remove_brackets("[][[") == "[]"
assert remove_brackets("[[(}]]") == "[[]]"
assert remove_brackets("[[{}()]]") == "[[{}()]]"
'''


import itertools


def is_balanced(bracket):
    while True:
        if '()' in bracket:
            bracket = bracket.replace('()', '')
        elif '[]' in bracket:
            bracket = bracket.replace('[]', '')
        elif '{}' in bracket:
            bracket = bracket.replace('{}', '')
        else:
            return not bracket
        

def remove_brackets(line: str) -> str:
    # your code here
    for i in range(len(line) + 1):
        for c in itertools.combinations(range(len(line)), i):
            bracket = ''.join(v for j, v in enumerate(line) if j not in c)
            if is_balanced(bracket):
                return bracket


print("Example:")
print(remove_brackets("(()()"))

# These "asserts" are used for self-checking
assert remove_brackets("(()()") == "()()"
assert remove_brackets("[][[[") == "[]"
assert remove_brackets("[[(}]]") == "[[]]"
assert remove_brackets("[[{}()]]") == "[[{}()]]"
assert remove_brackets("[[[[[[") == ""
assert remove_brackets("[[[[}") == ""
assert remove_brackets("") == ""
assert remove_brackets("[(])") == "()"

print("The mission is done! Click 'Check Solution' to earn rewards!")
