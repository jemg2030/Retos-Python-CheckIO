"""
The 4th task in the series of missions about the YAML format will be devoted to a complex structure.

YAML	Python/TypeScript

A list element can be another list.

        - Alex
        -
          - odessa
          - dnipro
        - Li

        [
          "Alex",
          [
            "odessa",
            "dnipro"
          ],
          "Li"
        ]

A dictionary can also be an element of an list.

        - 67
        -
          name: Irv
          game: Mario
        -
        - 56

        [
          67,
          {
            "game": "Mario",
            "name": "Irv"
          },
          None/null,
          56
        ]

A dictionary element can be another dictionary.

        name: Alex
        study:
          type: school
          number: 78
        age: 14

        {
          "age": 14,
          "study": {
            "type": "school",
            "number": 78
          },
          "name": "Alex"
        }

A list can also be an element of dictionary.

        name: Alex
        study:
          - 89
          - 89
          - "Hell"
        age: 14

        {
          "age": 14,
          "study": [
            89,
            89,
            "Hell"
          ],
          "name": "Alex"
        }

And, of course, data can have more than one nesting level.

        name: Alex
        study:
          -
            type: school
            num: 89
          -
            type: school
            num: 12
        age: 14

        {
          "age": 14,
          "study": [
            {
              "num": 89,
              "type": "school"
            },
            {
              "num": 12,
              "type": "school"
            }
          ],
          "name": "Alex"
        }


Input: Format string.

Output: An object (list/dictionary).

Examples:

assert yaml("- Alex\n-\n  - odessa\n  - dnipro\n- Li") == [
    "Alex",
    ["odessa", "dnipro"],
    "Li",
]
assert yaml("- 67\n-\n  name: Irv\n  game: Mario\n-\n- 56") == [
    67,
    {"game": "Mario", "name": "Irv"},
    None,
    56,
]
assert yaml("name: Alex\nstudy:\n  type: school\n  number: 78\nage: 14") == {
    "age": 14,
    "study": {"type": "school", "number": 78},
    "name": "Alex",
}
assert yaml('name: Alex\nstudy:\n  - 89\n  - 89\n  - "Hell"\nage: 14') == {
    "age": 14,
    "study": [89, 89, "Hell"],
    "name": "Alex",
}

Precondition: The YAML 1.2 standard is being used.

----------
----------


"""


# return converted
def convert(value):
    transform = {
        '"null"': "null",
        "": None,
        "null": None,  # value
        "true": True,
        "false": False,
    }  #
    if value in transform:
        return transform[value]
    value = value.replace("\\", "").replace('"', '"')
    if value[0] == value[-1] == '"':
        value = value[1:-1]
    return int(value) if value.isdigit() else value


# remove comment
def remove_comment(text):
    # from line
    quoted, data = False, ""
    for char in text:  #
        if char == '"':
            quoted = not quoted
        if char == "#" and not quoted:
            return data
        data += char
    return data


# recursively get yaml
def get_yaml(text):
    # block indent
    index = lambda x: len(x) - len(x.lstrip())
    ix = index(text[0])
    # type of block
    (delimeter, result) = ("-", []) if "-" in text[0] else (":", {})
    # let's go through the block
    while text:
        # get line
        line = text.pop(0)
        # get key and value
        key, value = line.split(delimeter)
        # if list then key = ''
        key, value = key.strip(), convert(value.strip())
        if line.strip()[-1] == delimeter and text and index(text[0]) != ix:
            # if find sub-block, go recursively through one
            subtext = []
            # get subblock text
            while text and index(text[0]) != ix:
                subtext.append(text.pop(0))
            # recursion
            value = get_yaml(subtext)
        if delimeter == ":":
            # add value to result
            result.update({key: value})
        else:
            result.append(value)
    return result


def yaml(a: str) -> list | dict:
    # your code here
    value = [remove_comment(line) for line in a.split("\n") if line and line[0] != "#"]
    return get_yaml(value)


print("Example:")
print(yaml("- Alex\n" "-\n" "  - odessa\n" "  - dnipro\n" "- Li"))

# These "asserts" are used for self-checking
assert yaml("- Alex\n-\n  - odessa\n  - dnipro\n- Li") == [
    "Alex",
    ["odessa", "dnipro"],
    "Li",
]
assert yaml("- 67\n-\n  name: Irv\n  game: Mario\n-\n- 56") == [
    67,
    {"game": "Mario", "name": "Irv"},
    None,
    56,
]
assert yaml("name: Alex\nstudy:\n  type: school\n  number: 78\nage: 14") == {
    "age": 14,
    "study": {"type": "school", "number": 78},
    "name": "Alex",
}
assert yaml('name: Alex\nstudy:\n  - 89\n  - 89\n  - "Hell"\nage: 14') == {
    "age": 14,
    "study": [89, 89, "Hell"],
    "name": "Alex",
}
assert yaml(
    "name: Alex\nstudy:\n  -\n    type: school\n    num: 89\n  -\n    type: school\n    num: 12\nage: 14"
) == {
    "age": 14,
    "study": [{"num": 89, "type": "school"}, {"num": 12, "type": "school"}],
    "name": "Alex",
}
assert yaml(
    "name: Alex\nstudy:\n  -\n    type: school\n    nums:\n      - 12\n      - 67\n  -\n    type: school\n    num: 12\nage: 14"
) == {
    "age": 14,
    "study": [{"type": "school", "nums": [12, 67]}, {"num": 12, "type": "school"}],
    "name": "Alex",
}

print("The mission is done! Click 'Check Solution' to earn rewards!")
