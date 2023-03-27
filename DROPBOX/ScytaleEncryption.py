'''
This is the second in a series of missions dedicated to classical cryptography. In this mission we
will try to break the Scytale encryption.

Scytale is one of the first known cryptographic devices, used by ancient Greeks, namely Spartans,
during their military campaigns. It consisted of a cylindrical rod or staff with a long strip of
parchment wrapped around it. The sender would simply write the message along the length of the rod
and across the winds of a strip until the end of the parchment was reached, then turn the cylinder
and continue writing the next line. After unwinding the parchment, the text became unintelligible.
To decrypt the message, it would be wrapped around another scytale of the same diameter, after which
the plaintext could be read along it.
Scytale is a transposition cipher. Unlike substitution ciphers, like Atbash or Caesar's cipher, here
the letters of the plaintext remain unchanged, but their order is altered.

For example, suppose the message is "let's meet at eleven in the evening" and diameter of the rod
allows to write 4 letters in a circle. The scytale with a message written on it would look like this:

After unwinding the strip the message becomes lteeeanvttaesetnmltieehneveg .

If an adversary intercepted a message, they wouldn't be able to read it unless they knew the key to
encryption - in this case, the diameter of the cylinder (or, more specifically, number of letters that c
ould be written in a circle around it). However, it could easily be found by trying several rods of
different size. Another method (attributed to Aristotle) includes wrapping the parchment with encrypted
message around a cone-shaped rod with varying diameter until a fragment of text becomes readable.

In this mission we'll try to break a scytale encryption. You have a cryptogram and a crib - a word that
is expected to be in the decrypted message. You need to try all the possible keys until you get a plaintext
that contains the crib. If after trying every key you either found no such plaintext, or found more than one
possible keys - return None .

There is also one last piece of informaion: you know that the sender encrypts the messages using the shortest
possible strip of parchment, so that there are no empty spaces on it. for example, the message "let's meet at
eleven in the evening" , encrypted with key 5 , will look like this:


Note that the lines have different lengths. The cryptogram will be "leeteetvhntaeeistnenmeivgeln" .

Input: ciphertext: str, crib: str

Output: plaintext: str or None

Example:
scytale_decipher('aaaatctwtkdn', 'dawn') == 'attackatdawn'
scytale_decipher('hdoeerlallrdow', 'world') == 'hellodearworld'
scytale_decipher('totetshpmeecisendysescwticsriasraytlaegphet', 'sicret') == None  #Crib is not in plaintext
scytale_decipher('aaaatctwtkdn', 'at') == None                                     #More than one possible decryptions

----------
----------

Esta es la segunda de una serie de misiones dedicadas a la criptografía clásica. En esta misión
intentaremos descifrar el cifrado Scytale.

El Scytale es uno de los primeros dispositivos criptográficos conocidos, utilizado por los antiguos
griegos, concretamente los espartanos, durante sus campañas militares. Consistía en una varilla
cilíndrica o bastón con una larga tira de pergamino enrollada alrededor. El remitente simplemente
escribía el mensaje a lo largo de la varilla y a través de los vientos de una tira hasta llegar al
final del pergamino, luego giraba el cilindro y continuaba escribiendo la siguiente línea. Una vez
desenrollado el pergamino, el texto se volvía ininteligible. Para descifrar el mensaje, se envolvía
en otra guadaña del mismo diámetro, tras lo cual se podía leer el texto en claro a lo largo de ella.
Scytale es un cifrado por transposición. A diferencia de los cifrados de sustitución, como Atbash o
el cifrado César, aquí las letras del texto plano permanecen inalteradas, pero su orden se altera.

Por ejemplo, supongamos que el mensaje es "quedamos a las once de la noche" y el diámetro de la varilla
permite escribir 4 letras en círculo. La guadaña con el mensaje escrito tendría este aspecto:

Después de desenrollar la tira el mensaje se convierte en lteeeanvttaesetnmltieehneveg .

Si un adversario interceptara el mensaje, no podría leerlo a menos que conociera la clave del cifrado,
en este caso, el diámetro del cilindro (o, más concretamente, el número de letras que podrían escribirse
en un círculo a su alrededor). Sin embargo, se podía averiguar fácilmente probando con varias varillas de
distinto tamaño. Otro método (atribuido a Aristóteles) consiste en envolver el pergamino con el mensaje
cifrado alrededor de una varilla en forma de cono de diámetro variable hasta que un fragmento del texto
resulte legible.

En esta misión intentaremos descifrar un cifrado de guadaña. Tienes un criptograma y una clave - una palabra
que se espera que esté en el mensaje descifrado. Tienes que probar todas las claves posibles hasta que
obtengas un texto plano que contenga la cuna. Si después de probar todas las claves no encuentra dicho
texto plano, o encuentra más de una clave posible, devuelve Ninguno.

También hay un último dato: sabes que el remitente encripta los mensajes utilizando la tira de pergamino
más corta posible, de modo que no haya espacios vacíos en ella. por ejemplo, el mensaje "quedamos a las
once de la noche" , encriptado con la clave 5 , tendrá este aspecto:

Observa que las líneas tienen longitudes diferentes. El criptograma será "leeteetvhntaeeistnenmeivgeln" .

Entrada: texto cifrado: cadena, crib: cadena

Salida: texto plano: cadena o Ninguno

Ejemplo: scytale_decipher
scytale_decipher('aaaatctwtkdn', 'dawn') == 'attackatdawn'
scytale_decipher('hdoeerlallrdow', 'mundo') == 'hellodearworld'
scytale_decipher('totetshpmeecisendysescwticsriasraytlaegphet', 'sicret') == None #Crib no está en texto plano
scytale_decipher('aaaatctwtkdn', 'at') == None #Más de un descifrado posible
'''


from typing import Optional


def scytale_decipher(ciphertext: str, crib: str) -> Optional[str]:
    # your code here
    ciphertext_len = len(ciphertext)
    for diameter in range(1, ciphertext_len // 2 + 1):
        plaintext = ""
        for i in range(diameter):
            plaintext += ciphertext[i::diameter]
        if crib in plaintext:
            # check if there is only one possible key
            possible_plaintexts = []
            for d in range(1, ciphertext_len // 2 + 1):
                possible_plaintext = ""
                for i in range(d):
                    possible_plaintext += ciphertext[i::d]
                if crib in possible_plaintext:
                    possible_plaintexts.append(possible_plaintext)
            if len(possible_plaintexts) == 1:
                return plaintext
            else:
                return None
    return None


if __name__ == "__main__":
    print("Example:")
    print(scytale_decipher("aaaatctwtkdn", "dawn"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert scytale_decipher("aaaatctwtkdn", "dawn") == "attackatdawn"
    assert scytale_decipher("hdoeerlallrdow", "world") == "hellodearworld"
    assert (
        scytale_decipher("totetshpmeecisendysescwticsriasraytlaegphet", "sicret")
        == None
    ), "Crib is not in plaintext"
    assert (
        scytale_decipher("aaaatctwtkdn", "at") == None
    ), "More than one possible decryptions"

    print("Coding complete? Click 'Check' to earn cool rewards!")
