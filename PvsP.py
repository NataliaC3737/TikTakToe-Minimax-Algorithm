import pygame, sys #modulo pygame para interfaz y sys para poder actuar en el sistema (por ejemplo, cerrar la ventana)
import numpy as np #modulo que te permite crear una matriz


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
    
    return False # Porque no gano nadie

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
    tablero_juego[linea, columna] = jugador
    
def espacio_libre(linea, columna):
    """
    Verificar si el espacio seleciona esta disponible
    """
    if tablero_juego[linea][columna] == 0:
        return True
    else:
        return False    
    
def tablero():
    """
    Dibuja todo el tablero y abre la pantalla de juego
    """
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

def iniciarPvsP():
    """
    Se inicia el modo de juego Player vs Player
    """
    tablero()

    player = 1
    finalizar_Juego = False
    while True: #bandera de inicio
        for evento in pygame.event.get(): #itera sobre todos los eventos que suceden en la pantalla
            if evento.type == pygame.QUIT: #cierra la ventana solo si el jugador lo ejecuta
                sys.exit()
            
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
                    player = player % 2 + 1 #cambio de jugador y de turno      
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r: #recoge el input si el jugador pulsa la tecla R y se resetea el juego
                    reset()
                    player = 1
                    finalizar_Juego = False
        pygame.display.update() #actualiza la pantalla

if __name__ == '__main__':  #se ejecuta la funcion comenzarIAaleatoria como main
    iniciarPvsP()


