# Proyecto_final_freegames
Proyecto colaborativo de modificación y mejora de videojuegos desarrollados en Python.

## Primer juego modificado: PACMAN
Modificado por: A01715004 - Tessa Heli Serrato Martínez

Cambios realizados:
  1. Cambiar el diseño del tablero:
      Se cambiaron los valores dentro de la variable "tiles", los 0 representan espacios donde no se puede caminar, mientras que los 1 representan un camino, así que para cambiar el diseño se cambiaron 0 por 1 y 1 por 0 para formar un patrón diferente al que se tenía antes.
     
  2. Cambiar la forma y color del alimento, pasó de ser un punto blanco a ser diamantes rosas.
     Para hacer esto se creó una nueva función que dibuja diamantes rosas (alimento) y se mandó a llamar dentro de la función world donde se dibuja el tablero, se cambió el código después del if (tile == 1) para llamar la función nueva que se creó, en lugar de llamar a dot. 
     
  3. Cambiar la velocidad de los fantasmas, ahora avanzan al doble de su velocidad, pasaron de avanzar 5 unidades a 10 unidades.
     Se realizaron dos cambios en las variables: ghosts y en options, se cambió el valor de 5 o -5 que correspondía a la velocidad, en cada uno de los vectores por un 10 o -10 según correspondía.
