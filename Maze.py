import collections

def crear_laberinto(dimension, muros):
    """
    Crea una matriz (lista de listas) representando el laberinto.
    ' ' = Espacio libre
    'X' = Muro
    'S' = Salida (en la última celda)
    """
    
    tablero = [[' ' for _ in range(dimension)] for _ in range(dimension)]
    
    
    for coordenadas in muros:
        fila, col = coordenadas
        if 0 <= fila < dimension and 0 <= col < dimension:
            tablero[fila][col] = 'X'
            
    
    tablero[dimension-1][dimension-1] = 'S'
    
    return tablero

def resolver_laberinto(tablero):
    """
    Encuentra la ruta desde (0,0) hasta la 'S' usando BFS (Búsqueda en Anchura)
    para garantizar el camino más corto.
    """
    dimension = len(tablero)
    inicio = (0, 0)
    meta_simbolo = 'S'
    
    
    cola = collections.deque([ (inicio[0], inicio[1], []) ])
    
    
    visitados = set()
    visitados.add(inicio)
    
    
    direcciones = [
        (1, 0, 'Abajo'),
        (0, 1, 'Derecha'),
        (-1, 0, 'Arriba'),
        (0, -1, 'Izquierda')
    ]
    
    while cola:
        f, c, camino = cola.popleft()
        
        
        if tablero[f][c] == meta_simbolo:
            return camino
        
        
        for df, dc, movimiento in direcciones:
            nf, nc = f + df, c + dc
            
            
            if 0 <= nf < dimension and 0 <= nc < dimension:
                
                if tablero[nf][nc] != 'X' and (nf, nc) not in visitados:
                    visitados.add((nf, nc))
                    
                    nueva_ruta = camino + [movimiento]
                    cola.append((nf, nc, nueva_ruta))
                    
    return None 

def main():
    
    DIMENSION = 5
    
    
    muros = (
        (0,1), (0,2), (0,3), (0,4),
        (1,1),
        (2,1), (2,3),
        (3,3),
        (4,0), (4,1), (4,2), (4,3)
    )
    
    
    laberinto = crear_laberinto(DIMENSION, muros)
    
    print("--- LABERINTO GENERADO ---")
    for fila in laberinto:
        print(fila)
    
    
    ruta = resolver_laberinto(laberinto)
    
    print("\n--- SOLUCIÓN ---")
    if ruta:
        print("Secuencia de movimientos encontrada:")
        print(ruta)
    else:
        print("No hay camino posible desde la entrada a la salida.")

if __name__ == "__main__":
    main()