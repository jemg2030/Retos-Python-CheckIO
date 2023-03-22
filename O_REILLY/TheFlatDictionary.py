'''
Nikola likes to categorize everything in sight. One time Stephan gave him a label maker for his birthday,
and the robots were peeling labels off of every surface in the ship for weeks. He has since categorized all
the reagents in his laboratory, books in the library and notes on the desk. But then he learned about Python
dictionaries, and categorized all the possible configurations for Sophia’s drones. Now the files are organized
in a deep nested structure, but Sophia doesn’t like this. Let's help Sophia to flatten these dictionaries.

Python dictionaries are a convenient data type to store and process configurations. They allow you to store
data by keys to create nested structures. You are given a dictionary where the keys are strings and the values
are strings or dictionaries. The goal is flatten the dictionary, but save the structures in the keys. The
result should be the a dictionary without the nested dictionaries. The keys should contain paths that contain
the parent keys from the original dictionary. The keys in the path are separated by a "/". If a value is an empty
dictionary, then it should be replaced by an empty string (""). Let's look at an example:

{
    "name": {
        "first": "One",
        "last": "Drone"
    },
    "job": "scout",
    "recent": {},
    "additional": {
        "place": {
            "zone": "1",
            "cell": "2"}
    }
}

The result will be:

{"name/first": "One",           # one parent
 "name/last": "Drone",
 "job": "scout",                # root key
 "recent": "",                  # empty dict
 "additional/place/zone": "1",  # third level
 "additional/place/cell": "2"}

Input: An original dictionary as a dict.

Output: The flattened dictionary as a dict.

Examples:
assert flatten({"key": "value"}) == {"key": "value"}
assert flatten({"key": {"deeper": {"more": {"enough": "value"}}}}) == {
    "key/deeper/more/enough": "value"
}
assert flatten({"empty": {}}) == {"empty": ""}
assert flatten(
    {
        "name": {"first": "One", "last": "Drone"},
        "job": "scout",
        "recent": {},
        "additional": {"place": {"zone": "1", "cell": "2"}},
    }
) == {
    "name/first": "One",
    "name/last": "Drone",
    "job": "scout",
    "recent": "",
    "additional/place/zone": "1",
    "additional/place/cell": "2",
}

How it is used: This concept can be useful if you need to parse config files and simplify structures
for grandfathered systems and file structures. You can easily modify this idea for your own specifications.
Besides that, it's a useful skill to be able to read code and search for bugs.

Preconditions:
keys in a dictionary are non-empty strings;
values in a dictionary are strings or dicts;
root_dictionary != {}.

----------
----------

A Nikola le gusta clasificar todo lo que ve. Una vez Stephan le regaló una etiquetadora por su cumpleaños,
y los robots estuvieron despegando etiquetas de todas las superficies de la nave durante semanas. Desde
entonces ha categorizado todos los reactivos de su laboratorio, los libros de la biblioteca y las notas
del escritorio. Pero entonces conoció los diccionarios de Python y categorizó todas las configuraciones
posibles para los drones de Sophia. Ahora los archivos están organizados en una profunda estructura anidada,
pero a Sophia no le gusta esto. Ayudemos a Sophia a aplanar estos diccionarios.

Los diccionarios de Python son un tipo de datos muy práctico para almacenar y procesar configuraciones.
Permiten almacenar datos por claves para crear estructuras anidadas. Se te da un diccionario donde las
claves son cadenas y los valores son cadenas o diccionarios. El objetivo es aplanar el diccionario,
pero guardar las estructuras en las claves. El resultado debería ser un diccionario sin los diccionarios
anidados. Las claves deben contener rutas que contengan las claves padre del diccionario original. Las
claves de la ruta están separadas por un "/". Si un valor es un diccionario vacío, debe sustituirse por
una cadena vacía (""). Veamos un ejemplo:

{
    "nombre": {
        "primero": "uno",
        "último": "Drone"
    },
    "job": "explorador",
    "reciente": {},
    "adicional": {
        "place": {
            "zona": "1",
            "celda": "2"}
    }
}

El resultado será:
{"nombre/primero": "Uno", # un padre
 "nombre/apellido": "Drone",
 "job": "explorador", # clave raíz
 "reciente": "", # empty dict
 "adicional/lugar/zona": "1", # tercer nivel
 "additional/place/cell": "2"}

Entrada: Un diccionario original como dict.

Salida: El diccionario aplanado como dict.

Ejemplo:
assert aplanar({"clave": "valor"}) == {"clave": "valor"}
assert flatten({"clave": {"más profundo": {"más": {"suficiente": "valor"}}}}) == {
    "clave/más/profundo/más/suficiente": "valor"
}
assert flatten({"vacío": {}}) == {"vacío": ""}
assert flatten(
    {
        "nombre": {"first": "Uno", "último": "Drone"},
        "trabajo": "explorador",
        "reciente": {},
        "adicional": {"lugar": {"zona": "1", "celda": "2"}},
    }
) == {
    "nombre/nombre": "1",
    "name/last": "Drone",
    "job": "explorador",
    "reciente": "",
    "adicional/lugar/zona": "1",
    "additional/place/cell": "2",
}

Cómo se utiliza: Este concepto puede ser útil si necesitas analizar archivos de configuración y
simplificar estructuras para sistemas y estructuras de archivos antiguos. Puedes modificar fácilmente
esta idea para tus propias especificaciones. Además, es una habilidad útil para poder leer código y
buscar errores.

Precondiciones:
las claves de un diccionario son cadenas no vacías;
los valores de un diccionario son cadenas o dicts;
root_dictionary != {}.
'''


def flatten(dictionary: dict[str, str | dict]) -> dict[str, str]:
    # your code here
    result = {}
    for key, value in dictionary.items():
        if isinstance(value, dict) and value:
            subdict = flatten(value)
            for subkey, subvalue in subdict.items():
                result[key + '/' + subkey] = subvalue
        elif value == {}:
            result[key] = ""
        else:
            result[key] = value
    return result


print("Example:")
print(flatten({"key": "value"}))

# These "asserts" are used for self-checking
assert flatten({"key": "value"}) == {"key": "value"}
assert flatten({"key": {"deeper": {"more": {"enough": "value"}}}}) == {
    "key/deeper/more/enough": "value"
}
assert flatten({"empty": {}}) == {"empty": ""}
assert flatten(
    {
        "name": {"first": "One", "last": "Drone"},
        "job": "scout",
        "recent": {},
        "additional": {"place": {"zone": "1", "cell": "2"}},
    }
) == {
    "name/first": "One",
    "name/last": "Drone",
    "job": "scout",
    "recent": "",
    "additional/place/zone": "1",
    "additional/place/cell": "2",
}

print("The mission is done! Click 'Check Solution' to earn rewards!")
