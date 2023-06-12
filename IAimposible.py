import pygame, sys #modulo pygame para interfaz y sys para poder actuar en el sistema (por ejemplo, cerrar la ventana)
import numpy as np #modulo que te permite crear una matriz
from random import choice #modulo para hacer elección random
from itertools import product #modulo para iterar en la matriz
import math #modulo que te permite usar elementos matematicos (en este programa se usa para que el minmax haga una comparacion de numeros maximos y minimos)


def dibujar_lineas(PANTALLA, COLORLINEAS, ANCHO_LINEAS):
    """
    dibuja las lineas del tablero en la pantalla 
    """
    #lineas horizontales
    pygame.draw.line(PANTALLA, COLORLINEAS, (0, 200), (600, 200), ANCHO_LINEAS)
    pygame.draw.line(PANTALLA, COLORLINEAS, (0, 400), (600, 400), ANCHO_LINEAS)
    #lineas verticales
    pygame.draw.line(PANTALLA, COLORLINEAS, (200, 0), (200, 600), ANCHO_LINEAS)
    pygame.draw.line(PANTALLA, COLORLINEAS, (400, 0), (400, 600), ANCHO_LINEAS)

def dibujos():
    """
    dibuja las figuras x y o 
    """
    for linea in range(DIMENSIONES):
        for column in range(DIMENSIONES): 
            if tablero_juego[linea][column] == 1:
                pygame.draw.circle(PANTALLA,COLOR_CIRCULO, (int(column * TAM_ESTANDAR + 100), int(linea * TAM_ESTANDAR + 100) ), RADIO, ANCHO_CIRCULO)
            elif tablero_juego[linea][column] == 2:
                pygame.draw.line(PANTALLA, COLOR_CRUZ, ((column * TAM_ESTANDAR  + ESPACIO), (linea * TAM_ESTANDAR +TAM_ESTANDAR - ESPACIO)), ((column * TAM_ESTANDAR + TAM_ESTANDAR - ESPACIO), (linea * TAM_ESTANDAR + ESPACIO)), 15)
                pygame.draw.line(PANTALLA, COLOR_CRUZ, ((column * TAM_ESTANDAR  + ESPACIO), (linea * TAM_ESTANDAR + ESPACIO)), ((column * TAM_ESTANDAR + TAM_ESTANDAR - ESPACIO), (linea * TAM_ESTANDAR +TAM_ESTANDAR - ESPACIO)),15)

def ganador(player):
    """
    comprueba si hay algún ganador en todas las posibles posiciones
    """
    # Comprobacion vertical
    for col_ver in range(DIMENSIONES):
        if tablero_juego[0][col_ver] == player and tablero_juego[1][col_ver] == player and tablero_juego[2][col_ver] == player:
            linea_vertical(col_ver, player)
            return True
    # Comprobacion Horizontal
    for linea in range(DIMENSIONES):
        if tablero_juego[linea][0] == player and tablero_juego[linea][1] == player and tablero_juego[linea][2] == player:
            linea_horizontal(linea, player)
            return True

    # Comprobacion Diagonal Ascendente
    if tablero_juego[2][0] == player and tablero_juego[1][1] == player and tablero_juego[0][2] == player:
        diag_Asc(player)
        return True

    # Comprobacion Diagonal Descendente
    if tablero_juego[0][0] == player and tablero_juego[1][1] == player and tablero_juego[2][2] == player:
        diag_Desc(player)
        return True

    return False #No gano nadie aún

