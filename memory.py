

"""Memory, juego de encontrar parejas de números.

Modificaciones:
1. Validar los clics fuera del tablero.
2. Contar y mostrar las parejas descubiertas.
3. Detectar cuando todas las parejas han sido descubiertas.
4. Reducir el tablero a una cuadrícula de 4x4.
"""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')

# Configuración del tablero.
filas = 4
columnas = 4
total_casillas = filas * columnas
total_parejas = total_casillas // 2
tamano_casilla = 50

tiles = list(range(total_parejas)) * 2
state = {'mark': None}
hide = [True] * total_casillas

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
        forward(tamano_casilla)
        left(90)
    end_fill()


def index(x, y):
    """Convierte las coordenadas (x, y) en el índice de una casilla."""
    columna = int((x + 100) // tamano_casilla)
    fila = int((y + 100) // tamano_casilla)
    return columna + fila * columnas


def xy(count):
    """Convierte el índice de una casilla en coordenadas (x, y)."""
    x = (count % columnas) * tamano_casilla - 100
    y = (count // columnas) * tamano_casilla - 100
    return x, y


def tap(x, y):
    """Actualiza la selección y las casillas descubiertas."""
    global parejas_encontradas, juego_terminado

    # Evita jugar después de encontrar todas las parejas.
    if juego_terminado:
        return

    # Ignora los clics que se realizan fuera del tablero.
    if not (-100 <= x < 100 and -100 <= y < 100):
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
        if parejas_encontradas == total_parejas:
            juego_terminado = True

    else:
        state['mark'] = spot


def draw():
    """Dibuja la imagen, las casillas y los mensajes."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(total_casillas):
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
    goto(-95, 120)
    color('black')
    write(
        f'Parejas encontradas: {parejas_encontradas} / {total_parejas}',
        font=('Arial', 12, 'normal')
    )

    # Muestra el mensaje cuando se completa el juego.
    if juego_terminado:
        goto(-110, -145)
        color('green')
        write(
            '¡Felicidades! ¡Ganaste!',
            font=('Arial', 18, 'bold')
        )

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(260, 300, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
