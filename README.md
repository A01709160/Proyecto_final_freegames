# Proyecto\_final\_freegames

Proyecto colaborativo de modificación y mejora de videojuegos desarrollados en Python.

## Primer juego modificado: PACMAN

Modificado por: A01715004 - Tessa Heli Serrato Martínez

## Cambios realizados

### 1\. Cambiar el diseño del tablero

Se cambiaron los valores dentro de la variable "tiles", los 0 representan espacios donde no se puede caminar, mientras que los 1 representan un camino, así que para cambiar el diseño se cambiaron 0 por 1 y 1 por 0 para formar un patrón diferente al que se tenía antes.

### 2\. Cambiar la forma y color del alimento, pasó de ser un punto blanco a ser diamantes rosas.

Para hacer esto se creó una nueva función que dibuja diamantes rosas (alimento) y se mandó a llamar dentro de la función world donde se dibuja el tablero, se cambió el código después del if (tile == 1) para llamar la función nueva que se creó, en lugar de llamar a dot.

### 3\. Cambiar la velocidad de los fantasmas, ahora avanzan al doble de su velocidad, pasaron de avanzar 5 unidades a 10 unidades.

Se realizaron dos cambios en las variables: ghosts y en options, se cambió el valor de 5 o -5 que correspondía a la velocidad, en cada uno de los vectores por un 10 o -10 según correspondía.

## Segundo juego modificado: Tictactoe

Modificado por: A01709160 - Emilie García Peschaud

## Cambios realizados

### 1\. Personalización estética de símbolos

* Se asignó el color azul a la "X" y el color rojo a la "O".
* Se incrementó el grosor del trazo a 5px.
* Se ajustó el dibujado y centrado de las figuras dentro de las casillas.

### 2\. Validación de casillas ocupadas

* Se incorporó la estructura state\['occupied'] para registrar las jugadas y prevenir que los jugadores sobreescriban una casilla ocupada o pierdan su turno por clics accidentales.

### 3\. Lógica de victoria y empate

* Se definieron las combinaciones ganadoras (WIN\_COMBOS) ajustadas a las coordenadas devueltas por la función floor().
* Se implementó la función check\_win() para determinar automáticamente al ganador al completar una línea.
* Se agregó la detección de empate al completar 9 tiros sin ganador y se bloqueó el tablero al finalizar la partida utilizando onscreenclick(None).



# Tercer juego modificado: MEMORIA

Modificado por: A01708767 - Alonso Uribe López



## Cambios realizados



#### 1\. Contador de parejas descubiertas

Se agregó un contador que muestra la cantidad de parejas que el jugador ha encontrado, así como el total de parejas disponibles en el tablero. El contador se actualiza automáticamente cada vez que se descubre una pareja.



#### 2\. Detección de finalización del juego

Se implementó una condición para detectar cuándo se han encontrado todas las parejas. Al completar el tablero, aparece un mensaje de felicitación indicando que el jugador ha ganado y se bloquean los clics adicionales.



#### 3\. Modificación del tamaño del tablero

Se modificó el tamaño original del tablero de 8x8 a una cuadrícula de 4x4, reduciendo el número de casillas de 64 a 16 y estableciendo un total de 8 parejas.



#### 4\. Validación de clics fuera del tablero

Se agregó una validación para ignorar los clics realizados fuera de los límites del tablero, evitando errores al seleccionar posiciones que no corresponden a ninguna casilla.