def ganadorPosibilidades():
    """
    Hace una visión a futuro de las posibilidades de ganar tanto de la IA como del jugador
    """
    
    ganador = None
    
    for jugadorF in [1,2]:
        # Comprobacion vertical
        for col_ver in range(DIMENSIONES):
            if tablero_juego[0][col_ver] == jugadorF and tablero_juego[1][col_ver] == jugadorF and tablero_juego[2][col_ver] == jugadorF:
                return revisarJugador(jugadorF)
        # Comprobacion Horizontal
        for linea in range(DIMENSIONES):
            if tablero_juego[linea][0] == jugadorF and tablero_juego[linea][1] == jugadorF and tablero_juego[linea][2] == jugadorF:
                return revisarJugador(jugadorF)

        # Comprobacion Diagonal Ascendente
        if tablero_juego[2][0] == jugadorF and tablero_juego[1][1] == jugadorF and tablero_juego[0][2] == jugadorF:
            return revisarJugador(jugadorF)

        # Comprobacion Diagonal Descendente
        if tablero_juego[0][0] == jugadorF and tablero_juego[1][1] == jugadorF and tablero_juego[2][2] == jugadorF:
            return revisarJugador(jugadorF)

    return "TIE" if not 0 in tablero_juego else ganador #No gano nadie

def revisarJugador(jugador): 
    """
    Revisa el jugador que hay en la casilla para la visión de la función ganadorPosibilidades
    """
    return "O" if jugador == 1 else "X"

def linea_vertical(col_ver, player):
    """
    Dibuja una línea vertical cuando gana alguien
    """
    posX = col_ver * TAM_ESTANDAR + TAM_ESTANDAR//2
    
    if player == 1:
        color = COLOR_CIRCULO
    
    elif player == 2:
        color = COLOR_CRUZ
        
    pygame.draw.line( PANTALLA, color, (posX, 15), (posX, ALTO - 15), ANCHO_LINEAS)

def linea_horizontal(linea, player):
    """
    Dibuja una línea horizontal cuando gana alguien
    """
    posY = linea * TAM_ESTANDAR + TAM_ESTANDAR//2
    
    if player == 1:
        color = COLOR_CIRCULO
    elif player == 2:
        color = COLOR_CRUZ
    
    pygame.draw.line(PANTALLA, color, (15, posY), (ANCHO - 15, posY), ANCHO_LINEAS)

def diag_Asc(player):
    """
    Dibuja la línea de la diagonal ascendente cuando gana alguien
    """
    if player == 1:
        color = COLOR_CIRCULO
    elif player == 2:
        color = COLOR_CRUZ
    
    pygame.draw.line(PANTALLA, color, (15, ALTO - 15), (ANCHO - 15, 15), ANCHO_LINEAS)

def diag_Desc(player):
    """
    Dibuja la línea de la diagonal descendente cuando gana alguien
    """
    if player == 1:
        color = COLOR_CIRCULO
    elif player == 2:
        color = COLOR_CRUZ
    
    pygame.draw.line(PANTALLA, color, (15, 15), (ANCHO - 15, ALTO - 15), ANCHO_LINEAS)

def reset():
    """
    Resetea el tablero
    """
    PANTALLA.fill(COLORFONDO)
    dibujar_lineas(PANTALLA, COLORLINEAS, ANCHO_LINEAS)

    for linea in range(DIMENSIONES):
        for columna in range(DIMENSIONES):
            tablero_juego[linea][columna] = 0

def marcar_x(linea, columna, jugador):
    """
    Marcar/Dibuja la x u o en el tablero
    """
    tablero_juego[linea][columna] = jugador
    
def espacio_libre(linea, columna):
    """
    Verificar si el espacio seleciona esta disponible
    """
    return tablero_juego[linea][columna] == 0

def minimax(tablero_juego, profundidad, esMaximo):
    """
    valora todas las posibilidades con un arbol de decisiones de ganar o perder y devuelve mejorPuntuación
    """
    resultado = ganadorPosibilidades()
    if resultado != None:
        return valores.get(resultado)
    if profundidad == 0: 
        # Forzar la jugada en el centro
        tablero_juego[1][1] = player
        puntuacion = minimax(tablero_juego, profundidad +1, False)
        tablero_juego[1][1] = 0
        return puntuacion
        
    if esMaximo:
        mejorPuntuacion = -math.inf       
        for linea in range(DIMENSIONES):
            for columna in range(DIMENSIONES):
                if espacio_libre (linea, columna):
                    tablero_juego[linea][columna] = player
                    puntuacion = minimax(tablero_juego, profundidad +1, False)             
                    tablero_juego[linea][columna] = 0
                    mejorPuntuacion = max(puntuacion, mejorPuntuacion)
        return mejorPuntuacion
    else:
        mejorPuntuacion = math.inf       
        for linea in range(DIMENSIONES):
            for columna in range(DIMENSIONES):
                if espacio_libre (linea, columna):
                    tablero_juego[linea][columna] = player %2 +1
                    puntuacion = minimax(tablero_juego, profundidad +1, True)             
                    tablero_juego[linea][columna] = 0
                    mejorPuntuacion = min(puntuacion, mejorPuntuacion)
        return mejorPuntuacion

