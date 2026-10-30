"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""

from turtle import *

from freegames import line

# Combinaciones posibles de coordenadas (x, y) en el tablero
WIN_COMBOS = [
    # Horizontales
    [(-200, 67), (-67, 67), (67, 67)],
    [(-200, -67), (-67, -67), (67, -67)],
    [(-200, -200), (-67, -200), (67, -200)],
    # Verticales
    [(-200, 67), (-200, -67), (-200, -200)],
    [(-67, 67), (-67, -67), (-67, -200)],
    [(67, 67), (67, -67), (67, -200)],
    # Diagonales
    [(-200, 67), (-67, -67), (67, -200)],
    [(-200, -200), (-67, -67), (67, 67)],
]


def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Draw X player."""
    color('blue')
    width(5)
    line(x + 20, y + 20, x + 113, y + 113)
    line(x + 20, y + 113, x + 113, y + 20)

def drawo(x, y):
    """Draw O player."""
    color('red')
    width(5)
    up()
    goto(x + 67, y + 15)
    down()
    circle(52)


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200

#Agregar registro de casillas en state
state = {'player': 0, 'occupied':{}}
players = [drawx, drawo]


def check_win(player):
    """Verificar si el jugador actual completó una línea."""
    for combo in WIN_COMBOS:
        if all(
            state['occupied'].get(pos) == player for pos in combo
        ):
            return True
    return False


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)

    #Validar si la casilla ya esta ocupada
    if (x, y) in state ['occupied']:
        return

    player = state['player']
    state['occupied'][(x, y)] = player

    draw = players[player]
    draw(x, y)
    update()

    # Validar si el jugador actual ganó
    if check_win(player):
        symbol = 'X' if player == 0 else 'O'
        print(f"¡El jugador {symbol} ha ganado!")
        return


    state['player'] = not player

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
