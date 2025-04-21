"""
Cuarta tarea: Generación de números aleatorios

Imelda Run Montes Martín

El fichero contiene una clase Aleat, que actúa a modo de generador de números pseudoaleatorios; y una función aleat() que genera infinitamente números pseudoaleatorios.

"""

class Aleat:
    """
     Generador de números pseudoaleatorios usando el método congruencial lineal.

    Atributos:
        m (int): Módulo del generador. Define el rango superior de los valores generados.
        a (int): Multiplicador del generador.
        c (int): Incremento constante.
        x (int): Valor actual o semilla del generador.

    Métodos:
        __next__(): Devuelve el siguiente número pseudoaleatorio de la secuencia.
        __call__(num): Reinicia la semilla del generador con un nuevo valor.
        send(num): Establece una nueva semilla y devuelve inmediatamente el siguiente número.

    Pruebas unitarias:
    >>> rand = Aleat(m=32, a=9, c=13, x0=11)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    16
    29
    18
    15

    >>> rand(29)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    18
    15
    20
    1
    """
    def __init__(self, m=2**48, a=25214903917, c=11, x0=1212121):
        self.m = m
        self.a = a
        self.c = c
        self.x = x0

    def __next__(self):
        self.x = (self.a * self.x + self.c) % self.m
        return self.x
    
    def __call__(self, num):
        self.x = num

    def send(self, num):
        self.x = num 
        return next(self)

def aleat(m=2**48, a=25214903917, c=11,x0=1212121):
    """
    Generador de números pseudoaleatorios basado en el método congruencial lineal.

    Argumentos:
        m (int): Módulo del generador. Valor máximo excluyente del rango.
        a (int): Multiplicador del generador.
        c (int): Incremento constante.
        x0 (int): Valor inicial o semilla del generador.

    Salida:
        Un generador que produce números pseudoaleatorios enteros en el rango [0, m).

    >>> rand = aleat(m=64, a=5, c=46, x0=36)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    34
    24
    38
    44

    >>> rand.send(24)
    38
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    44
    10
    32
    14
    """
    x = x0
    while True:
        x = (a * x + c) % m
        num = yield x
        if num is not None:
            x = num

import doctest
doctest.testmod()