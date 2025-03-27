from .Nodo import Nodo
from .Grafo import root
from math import sqrt
import heapq
import random
def get_nodo(nodo:str) -> Nodo:
    head:Nodo = root
    while head:
        if head.informacion == nodo:
            return head
        head = head.get_siguiente_nodo()
    return None

def bfs(edoInicial:Nodo, edoFinal:Nodo):
    edoAbierto = [edoInicial]
    edoCerrado= []
    origen = {}
    actual = None
    while edoAbierto:
        actual = edoAbierto.pop(0)
        if actual == edoFinal:
            break
        
        hijo = actual.get_lista_adyacencia()
        while hijo:
            if not (hijo.get_nodo_adyacente() in edoAbierto or hijo.get_nodo_adyacente() in edoCerrado):
                edoAbierto.append(hijo.get_nodo_adyacente())
                origen[edoAbierto[-1].informacion] = actual.informacion
            hijo = hijo.get_siguiente_adyacente()
        edoCerrado.append(actual)
    
    if actual != edoFinal:
        return []
    
    camino = [actual.informacion]
    while(camino[-1] in origen):
        camino.append(origen[camino[-1]])
    return camino[::-1]

def dfs(edoInicial:Nodo, edoFinal:Nodo):
    edoAbierto = [edoInicial]
    edoCerrado= []
    origen = {}
    actual = None
    while edoAbierto:
        actual = edoAbierto.pop()
        if actual == edoFinal:
            break
        
        hijo = actual.get_lista_adyacencia()
        while hijo:
            if not (hijo.get_nodo_adyacente() in edoAbierto or hijo.get_nodo_adyacente() in edoCerrado):
                edoAbierto.append(hijo.get_nodo_adyacente())
                origen[edoAbierto[-1].informacion] = actual.informacion
            hijo = hijo.get_siguiente_adyacente()
        edoCerrado.append(actual)
    
    if actual != edoFinal:
        return []
    
    camino = [actual.informacion]
    while(camino[-1] in origen):
        camino.append(origen[camino[-1]])
    return camino[::-1]

def voraz(edoInicial:Nodo, edoFinal:Nodo):
    edoAbierto = [(edoInicial, heuristica(edoInicial, edoFinal))]
    edoCerrado= []
    origen = {}
    actual = None
    while edoAbierto:
        actual = edoAbierto.pop(0)
        edoCerrado.append(actual[0])

        if actual[0] == edoFinal:
            break

        hijo = actual[0].get_lista_adyacencia()
        while hijo:
            nodo_hijo = hijo.get_nodo_adyacente()
            if nodo_hijo not in [n[0] for n in edoAbierto] and nodo_hijo not in edoCerrado:
                heuristica_hijo = heuristica(nodo_hijo, edoFinal)
                edoAbierto.append((nodo_hijo, heuristica_hijo))
                origen[nodo_hijo.informacion] = actual[0].informacion
            hijo = hijo.get_siguiente_adyacente()
        edoAbierto.sort(key=lambda x: x[1])
    
    if not edoAbierto:
        return []
    
    camino = [actual[0].informacion]
    while(camino[-1] in origen):
        camino.append(origen[camino[-1]])
    return camino[::-1]

def dijkstra(edoInicial: Nodo, edoFinal: Nodo):
    edoAbierto = [(0, edoInicial)]
    edoCerrado = set()
    origen = {}
    costos = {edoInicial: 0}

    while edoAbierto:
        costo_actual, actual = heapq.heappop(edoAbierto)

        if actual in edoCerrado:
            continue

        edoCerrado.add(actual)

        if actual == edoFinal:
            break

        hijo = actual.get_lista_adyacencia()
        while hijo:
            nodo_hijo = hijo.get_nodo_adyacente()
            costo_hijo = costo_actual + hijo.peso

            if nodo_hijo not in edoCerrado and (nodo_hijo not in costos or costo_hijo < costos[nodo_hijo]):
                costos[nodo_hijo] = costo_hijo
                heapq.heappush(edoAbierto, (costo_hijo, nodo_hijo))
                origen[nodo_hijo] = actual

            hijo = hijo.get_siguiente_adyacente()

    if edoFinal not in origen:
        return []

    camino = [edoFinal]
    while camino[-1] in origen:
        camino.append(origen[camino[-1]])

    return [nodo.informacion for nodo in camino[::-1]]

def aEstrella(edoInicial: Nodo, edoFinal: Nodo):
    edoAbierto = [(0 + heuristica(edoInicial, edoFinal), 0, edoInicial)]
    heapq.heapify(edoAbierto)
    
    edoCerrado = set()
    origen = {}
    costos = {edoInicial: 0}

    while edoAbierto:
        _, costo_actual, actual = heapq.heappop(edoAbierto)

        if actual in edoCerrado:
            continue

        edoCerrado.add(actual)

        if actual == edoFinal:
            break

        hijo = actual.get_lista_adyacencia()
        while hijo:
            nodo_hijo = hijo.get_nodo_adyacente()
            costo_hijo = costo_actual + hijo.peso

            if nodo_hijo not in edoCerrado and (nodo_hijo not in costos or costo_hijo < costos[nodo_hijo]):
                costos[nodo_hijo] = costo_hijo
                f_n = costo_hijo + heuristica(nodo_hijo, edoFinal)
                heapq.heappush(edoAbierto, (f_n, costo_hijo, nodo_hijo))
                origen[nodo_hijo] = actual

            hijo = hijo.get_siguiente_adyacente()

    if edoFinal not in origen:
        return []

    camino = [edoFinal]
    while camino[-1] in origen:
        camino.append(origen[camino[-1]])

    return [nodo.informacion for nodo in camino[::-1]]


def hillClimbing(edoInicial: Nodo, edoFinal: Nodo):
    actual = edoInicial
    camino = [actual]

    while actual != edoFinal:
        hijo = actual.get_lista_adyacencia()
        mejor_hijo = None
        mejor_h = float('inf')

        while hijo:
            nodo_hijo = hijo.get_nodo_adyacente()
            h_n = heuristica(nodo_hijo, edoFinal)

            if h_n < mejor_h:
                mejor_h = h_n
                mejor_hijo = nodo_hijo

            hijo = hijo.get_siguiente_adyacente()

        if mejor_hijo is None or heuristica(edoInicial, edoFinal) <= mejor_h:
            break

        actual = mejor_hijo
        camino.append(actual)

    return [nodo.informacion for nodo in camino]

def heuristica(edoInicial:Nodo, edoFinal:Nodo):
    return sqrt((edoFinal.coords[0] - edoInicial.coords[0])**2 + (edoFinal.coords[1] - edoInicial.coords[1])**2)

def getTiempo(camino:list[str]):
    first = get_nodo(camino.pop(0))
    tiempo = 0
    while camino:
        la = first.get_lista_adyacencia()
        while la:
            if la.get_nodo_adyacente().informacion == camino[0]:
                tiempo += la.peso
                camino.pop(0)
                break
            la = la.get_siguiente_adyacente()
        if not la:
            return 0
        if first == la.get_nodo_adyacente():
            return 0
        first = la.get_nodo_adyacente()
    return tiempo
        