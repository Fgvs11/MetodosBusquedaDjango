from .Nodo import Nodo
# from .Metodos import Metodos

nodos = [
    ('A', (1091, 502)), ('B', (999, 445)), ('C', (931, 513)), ('D', (934, 431)),
    ('E', (880, 412)), ('F', (847, 494)), ('G', (829, 425)), ('H', (764, 386)),
    ('I', (767, 501)), ('J', (717, 515)), ('K', (796, 346)), ('L', (676, 424)),
    ('M', (656, 355)), ('N', (599, 346)), ('Ñ', (597, 484)), ('O', (579, 409)),
    ('P', (606, 538)), ('Q', (524, 439)), ('R', (459, 460)), ('S', (437, 528)),
    ('T', (394, 463)), ('U', (402, 402)), ('V', (327, 518)), ('W', (227, 462)),
    ('X', (162, 531)), ('Y', (198, 422)), ('Z', (158, 343)), ('T1', (277, 391)),
    ('T2', (385, 357)), ('CC', (242, 525)), ('FF', (662, 526)), ('Cn1', (59, 406)),
    ('Cn2', (298, 454)), ('Et1', (1085, 559)), ('Et2', (846, 559)), ('Et3', (715, 573)),
    ('Et4', (304, 569)), ('Et5', (132, 469)), ('Et6', (108, 410))
]


li : dict[Nodo] = {}
for i in range(len(nodos)-1, -1, -1):
    nodo = nodos[i][0]
    li[nodo]= Nodo(informacion=nodos[i][0], coords=nodos[i][1])
    if i != len(nodos)-1:
        li[nodo].set_siguiente_nodo(li[nodos[i+1][0]])

#Listas de adyacencia
listas : dict[list[tuple]] = {
    "A": [("Et1",56.1),("C",256.7),("B",238)],
    "B": [("D",86.7),("C",158.1),("A",238)],
    "C": [("Et2",139.5),("Et1",273.7),("F",159.8),("E",187),("D",90.1),("B", 256.7),("A",256.7)],
    "D": [("E",102),("C",90.1),("B",86.7)],
    "E": [("G",51),("F",156.4),("C",187)],
    "F": [("Et2",102),("I",278.8),("G",98.6),("E",156.4),("C",159.8)],
    "G": [("I",272),("H",139.4),("F",98.6),("E",51)],
    "H": [("L",136),("K",159.8),("I",278.8),("G",139.4)],
    "I": [("Et3",139.4),("J",37.4),("H",278.8),("F",278.8)],
    "J": [("Et3",98.6),("FF",185.3),("L",153),("I",37.4)],
    "K": [("M",45.9),("L",153),("H",159.8)],
    "L": [("FF",154.7),("O",124.1),("Ñ",168.3),("M",132.6),("K",153),("J", 153),("H",136)],
    "M": [("N",45.9),("L",132.6),("K",159.8)],
    "N": [("O",144.5),("M",45.9)],
    "Ñ": [("S",319.6),("Q",202.3),("P",91.8),("O",88.4),("L",168.3)],
    "O": [("U",448.8),("Q",170),("Ñ",88.4),("N",144.5),("L",124.1)],
    "P": [("FF",57.8),("S",326.4),("Ñ",91.8)],
    "Q": [("U",260.1),("R",93.5),("O",170),("Ñ",202.3)],
    "R": [("U",255),("T",122.4),("S",86.7),("Q",93.5)],
    "S": [("Et4",309.4),("V",192.1),("R",86.7),("P",326.4),("Ñ",319.6)],
    "T": [("Cn2",134.3),("V",219.3),("U",221),("R",122.4)],
    "U": [("Cn2",212.5),("T2",25.5),("T1",198.9),("T",221),("R",255),("Q",260.1),("O",448.8)],
    "V": [("Et4",105.4),("Cn2",71.4),("CC",234.6),("T",219.3),("S",192.1)],
    "W": [("Cn2",188.7),("CC",54.4),("T1",154.7),("Y",11.9),("X",130.9)],
    "X": [("Et5",113.9),("Et4",207.4),("CC",103.7),("W",130.9)],
    "Y": [("Et6",127.5),("Et5",90.1),("Z",241.4),("W",11.9)],
    "Z": [("Et6",98.6),("Y",241.4)],
    "T1": [("Cn2",54.4),("W",154.7),("U",198.9)],
    "T2": [("U",25.5)],
    "CC": [("Et4",134.3),("X",103.7),("W",54.5),("V",234.6)],
    "FF": [("Et3",91.8),("P",57.8),("L",154.7),("J",185.3)],
    "Cn1": [("Et6",40.8)],
    "Cn2": [("T1",54.4),("W",188.7),("V",71.4),("U",212.5),("T",134.3)],
    "Et1": [("C",161),("A",56.1)],
    "Et2": [("Et3",204),("F",51),("C",139.5)],
    "Et3": [("Et2",204),("FF",91.8),("J",98.6),("I",139.4)],
    "Et4": [("CC",134.3),("X",207.4),("V",105.4),("S",309.4)],
    "Et5": [("Et6",78.2),("X",90.1),("Y",113.9)],
    "Et6": [("Et5",78.2),("Cn1",40.8),("Z",98.6),("Y",127.5)],
}

for nodo,listaAdyacencia in listas.items():
    anterior:Nodo = None
    for na in listaAdyacencia:
        siguiente:Nodo = Nodo(peso=na[1])
        siguiente.set_nodo_adyacente(li[na[0]])
        siguiente.set_siguiente_adyacente(anterior)
        anterior = siguiente
    li[nodo].set_lista_adyacencia(anterior)

root = li["A"]
if __name__ == '__main__':
    head:Nodo = [li["B"]]
    nodo1 = li["V"]
    nodo2 = li["L"]
    # print(nodo1.coords)
    # print(Metodos.bfs(nodo1,nodo2))
    # print(Metodos.dfs(nodo1,nodo2))
    # print(Metodos.get_nodo('Et2'))
    
    # while head:
    #     print(head)
    #     print()
    #     # la = head.get_lista_adyacencia()
    #     # if la:
    #     #     print(la)
    #     head = head.get_siguiente_nodo()