def elegirValores(siguienteJugador):
    """
    elige los valores de las fichas
    """
    xGanador = {"X":1, "O":-1, "TIE":0}
    oGanador ={"X":-1, "O":1, "TIE":0}
    if siguienteJugador:
        return xGanador
    else:
        return oGanador
   
def tablero():
    """
    Dibuja todo el tablero y abre la pantalla de juego
    """
    # Inicializar objetos
    pygame.init()
    global tablero_juego
    global PANTALLA
    global color_dibujos
    global RADIO
    global ANCHO_CIRCULO
    global ESPACIO
    global COLOR_CIRCULO
    global COLOR_CRUZ
    global DIMENSIONES
    global TAM_ESTANDAR
    global ANCHO
    global ALTO
    global ANCHO_LINEAS
    global COLORFONDO
    global COLORLINEAS
    global COLOR_LINEAS

    # Seteo de texto en la ventana.
    pygame.display.set_caption("TRES EN RAYA")
    #Declaracion de constantes
    ANCHO = 600 
    ALTO = 600
    TAM_ESTANDAR = 200
    COLORFONDO = (28, 170, 156) # Se declara en rgb
    COLORLINEAS = (255, 0,0)
    ANCHO_LINEAS = 15
    color_dibujos = (220, 119, 215)
    RADIO = 60
    ANCHO_CIRCULO = 15
    COLOR_CIRCULO = (87, 218, 38)
    COLOR_CRUZ = (228, 57, 20)
    ESPACIO = 55
    # Seteo y aplicacion de los tamaños de la ventana
    PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
    # Relleno de colores
    PANTALLA.fill(COLORFONDO)
    dibujar_lineas(PANTALLA, COLORLINEAS, ANCHO_LINEAS)
    
    DIMENSIONES = 3
    tablero_juego = np.zeros((DIMENSIONES,DIMENSIONES)) #crea una matriz 3x3

