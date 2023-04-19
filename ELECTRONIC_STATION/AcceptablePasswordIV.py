'''
In this mission you need to create a password verification function.

The verification conditions are:

the length should be bigger than 6;
should contain at least one digit, but it cannot consist of just digits;
if the password is longer than 9 - previous rule (about one digit), is not required.
Input: A string.

Output: A bool.

Examples:
assert is_acceptable_password("short") == False
assert is_acceptable_password("short54") == True
assert is_acceptable_password("muchlonger") == True
assert is_acceptable_password("ashort") == False

How it’s used: For password verification form. Also it's good to learn how the task can be evaluated.

----------
----------

En esta misión debe crear una función de verificación de contraseña.

Las condiciones de verificación son:

la longitud debe ser superior a 6
debe contener al menos un dígito, pero no puede consistir sólo en dígitos;
si la contraseña es superior a 9 - regla anterior (sobre un dígito), no es necesario.
Entrada: Una cadena.

Salida: Un bool.

Ejemplos:
assert es_contraseña_aceptable("corta") == False
assert es_contraseña_aceptable("corta54") == True
assert is_acceptable_password("muchlonger") == True
assert is_acceptable_password("ashort") == False

Cómo se usa: Para el formulario de verificación de contraseñas. También es bueno aprender cómo se puede
evaluar la tarea.

Traducción realizada con la versión gratuita del traductor www.DeepL.com/Translator
'''


# Taken from mission Acceptable Password III

# Taken from mission Acceptable Password II
# Taken from mission Acceptable Password I
def is_acceptable_password(password: str) -> bool:
    # your code here
    if len(password) > 9:
        return True
    if len(password) > 6 and not password.isdigit():
        return any(char.isdigit() for char in password)
    return False


print("Example:")
print(is_acceptable_password("short"))

# These "asserts" are used for self-checking
assert is_acceptable_password("short") == False
assert is_acceptable_password("short54") == True
assert is_acceptable_password("muchlonger") == True
assert is_acceptable_password("ashort") == False
assert is_acceptable_password("notshort") == False
assert is_acceptable_password("muchlonger5") == True
assert is_acceptable_password("sh5") == False
assert is_acceptable_password("1234567") == False
assert is_acceptable_password("12345678910") == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
