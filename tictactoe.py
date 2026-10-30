"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""

from turtle import *

from freegames import line

# Combinaciones posibles de coordenadas (x, y) en el tablero necesarias para ganar
WIN_COMBOS = [
    # Horizontales
    [(-200, 66), (-67, 66), (66, 66)],
    [(-200, -67), (-67, -67), (66, -67)],
    [(-200, -200), (-67, -200), (66, -200)],
    # Verticales
    [(-200, 66), (-200, -67), (-200, -200)],
    [(-67, 66), (-67, -67), (-67, -200)],
    [(66, 66), (66, -67), (66, -200)],
    # Diagonales
    [(-200, 66), (-67, -67), (66, -200)],
    [(-200, -200), (-67, -67), (66, 66)],
]


# Dibujar el tablero de juego 3x3.
def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)

# Dibujar el símbolo X con color azul y grosor de 5px
def drawx(x, y):
    """Draw X player."""
    color('blue')
    width(5)
    line(x + 20, y + 20, x + 113, y + 113)
    line(x + 20, y + 113, x + 113, y + 20)

# Dibujar el símbolo O con color rojo y grosor de 5px
def drawo(x, y):
    """Draw O player."""
    color('red')
    width(5)
    up()
    goto(x + 67, y + 15)
    down()
    circle(52)

# Redondear la coordenada al centro de la casilla correspondiente
def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200

# Agregar registro de casillas en state
state = {'player': 0, 'occupied':{}}
players = [drawx, drawo]

# Verificar si el jugador activo completó alguna combinación ganadora.
def check_win(player):
    for combo in WIN_COMBOS:
        if all(
            state['occupied'].get(pos) == player for pos in combo
        ):
            return True
    return False

# Manejar los clics en el tablero, validar jugadas y revisar estado del juego
def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)

# Prevenir sobreescritura si la casilla ya fue jugada
    if (x, y) in state ['occupied']:
        return
    
# Registrar tiro y dibujar figura del jugador actual
    player = state['player']
    state['occupied'][(x, y)] = player

    draw = players[player]
    draw(x, y)
    update()

# Evaluar victoria del jugador actual
    if check_win(player):
        symbol = 'X' if player == 0 else 'O'
        print(f"¡El jugador {symbol} ha ganado!")
        return
    
# Evaluar empate si las 9 casillas están llenas
    if len(state['occupied']) == 9:
        print("¡Es un empate!")
        onscreenclick(None)  # Bloquea mas clics
        return

# Alternar turno entre 0 (X) y 1 (O)
    state['player'] = not player

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
