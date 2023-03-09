'''
You are at the beginning of a password series. Every mission is based on the previous one. The missions
that follow will become slightly more complex.

In this mission, you need to create a password verification function.

The verification condition is:

the length should be bigger than 6.

Input: A string.

Output: A bool.

Examples:
assert is_acceptable_password("short") == False
assert is_acceptable_password("muchlonger") == True
assert is_acceptable_password("ashort") == False

How it’s used: For a password verification form. Also it’s good to learn how the task can be evaluated.

----------
----------

Te encuentras al principio de una serie de contraseñas. Cada misión se basa en la anterior. Las misiones
siguientes serán algo más complejas.

En esta misión, tienes que crear una función de verificación de contraseña.

La condición de verificación es:

la longitud debe ser mayor que 6.

Entrada: Una cadena.

Salida: Un bool.

Ejemplo:
assert es_contraseña_aceptable("corta") == False
assert is_acceptable_password("muchlonger") == True
assert es_contraseña_aceptable("corta") == False

Cómo se usa: Para un formulario de verificación de contraseña. También es bueno aprender cómo se
puede evaluar la tarea.
'''


def is_acceptable_password(password: str) -> bool:
    # your code here
    return len(password) > 6


print("Example:")
print(is_acceptable_password("short"))

# These "asserts" are used for self-checking
assert is_acceptable_password("short") == False
assert is_acceptable_password("muchlonger") == True
assert is_acceptable_password("ashort") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
