from PvsP import iniciarPvsP #modularizacion para importar modo de juego de Player vs Player
from IAAleatoria import comenzarIAaleatoria #modularizacion para importar modo de juego de IA aleatoria
from IAimposible import comenzarIAimposible #modularizacion para importar modo de juego de IA imposible
from random import choice #modulo para hacer elección random

def main():
    """
    menú de selección de jugadores
    """
    print("")
    print("")
    print("Bienvenido al juego del Tres En Raya")

    
    while True:
        opcion = input("Selecciona un modo de Juego:\nPlayer vs Player -> 1\nPlayer vs IA Aleatoria -> 2\nPlayer vs IA Imposible -> 3\n")

        try:
            opcion = int(opcion)
        except ValueError:
            print("Porfavor, introduce un número del 1 al 3.")

        if opcion == 1:
            print("Elegiste el modo de juego: Player vs Player")

            jugador1 = input("Jugador 1\nIntroduce Tu Nombre: ")
            jugador2 = input("Jugador 2\nIntroduce Tu Nombre: ")
            players = [jugador1, jugador2]
            jugadorSeleccionado = choice(players)
            print(f"El jugador {jugadorSeleccionado} inicia con Circulo")
        
            iniciarPvsP()

        elif opcion == 2:
            print("Elegiste el modo de juego: Player vs IA Aleatoria")

            comenzarIAaleatoria()
        
        elif opcion == 3: 
            print("Elegiste el modo de juego: Player vs IA Imposible")

            comenzarIAimposible()
        
    
    
if __name__ == '__main__':
    main()


