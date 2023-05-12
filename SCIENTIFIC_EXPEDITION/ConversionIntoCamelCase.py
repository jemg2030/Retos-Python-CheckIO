'''
Your mission is to convert the name of a function (a string) from the Python format (for example
"my_function_name") into CamelCase ("MyFunctionName"), where the first char of every word is in
uppercase and all words are concatenated without any intervening characters.

Input: A function name as a string.

Output: The same string, but in CamelCase.

Example:
assert to_camel_case("my_function_name") == "MyFunctionName"
assert to_camel_case("i_phone") == "IPhone"

How it is used: To apply function names in the style in which they are adopted in a specific
language (Python, JavaScript, etc.).

Precondition:
0 < len(string) <= 100
Input data won't contain any numbers.

----------
----------

Tu misión es convertir el nombre de una función (una cadena) del formato Python (por ejemplo
"mi_nombre_funcion") a CamelCase ("MiNombreFuncion"), donde el primer carácter de cada palabra
está en mayúscula y todas las palabras están concatenadas sin caracteres intermedios.

Entrada: Un nombre de función como cadena.

Salida: La misma cadena, pero en CamelCase.

Ejemplo:
assert to_camel_case("mi_nombre_funcion") == "MiNombre_funcion"
assert to_camel_case("i_phone") == "IPhone"

Cómo se utiliza: Para aplicar nombres de función en el estilo en que se adoptan en un lenguaje
específico (Python, JavaScript, etc.).

Precondición:
0 < len(cadena) <= 100
Los datos de entrada no contendrán ningún número.
'''


def to_camel_case(name: str) -> str:
    # replace this for solution
    words = name.split('_')
    camel_case_words = [word.capitalize() for word in words]
    return ''.join(camel_case_words)


print("Example:")
print(to_camel_case("my_function_name"))

# These "asserts" are used for self-checking
assert to_camel_case("my_function_name") == "MyFunctionName"
assert to_camel_case("i_phone") == "IPhone"

print("The mission is done! Click 'Check Solution' to earn rewards!")
