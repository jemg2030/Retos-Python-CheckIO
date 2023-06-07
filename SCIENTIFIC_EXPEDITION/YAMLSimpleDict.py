'''
Have you ever heard of such markup language as YAML? It’s a friendly data serialization format.
In fact it’s so friendly that both people and programs can read it quite well. You can play
around with the standard by following this link.

YAML is a text, and you need to convert it into an object. But I’m not asking you to implement
the entire YAML standard, we’ll implement it step by step.

The first step is the key-value conversion. The key can be any string consisting of Latin
letters and numbers. The value can be a single-line string (which consists of spaces, Latin
letters and numbers) or a number (int).

I’ll show some examples:

name: Alex
age: 12
Converted into a dictionary.

{
  "name": "Alex",
  "age": 12
}

Note that the number automatically gets type int.

Another example shows that the string may contain spaces.

name: Alex Fox
age: 12

class: 12b
Will be converted into the next dictionary.

{
  "age": 12,
  "name": "Alex Fox",
  "class": "12b"
}

Pay attention to a few things. Between the string "age" and the string "class" there is an
empty string that doesn’t interfere with parsing. The class starts with numbers, but has
letters, which means it cannot be converted to numbers, so its type remains a str.

Input: A format string.

Output: An object (dictionary).

Examples:
assert yaml("name: Alex\nage: 12") == {"name": "Alex", "age": 12}
assert yaml("name: Alex Fox\nage: 12\n\nclass: 12b") == {
    "age": 12,
    "name": "Alex Fox",
    "class": "12b",
}

Precondition: YAML 1.2 is being used with JSON Schema.

----------
----------

¿Has oído hablar alguna vez de un lenguaje de marcado como YAML? Es un formato de serialización de datos amigable.
De hecho, es tan amigable que tanto las personas como los programas pueden leerlo bastante bien. Puedes jugar
con el estándar siguiendo este enlace.

YAML es un texto, y necesitas convertirlo en un objeto. Pero no te estoy pidiendo que implementes
todo el estándar YAML, lo implementaremos paso a paso.

El primer paso es la conversión clave-valor. La clave puede ser cualquier cadena formada por letras
y números. El valor puede ser una cadena de una sola línea (formada por espacios, letras
letras latinas y números) o un número (int).

Mostraré algunos ejemplos:

nombre: Alex
edad 12
Convertido en un diccionario.

{
  "nombre": "Alex",
  "edad": 12
}

Observe que el número obtiene automáticamente el tipo int.

Otro ejemplo muestra que la cadena puede contener espacios.

nombre: Alex Fox
edad 12

clase 12b
Estará en el siguiente diccionario.

{
  "edad": 12,
  "nombre": "Alex Fox",
  "clase": "12b"
}

Presta atención a algunas cosas. Entre la cadena "edad" y la cadena "clase" hay una cadena
cadena vacía que no interfiere con el análisis. La clase empieza con números, pero tiene
letras, lo que significa que no se puede convertir a números, por lo que su tipo sigue siendo una cadena.

Entrada: Una cadena de formato.

Salida: Un objeto (diccionario).

Ejemplos:
assert yaml("nombre: Alexedad: 12") == {"nombre": "Alex", "edad": 12}
assert yaml("nombre: Alex Fox\nedad: 12\nclase: 12b") == {
    "edad": 12,
    "nombre": "Alex Fox",
    "class": "12b",
}

Precondición: Se está utilizando YAML 1.2 con JSON Schema.

liks
------
https://yaml-online-parser.appspot.com/
https://yaml.org/
https://yaml.org/spec/1.2-old/spec.html#id2803231
'''


def yaml(a: str) -> dict:
    # your code here
    result = {}
    lines = a.split("\n")
    for line in lines:
        if ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            if value.isdigit():
                value = int(value)
            result[key] = value
    return result


print("Example:")
print(
    yaml(
        """name: Alex
age: 12"""
    )
)

# These "asserts" are used for self-checking
assert yaml("name: Alex\nage: 12") == {"name": "Alex", "age": 12}
assert yaml("name: Alex Fox\nage: 12\n\nclass: 12b") == {
    "age": 12,
    "name": "Alex Fox",
    "class": "12b",
}

print("The mission is done! Click 'Check Solution' to earn rewards!")
