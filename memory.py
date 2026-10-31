
"""Memory, juego de encontrar parejas de números.

Modificaciones:
1. Validar los clics fuera del tablero.
2. Contar y mostrar las parejas descubiertas.
3. Detectar cuando todas las parejas han sido descubiertas.
"""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64

# Contador de parejas descubiertas.
parejas_encontradas = 0

# Indica si el jugador ya encontró todas las parejas.
juego_terminado = False


def square(x, y):
    """Dibuja un cuadrado blanco con contorno negro."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convierte las coordenadas (x, y) en el índice de una casilla."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convierte el índice de una casilla en coordenadas (x, y)."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Actualiza la selección y las casillas descubiertas."""
    global parejas_encontradas, juego_terminado

    # Evita jugar después de encontrar todas las parejas.
    if juego_terminado:
        return

    # Ignora los clics que se realizan fuera del tablero.
    if not (-200 <= x < 200 and -200 <= y < 200):
        return

    spot = index(x, y)
    mark = state['mark']

    # Evita seleccionar una casilla que ya fue descubierta.
    if not hide[spot]:
        return

    if mark is None:
        state['mark'] = spot

    elif mark == spot:
        return

    elif tiles[mark] == tiles[spot]:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

        # Incrementa el contador al encontrar una pareja.
        parejas_encontradas += 1

        # Comprueba si todas las parejas fueron descubiertas.
        if parejas_encontradas == 32:
            juego_terminado = True

    else:
        state['mark'] = spot


def draw():
    """Dibuja la imagen, las casillas y los mensajes."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    # Muestra las parejas descubiertas encima del tablero.
    up()
    goto(-190, 205)
    color('black')
    write(
        f'Parejas encontradas: {parejas_encontradas} / 32',
        font=('Arial', 12, 'normal')
    )

    # Muestra el mensaje cuando se completa el juego.
    if juego_terminado:
        goto(-110, -230)
        color('green')
        write(
            '¡Felicidades! ¡Ganaste!',
            font=('Arial', 18, 'bold')
        )

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 460, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