def comenzarIAimposible():
    """
    Se inicia el modo de juego IA imposible
    """
    #valores iniciales 
    tablero()
    global valores
    global player
    siguienteJugador = choice([True, False]) #elige de forma aleatoria quien comienza
    player = 1
    finalizar_Juego = False
    valores = elegirValores(siguienteJugador) #se reinician los valores
    primeraJugada = True
    profundidad = 0
    while True: #bandera de inicio
        for evento in pygame.event.get(): #itera sobre todos los eventos que suceden en la pantalla
            if evento.type == pygame.QUIT: #cierra la ventana solo si el jugador lo ejecuta
                sys.exit()

            if siguienteJugador: #turno de jugador
                if evento.type == pygame.MOUSEBUTTONDOWN and not finalizar_Juego: #recoge el click del jugador
                    #cogemos el int del jugador
                    mouseX = evento.pos[0] #se guarda la posición del click del jugador en el eje X
                    mouseY =  evento.pos[1] #se guarda la posición del click del jugador en el eje Y

                    linea_click = int(mouseY // 200) #ajusta el click del eje Y para que de valores enteros del 0 al 2 (para iterar en la matriz)
                    columna_click = int(mouseX // 200) #ajusta el click del eje X para que de valores enteros del 0 al 2 (para iterar en la matriz)
                    if espacio_libre (linea_click, columna_click):
                        marcar_x(linea_click, columna_click, player) 
                        dibujos()
                        if ganador(player):
                            finalizar_Juego = True #el juego termina si hay ganador
                            
                        elif not 0 in tablero_juego: #verifica que el tablero esté completo (de esa manera habría empate) y aparece una pantalla para reiniciar el juego
                            font = pygame.font.Font('freesansbold.ttf', 32)
                            white = (255, 255, 255)
                            black = (0, 0, 0)
                            blue = (0, 0, 128)
                            text = font.render('¡Has terminado en Tablas!', True, black, white)
                            text2 = font.render('¡Presiona R para reintentar!', True, black, white)
                            textRect = text.get_rect()
                            textRect2 = text2.get_rect()
                            textRect.center = (ANCHO // 2, (ALTO // 2) + 20)
                            textRect2.center = (ANCHO // 2, (ALTO // 2) - 20)
                            PANTALLA.fill(white)
                            PANTALLA.blit(text, textRect)
                            PANTALLA.blit(text2, textRect2)
                            primeraJugada = True
                        player = player % 2 + 1 #cambia el numero del jugador
                        siguienteJugador = False #cambia el turno
                      
            else:
                if not finalizar_Juego: # finalizar juego es True, ya no entra
                    if primeraJugada == True and espacio_libre(1, 1) and profundidad == 0: #pone la casilla en el centro si empieza ella
                        marcar_x(1, 1, player)
                        dibujos()
                        primeraJugada = False
                        profundidad += 1
                    elif primeraJugada == True and profundidad > 0: #actúa el algoritmo minimax en la primera jugada
                        mejorPuntuacion = -math.inf
                        for linea in range(DIMENSIONES): #itera sobre el eje Y
                            for columna in range(DIMENSIONES): #itera sobre el eje X
                                if espacio_libre (linea, columna):
                                    marcar_x(linea, columna, player)
                                    puntuacion = minimax(tablero_juego, profundidad +1, False) #guada la puntuación que devuelve el minimax
                                    
                                    marcar_x(linea, columna, 0)
                                    if puntuacion > mejorPuntuacion: #guarda el mejor movimiento
                                        mejorPuntuacion = puntuacion
                                        movimiento = (linea, columna)
                    
                    else: #actúa el algoritmo minimax si la primera jugada fue del jugador
                        mejorPuntuacion = -math.inf
                        for linea in range(DIMENSIONES):
                            for columna in range(DIMENSIONES):
                                if espacio_libre (linea, columna):
                                    marcar_x(linea, columna, player)
                                    puntuacion = minimax(tablero_juego, profundidad +1, False)
                                    
                                    marcar_x(linea, columna, 0)
                                    if puntuacion > mejorPuntuacion:
                                        mejorPuntuacion = puntuacion
                                        movimiento = (linea, columna)
                        
                        #dibuja el mejor movimiento
                        i = movimiento[0]
                        j = movimiento[1]
                        marcar_x(i, j, player)
                        dibujos()

                    if ganador(player): #comprueba si hay ganadores en el turno de la IA
                        finalizar_Juego = True
                    elif not 0 in tablero_juego and not finalizar_Juego: #verifica que el tablero esté completo (de esa manera habría empate) y aparece una pantalla para reiniciar el juego
                        font = pygame.font.Font('freesansbold.ttf', 32)
                        white = (255, 255, 255)
                        black = (0, 0, 0)
                        blue = (0, 0, 128)
                        text = font.render('¡Has terminado en Tablas!', True, black, white)
                        text2 = font.render('¡Presiona R para reintentar!', True, black, white)
                        textRect = text.get_rect()
                        textRect2 = text2.get_rect()
                        textRect.center = (ANCHO // 2, (ALTO // 2) + 20)
                        textRect2.center = (ANCHO // 2, (ALTO // 2) - 20)
                        PANTALLA.fill(white)
                        PANTALLA.blit(text, textRect)
                        PANTALLA.blit(text2, textRect2)
                        primeraJugada = True
                    player = player % 2 + 1
                    siguienteJugador = True

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r: #recoge el input si el jugador pulsa la tecla R y se resetea el juego
                    reset()
                    player = 1
                    finalizar_Juego = False
 
        pygame.display.update() #actualiza la pantalla
        
if __name__ == '__main__': #se ejecuta la funcion comenzarIAimposible como main
    comenzarIAimposible()


