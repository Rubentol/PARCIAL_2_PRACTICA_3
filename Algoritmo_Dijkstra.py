#Practica #3 Algoritmo Dijkstra

# Definición del grafo como un diccionario de adyacencia
grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Función para el algoritmo de Dijkstra
def dijkstra(grafo, nodo_inicial):
    distancia = {nodo: float('infinity') for nodo in grafo}
    distancia[nodo_inicial] = 0
    visitados = set()

    while len(visitados) < len(grafo):
        nodo_actual = None
        min_distancia = float('infinity')
        for nodo, dist in distancia.items():
            if nodo not in visitados and dist < min_distancia:
                nodo_actual = nodo
                min_distancia = dist

        if nodo_actual is None:
            break

        visitados.add(nodo_actual)

        for vecino, peso in grafo[nodo_actual].items():
            if distancia[nodo_actual] + peso < distancia[vecino]:
                distancia[vecino] = distancia[nodo_actual] + peso

    return distancia

# Nodo inicial para iniciar el algoritmo de Dijkstra
nodo_inicial = 'A'

# Calcular distancias más cortas usando Dijkstra
distancias = dijkstra(grafo, nodo_inicial)

# Mostrar las distancias más cortas desde el nodo inicial
print("Distancias más cortas desde el nodo", nodo_inicial + ":")
for nodo, distancia in distancias.items():
    print(f'{nodo}: {distancia}')
