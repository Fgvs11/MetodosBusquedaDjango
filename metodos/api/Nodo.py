from colorama import Fore, Style
class Nodo():
    def __init__(self, informacion: str = None, peso: int = None, heuristica: float = None, first = None, second = None, coords: tuple[int] = None) -> None:
        self.informacion:str = informacion
        self.peso: float = peso
        self.heuristica:float = heuristica
        self.coords : tuple[int] = coords
        self.__first: Nodo = first
        self.__second : Nodo = second
    
    def get_siguiente_nodo(self):
        return self.__first
    
    def set_siguiente_nodo(self, nodo)-> None:
        self.__first = nodo

    def get_lista_adyacencia(self):
        return self.__second
    
    def set_lista_adyacencia(self, lista)-> None:
        self.__second = lista

    def get_nodo_adyacente(self):
        return self.__first
    
    def set_nodo_adyacente(self, nodo)-> None:
        self.__first = nodo

    def get_siguiente_adyacente(self):
        return self.__second
    
    def set_siguiente_adyacente(self, lista)-> None:
        self.__second = lista

    def __str__(self):
        if self.informacion:
            # Nodo principal
            resultado = f"{Fore.GREEN}{'Nodo: ' + self.informacion:^27}{Style.RESET_ALL}\n"
            resultado += "=" * 27 + "\n"

            # Cabecera de la tabla
            resultado += f"| {'Adyacente':<12} | {'Peso':<8} |\n"
            resultado += "-" * 27 + "\n"

            # Recorrer la lista de adyacencia
            nodo = self.get_lista_adyacencia()
            if nodo:
                while nodo:
                    resultado += f"| {nodo.get_nodo_adyacente().informacion:<12} | {nodo.peso:<8} |\n"
                    nodo = nodo.get_siguiente_adyacente()
            else:
                resultado += "|    Sin    adyacencias   |\n"

            resultado += "=" * 27
            return resultado
        else:
            return "Nodo sin información"
    
    def __lt__(self, otro):
        return self.informacion < otro.informacion  # Comparación por información o ID del nodo
    
    # # Métodos de comparación y hash para sets
    # def __eq__(self, other):
    #     if isinstance(other, Nodo):
    #         return self.informacion == other.informacion
    #     return False
    
    # def __hash__(self):
    #     return hash(self.informacion)