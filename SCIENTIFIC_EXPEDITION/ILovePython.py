'''
Over six years ago, in December 1989, I was looking for a "hobby" programming project that would
keep me occupied during the week around Christmas. My office (a government-run research lab in
Amsterdam) would be closed, but I had a home computer, and not much else on my hands. I decided
to write an interpreter for the new scripting language I had been thinking about lately: a
descendant of ABC that would appeal to Unix/C hackers. I chose Python as a working title for
the project, being in a slightly irreverent mood (and a big fan of Monty Python's Flying Circus).

Today, I can safely say that Python has changed my life. I have moved to a different continent.
I spend my working days developing large systems in Python, when I'm not hacking on Python or
answering Python-related email. There are Python T-shirts, workshops, mailing lists, a newsgroup,
and now a book. Frankly, my only unfulfilled wish is to have my picture on the front page of the
New York Times.

-- Guido van Rossum, Foreword for "Programming Python", Reston, VA, May 1996

This mission is simple to solve. You are given a function called "i_love_python" which will only
return the phrase - "I love Python!"

Let's write an essay in python code which will explain why you love python (if you don't love it,
when we will make an additional mission special for the haters). Publishing the default solution
will only earn you 0 points as the goal is to earn points through votes for your code essay.

Input: Nothing.

Output: The string "I love Python!".

Example:
i_love_python() == "I love Python!"

How it is used: This mission revolves around code literacy.

----------
----------

Hace más de seis años, en diciembre de 1989, buscaba un proyecto de programación como "hobby"
que me mantuviera ocupado durante la semana de Navidad. Mi oficina (un laboratorio de
investigación gubernamental en Amsterdam) estaría cerrada, pero tenía un ordenador en casa
y no mucho más en mis manos. Decidí escribir un intérprete para el nuevo lenguaje de scripting
en el que había estado pensando últimamente: un descendiente de ABC que atrajera a los hackers
de Unix/C. Elegí Python como lenguaje de trabajo. Elegí Python como título provisional para el
proyecto, ya que estaba de un humor ligeramente irreverente (y era un gran fan de Monty Python's
Flying Circus).

Hoy puedo decir que Python me ha cambiado la vida. Me he mudado a otro continente. Paso mis días
de trabajo desarrollando grandes sistemas en Python, cuando no estoy hackeando Python o contestando
correos electrónicos relacionados con Python. Hay camisetas de Python, talleres, listas de correo,
un grupo de noticias y ahora un libro. Francamente, mi único deseo no cumplido es que mi foto
aparezca en la portada del New York Times.

-- Guido van Rossum, Prólogo de "Programming Python", Reston, VA, mayo de 1996

Esta misión es sencilla de resolver. Se te da una función llamada "i_love_python" que sólo devolverá
la frase - "¡Me encanta Python!"

Vamos a escribir un ensayo en código python que explicará por qué te encanta python (si no te
encanta, cuando haremos una misión adicional especial para los haters). La publicación de la solución
por defecto sólo le hará ganar 0 puntos, ya que el objetivo es ganar puntos a través de votos para su
ensayo de código.

Entrada: Nada.

Salida: La cadena "¡Me encanta Python!".

Ejemplo:
i_love_python() == "¡Me encanta Python!"

Cómo se utiliza: Esta misión gira en torno a la alfabetización en código.
'''


def i_love_python():
    """
        Let's explain why do we love Python.
    """
    """
        This essay explains why Python is loved by many developers.
        """

    # Python is Readable and Elegant
    python_is_readable = True
    python_is_elegant = True

    if python_is_readable and python_is_elegant:
        print("Python's readability and elegance make it a joy to work with.")

    # Python is Beginner-Friendly
    python_is_beginner_friendly = True

    if python_is_beginner_friendly:
        print("Python's simplicity and clear syntax make it an excellent language for beginners.")

    # Python is Versatile
    python_is_versatile = True

    if python_is_versatile:
        print(
            "Python's versatility allows it to be used in various domains, such as web development, "
            "data analysis, machine learning, and more.")

    # Python has a Rich Ecosystem
    python_has_rich_ecosystem = True

    if python_has_rich_ecosystem:
        print(
            "Python has a vast collection of libraries and frameworks that empower developers to build "
            "complex applications efficiently.")

    # Python has a Strong Community
    python_has_strong_community = True

    if python_has_strong_community:
        print(
            "Python has a supportive and active community that fosters collaboration, knowledge sharing, "
            "and continuous improvement.")

    # Python is Cross-Platform
    python_is_cross_platform = True

    if python_is_cross_platform:
        print("Python runs on multiple platforms, including Windows, macOS, Linux, making it "
              "highly accessible.")

    # Python is High-Level and Productive
    python_is_high_level = True
    python_is_productive = True

    if python_is_high_level and python_is_productive:
        print(
            "Python's high-level nature and productivity-enhancing features enable developers to "
            "write code faster and focus on problem-solving.")

    # Python is Reliable and Scalable
    python_is_reliable = True
    python_is_scalable = True

    if python_is_reliable and python_is_scalable:
        print(
            "Python's reliability and scalability make it suitable for building large-scale, "
            "mission-critical applications.")

    # Python has Great Documentation
    python_has_great_documentation = True

    if python_has_great_documentation:
        print(
            "Python's extensive and well-maintained documentation helps developers find "
            "solutions and learn effectively.")

    # Python has Guido van Rossum
    python_has_guido_van_rossum = True

    if python_has_guido_van_rossum:
        print(
            "Python has the brilliant mind of Guido van Rossum, its creator, whose vision and "
            "leadership have shaped the language.")

    return "I love Python!"


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert i_love_python() == "I love Python!"

