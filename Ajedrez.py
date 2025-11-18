import os

def crear_tablero_inicial():
    """
    Crea el tablero de ajedrez inicial con caracteres Unicode.
    Devuelve una lista de listas (matriz 8x8).
    """
    
    fila_0 = ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜']
    fila_1 = ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟']
    
    
    filas_vacias = [[' ' for _ in range(8)] for _ in range(4)]
    
    fila_6 = ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙']
    fila_7 = ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']

    tablero = [fila_0, fila_1] + filas_vacias + [fila_6, fila_7]
    return tablero

def guardar_tablero(nombre_fichero, tablero, modo='a'):
    """
    Guarda el tablero actual en el fichero especificado.
    Las columnas se separan por tabuladores y las filas por saltos de línea.
    
    modo: 'w' para sobrescribir (inicio), 'a' para añadir (movimientos).
    """
    with open(nombre_fichero, modo, encoding='utf-8') as f:
        for fila in tablero:
            linea = '\t'.join(fila)
            f.write(linea + '\n')

def mover_pieza(tablero, f_origen, c_origen, f_destino, c_destino):
    """
    Mueve una pieza en el tablero (matriz).
    No valida reglas de ajedrez, solo mueve de A a B.
    """
    pieza = tablero[f_origen][c_origen]
    tablero[f_destino][c_destino] = pieza
    tablero[f_origen][c_origen] = ' ' 
    return tablero

def leer_movimiento(nombre_fichero, n_movimiento):
    """
    Lee el fichero y extrae el tablero correspondiente al número de movimiento.
    Asumimos que cada tablero ocupa 8 líneas.
    """
    lineas_totales = []
    try:
        with open(nombre_fichero, 'r', encoding='utf-8') as f:
            lineas_totales = f.readlines()
    except FileNotFoundError:
        return None

   
    inicio = n_movimiento * 8
    fin = inicio + 8

    if inicio >= len(lineas_totales):
        return [] 

    return lineas_totales[inicio:fin]

def main():
    print("--- GENERADOR DE PARTIDAS DE AJEDREZ ---")
    nombre_fichero = input("Introduce el nombre del fichero para guardar la partida (ej: partida.txt): ")
    
    tablero = crear_tablero_inicial()
    guardar_tablero(nombre_fichero, tablero, modo='w') 
    print("Tablero inicial guardado.")

    
    contador_movimientos = 0
    while True:
        opcion = input("\n¿Quieres hacer un movimiento (s) o terminar (n)? ").lower()
        if opcion != 's':
            break
        
        try:
            print(f"--- Movimiento {contador_movimientos + 1} ---")
            print("Introduce coordenadas (0-7). Fila 0 es arriba (negras), Fila 7 abajo (blancas).")
            fo = int(input("Fila origen: "))
            co = int(input("Columna origen: "))
            fd = int(input("Fila destino: "))
            cd = int(input("Columna destino: "))

            
            tablero = mover_pieza(tablero, fo, co, fd, cd)
            
            
            guardar_tablero(nombre_fichero, tablero, modo='a')
            contador_movimientos += 1
            print("Movimiento registrado.")
            
        except (ValueError, IndexError):
            print("Error: Coordenadas inválidas. Inténtalo de nuevo.")

    
    print("\n--- REVISOR DE PARTIDA ---")
    while True:
        try:
            entrada = input(f"Introduce el número de movimiento a visualizar (0 a {contador_movimientos}, o 'x' para salir): ")
            if entrada.lower() == 'x':
                break
            
            n_mov = int(entrada)
            lineas_tablero = leer_movimiento(nombre_fichero, n_mov)

            if lineas_tablero is None:
                print("Error: No se encuentra el fichero.")
                break
            elif not lineas_tablero:
                print("Ese movimiento no existe en el fichero.")
            else:
                print(f"\nTablero en movimiento {n_mov}:")
                print("-" * 20)
        
                for linea in lineas_tablero:
                    print(linea.strip())
                print("-" * 20)

        except ValueError:
            print("Por favor, introduce un número válido.")

if __name__ == "__main__":
    main()