'''
This is the second task on parsing YAML. It represents the next step where parsing gets
more complicated. The data types, such as None and bool, are being added, and besides that,
you’re getting the ability to use quotes in strings.

Here are some of the examples:

name: "Bob Dylan"
children: 6
{
  "name": "Bob Dylan",
  "children": 6
}

name: "Alex \\"Fox\\""
children: 6
{
  "name": "Alex \"Fox\"",
  "children": 6
}

As you can see, the string can be put in quotes. It can be both double and single quotes.

name: "Bob Dylan"
children: 6
alive: false

{
  "name": "Bob Dylan",
  "alive": False,
  "children": 6
}

True and False are the keywords defining the bool type.

name: "Bob Dylan"
children: 6
coding:

{
  "coding": None,
  "name": "Bob Dylan",
  "children": 6
}

If no value is specified, it becomes undefined. There also is a keyword for this - None.

Input: A format string.

Output: An object (list/dictionary).

Examples:
assert yaml("name: Alex\nage: 12") == {"name": "Alex", "age": 12}
assert yaml("name: Alex Fox\nage: 12\n\nclass: 12b") == {
    "age": 12,
    "name": "Alex Fox",
    "class": "12b",
}
assert yaml('name: "Alex Fox"\nage: 12\n\nclass: 12b') == {
    "age": 12,
    "name": "Alex Fox",
    "class": "12b",
}
assert yaml('name: "Alex \\"Fox\\""\nage: 12\n\nclass: 12b') == {
    "age": 12,
    "name": 'Alex "Fox"',
    "class": "12b",
}

Precondition: YAML 1.2 is being used with JSON Schema.

----------
----------

Esta es la segunda tarea de análisis sintáctico de YAML. Representa el siguiente paso donde el parseo se hace
más complicado. Los tipos de datos, como None y bool, están siendo añadidos, y además de eso,
que está recibiendo la capacidad de utilizar comillas en las cadenas.

He aquí algunos ejemplos:

nombre: "Bob Dylan"
niños: 6
{
  "nombre": "Bob Dylan",
  "children": 6
}

nombre: "Alex Fox"
niños: 6
{
  "nombre "Alex \"Fox\"",
  "niños": 6
}

Como puede ver, la cadena puede ir entre comillas. Pueden ser tanto comillas dobles como simples.

nombre: "Bob Dylan"
hijos: 6
vivo: false

{
  "nombre": "Bob Dylan"
  "alive": Falso,
  "niños": 6
}

True y False son las palabras clave que definen el tipo bool.

nombre: "Bob Dylan"
niños: 6
codificación:

{
  "codificación": Ninguno,
  "name": "Bob Dylan",
  "children": 6
}

Si no se especifica ningún valor, se convierte en indefinido. También hay una palabra clave para esto - Ninguno.

Entrada: Una cadena de formato.

Salida: Un objeto (lista/diccionario).

Ejemplos:
assert yaml("nombre: Alexedad: 12") == {"nombre": "Alex", "edad": 12}
assert yaml("nombre: Alex Fox\nedad: 12\nclase: 12b") == {
    "edad": 12,
    "nombre": "Alex Fox",
    "class": "12b",
}
assert yaml('nombre: "Alex Fox "edad: 12clase: 12b') == {
    "edad": 12,
    "name": "Alex Fox",
    "class": "12b",
}
assert yaml('nombre: "Alex Fox" edad: 12 clase: 12b') == {
    "edad": 12,
    "name": 'Alex "Fox"',
    "clase": "12b",
}

Precondición: Se está utilizando YAML 1.2 con JSON Schema.
'''


# Taken from mission YAML. Simple Dict


BOOLS = ['false', 'true']


def yaml(a):
    obj = {}
    for line in a.splitlines():
        split_index = line.find(':')
        if split_index != -1:
            name, val_str = line[:split_index].strip(), line[split_index + 1:].strip()
            if val_str.startswith('"') and val_str.endswith('"'):
                value = val_str[1:-1].replace('\\"', '"')
            elif val_str in BOOLS:
                value = bool(BOOLS.index(val_str))
            elif val_str.isdigit():
                value = int(val_str)
            elif val_str == 'null' or not val_str:
                value = None
            else:
                value = val_str
            obj[name] = value
    return obj


print("Example:")
print(yaml("name: Alex\nage: 12"))

# These "asserts" are used for self-checking
assert yaml("name: Alex\nage: 12") == {"name": "Alex", "age": 12}
assert yaml("name: Alex Fox\nage: 12\n\nclass: 12b") == {
    "age": 12,
    "name": "Alex Fox",
    "class": "12b",
}
assert yaml('name: "Alex Fox"\nage: 12\n\nclass: 12b') == {
    "age": 12,
    "name": "Alex Fox",
    "class": "12b",
}
assert yaml('name: "Alex \\"Fox\\""\nage: 12\n\nclass: 12b') == {
    "age": 12,
    "name": 'Alex "Fox"',
    "class": "12b",
}
assert yaml('name: "Bob Dylan"\nchildren: 6\nalive: false') == {
    "name": "Bob Dylan",
    "alive": False,
    "children": 6,
}
assert yaml('name: "Bob Dylan"\nchildren: 6\ncoding:') == {
    "coding": None,
    "name": "Bob Dylan",
    "children": 6,
}
assert yaml('name: "Bob Dylan"\nchildren: 6\ncoding: null') == {
    "coding": None,
    "name": "Bob Dylan",
    "children": 6,
}
assert yaml('name: "Bob Dylan"\nchildren: 6\ncoding: "null" ') == {
    "coding": "null",
    "name": "Bob Dylan",
    "children": 6,
}

print("The mission is done! Click 'Check Solution' to earn rewards!")
