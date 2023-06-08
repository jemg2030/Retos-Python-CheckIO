'''
"di-dah di-di-di-dit di-dah-dah di-dah-dah-dah dah-di-dit dah-di-di-dah", sound
of Morszelizer clanked out loud.

"What're you doing?" Nikola asked curiously.

"I'm sending our time logs for the last expedition to headquarters, but it's not an easy task..."
Stephen grumbled, "Can you imagine that with all the computer power at our disposal, I STILL
have to convert this message to Morse-code with only an on/off button... Hrmph... what a pain."
He grumbled at the inconvenience.

"Let me look at it." Nikola offered his help, "It looks like a pretty easy solution, we could
automate the process."

"Oh.. you hero of my day." Stephen started excitedly. "So, how do we start it?"

"With Python!" Nikola exclaimed.

Help Stephen to create a module for converting a normal time string to a morse time string. As
you can see in the illustration, a gray circle means on, while a white circle means off. Every
digit in the time string contains a different number of slots. The first digit for the hours has
a length of 2 while the second digit for the hour has a length of 4. The first digits for the
minutes and seconds have a length of 3 while the second digits for the minutes and seconds have a
length of 4. Every digit in the time is converted to binary representation. You will convert every
on (or 1) signal to dash ("-") and every off (or 0) signal to dot (".").

example source: Wikipedia

An time string could be in the follow formats: "hh:mm:ss" , "h:m:s" or "hh:m:ss" . The "missing"
digits are zeroes. For example, "1:2:3" is the same as "01:02:03".

The result will be a morse time string with specific format:
"h h : m m : s s"
where each digits represented as sequence of "." and "-"

Input: A normal time string as a string (unicode).

Output: The morse time string as a string.

Example:
checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-"
checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--."
checkio("00:1:02") == ".. .... : ... ...- : ... ..-."
checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-"

How it is used: Did you see the binary clocks task earlier? This is can be a fun gift for any geek.
We tried to combine the old good Morse code with a binary clock in this task, and now you can create
the new more complex binary clock, which doesn't show time -- but makes morse style bips and beeps. ;-)

Precondition:
time_string contains correct time.

----------
----------

"di-dah di-di-di-dit di-dah-dah di-dah-dah-dah dah-di-dit dah-di-di-dah", El Morszelidazor
hacía fuertes ruidos metalicos.

"Que estas haciendo?" pregunto Nikola con curiosidad.

"Estoy enviando los registros de la ultima expedicion al cuartel general, pero no es una tara
facil..." refunfuño Stephen , "Puedes imaginar que con toda la potencia de los ordenadores que
tenemos a nuestra disposicion tengo que un mensaje a codigo Morse con solo un boton de encendido/apagado...
Mmm... que fastidio." Se quejo del problema.

"Dejame echar un vistazo." Nikola ofrecio su ayuda, "Parece que hay una magnfica solucion,
podriamos automatizar el proceso."

"Oh.. tu, mi heroe." dijo Stephen excitado . "Pero, como lo hacemos?"

"Con Python!" Nikola exclaimed.

Ayuda a Stephen a crear un modulo para convertir una cadena con horario normal en una cadena con
horario Morse. Como puedes ver en la ilustracion, el circulo gris significa "encendido", mientras
que el circulo blanco significa "apagado". Todo digito en la cadena del horario tiene un numero
diferente de ranuras. El primer digito de la hora contiene una longitud de 2 mientras que el
segundo tiene una longitud de 4. El primer digito de los minutos y los segundos tiene una longitud
de 3 mientras que el segundo digito de los minutos y los segundos tienen una longitud de 4. Todos
los digitos son convertidos a representacion binaria .Tu convertiras todo "encendido" (o 1) en
una raya ("-") and todo "apagado" (o 0) en un punto (".")

example source: Wikipedia

Una cadena de tiempo puede estar en los siguientes formatos: "hh:mm:ss" , "h:m:s" or "hh:m:ss".
Los digitos perdidos se tomaran como cero. Por ejemplo, "1:2:3" es lo mismo que "01:02:03".

El resultado sera una cadena de tiempo en morse con el siguiente formato:
"h h : m m : s s"
donde cada digito esatara representado por una secuencia de "." and "-".

Input: Una cadena de tiempo normal como string (unicode).

Output: Una cadena de tiempo en morse como string.

Ejemplo:
checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-"
checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--."
checkio("00:1:02") == ".. .... : ... ...- : ... ..-."
checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-"

Para que se usa: Has visto la tarea del reloj binario antes? Esto es puede ser un regalo
divertido para cualquier geek. Tratamos de combinar el viejo buen codigo Morse con un reloj
binario en esta tarea, y ahora se puede crear el nuevo reloj binario mas complejo, no muestra
el tiempo - pero hace bips and beeps estilo morse. ;-)

Precondicion:
time_string contiene el tiempo correctamente.

link
------
https://en.wikipedia.org/wiki/Binary_clock
'''


def checkio(time_string: str) -> str:

    #replace this for solution
    tab = [2, 4, 0, 3, 4, 0, 3, 4]
    wined: str = ""

    if len(time_string) < 8:
        counter = 0
        ile = len(time_string)
        for a in range(ile):
            if time_string[a] != ":":
                counter += 1
            else:
                if counter == 1:
                    time_string = time_string[:(a - 1)] + "0" + time_string[(a - 1):]
                    ile = ile + 1
                counter = 0

    if len(time_string) < 8:
        time_string = time_string[:(6)] + "0" + time_string[(6):]

    i = 0
    for i in range(len(time_string)):
        if time_string[i] != ":":
            libc = '{0:b}'.format(int(time_string[i]))
            if int(len(libc)) < int(tab[i]):
                j = 0
                for j in range(tab[i] - len(libc)):
                    libc = "0" + libc
            k = 0
            for k in range(len(libc)):
                if libc[k] == "0":
                    wined = wined + "."
                else:
                    wined = wined + "-"
            wined = wined + " "
        else:
            wined = wined + ": "
    wined = wined.rstrip()
    return wined


if __name__ == '__main__':
    print("Example:")
    print(checkio("10:37:49"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"
    print("Coding complete? Click 'Check' to earn cool rewards!")
