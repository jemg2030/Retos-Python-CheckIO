'''
"Where does a wise man hide a leaf? In the forest. But what does he do if there is no forest? ...
He grows a forest to hide it in."
-- Gilbert Keith Chesterton

Ever tried to send a secret message to someone without using the postal service? You could use newspapers
to tell your secret. Even if someone finds your message, it's easy to brush them off as paranoid and as
a conspiracy theorist. One of the simplest ways to hide a secret message is to use capital letters. Let's
find some of these secret messages.

You are given a chunk of text. Gather all capital letters in one word in the order that they appear
in the text.

For example: text = " H ow are you? E h, ok. L ow or L ower? O hhh.", if we collect all of the capital
letters, we get the message "HELLO".

Input: A text as a string (unicode).

Output: The secret message as a string or an empty string.

Example:
find_message(('How are you? Eh, ok. Low or Lower? '
 'Ohhh.')) == 'HELLO'
find_message('hello world!') == ''
find_message('HELLO WORLD!!!') == 'HELLOWORLD'

How it is used: This is a simple exercise in working with strings: iterate, recognize and concatenate.

Precondition: 0 < len(text) ≤ 1000
all(ch in string.printable for ch in text)

----------
----------

"Dónde un hombre sabio esconde una hoja? En el bosque. Pero que hace él si no hay bosque? ...
Él hace crecer un bosque para ocultarla ahí.
-- Gilbert Keith Chesterton

Alguna vez intentaste enviar un mensaje secreto a alguien sin usar el servicio postal? Podrías
usar periódicos para decir tu secreto. Incluso si alguien encuentra tu mensaje, es fácil quitarselos
de encima y eso es paranoía y una falsa teoría de conspiración. Una de las maneras más simples
de esconder un mensaje secreto es usar letras mayúsculas. Encontremos algunos de esos mensajes secretos.

Se te da tramo de texto. Reune todas las letras mayúsculas en una palabra en el orden que aparecen en
el texto.

Por ejemplo: texto = " H ow are you? E h, ok. L ow or L ower? O hhh.", Si recolectqamos todas las letras
mayúsculas, obtenemos el mensaje "HELLO".

Entrada: Un texto como cadena de carácteres (unicode).

Salida: El mensaje secreto como una cadena de carácteres o una cadena vacia.

Ejemlpo:
find_message(('How are you? Eh, ok. Low or Lower? '
 'Ohhh.')) == 'HELLO'
find_message('hello world!') == ''
find_message('HELLO WORLD!!!') == 'HELLOWORLD'

Cómo se usa: Este es un ejercicio simple para trabajar con cadenas de carácteres: iterar, reconocer
y concatenar.

Precondición: 0 < len(text) ≤ 1000
all(ch in string.printable for ch in text)
'''


def find_message(message: str) -> str:
    # your code here
    secret_message = ''
    for char in message:
        if char.isupper():
            secret_message += char
    return secret_message


if __name__ == '__main__':
    print("Example:")
    print(find_message(('How are you? Eh, ok. Low or Lower? '
 + 'Ohhh.')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert find_message(('How are you? Eh, ok. Low or Lower? '
 + 'Ohhh.')) == 'HELLO'
    assert find_message('hello world!') == ''
    assert find_message('HELLO WORLD!!!') == 'HELLOWORLD'
    print("Coding complete? Click 'Check' to earn cool rewards!")
