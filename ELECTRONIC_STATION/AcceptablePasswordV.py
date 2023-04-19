'''
In this mission you need to create a password verification function.

The verification conditions are:

the length should be bigger than 6;
should contain at least one digit, but it cannot consist of just digits;
having numbers or containing just numbers does not apply to the password longer than 9;
a string should not contain the word "password" in any case.
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
tener números o contener sólo números no se aplica a la contraseña de longitud superior a 9;
la cadena no debe contener la palabra "contraseña" en ningún caso.
Entrada: Una cadena.

Salida: Un bool.

Ejemplos:
assert es_contraseña_aceptable("corta") == False
assert es_contraseña_aceptable("corta54") == True
assert is_acceptable_password("muchlonger") == True
assert is_acceptable_password("ashort") == False

Cómo se usa: Para el formulario de verificación de contraseñas. También es bueno aprender cómo se
puede evaluar la tarea.
'''


# Taken from mission Acceptable Password IV

# Taken from mission Acceptable Password III
# Taken from mission Acceptable Password II
# Taken from mission Acceptable Password I
def is_acceptable_password(password: str) -> bool:
    # your code here
    if len(password) <= 6 or "password" in password.lower():
        return False
    if len(password) > 9:
        return True
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
    if not has_digit or password.isdigit():
        return False
    return True


print("Example:")
print(is_acceptable_password("short"))

# These "asserts" are used for self-checking
assert is_acceptable_password("short") == False
assert is_acceptable_password("short54") == True
assert is_acceptable_password("muchlonger") == True
assert is_acceptable_password("ashort") == False
assert is_acceptable_password("muchlonger5") == True
assert is_acceptable_password("sh5") == False
assert is_acceptable_password("1234567") == False
assert is_acceptable_password("12345678910") == True
assert is_acceptable_password("password12345") == False
assert is_acceptable_password("PASSWORD12345") == False
assert is_acceptable_password("pass1234word") == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
