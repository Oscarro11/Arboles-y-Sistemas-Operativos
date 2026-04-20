from typing import List, Tuple, TypeVar

T = TypeVar("T")

class IBinaryTree[T]:

    # Inserta un elemento. True si se insertó y false si ya existe.
    def insertar (self, elemento: T) -> bool:
        pass

    # Elimina un elemento. True si se eliminó y false si no existe.
    def eliminar (self, elemento: T) -> bool:
        pass

    # Busca un elemento. Retorna si lo encontró y cuántas comparaciones hizo.
    def buscar (self, elemento: T) -> Tuple[bool, int]:
        pass
    
    # Verifica si el elemento es la raíz.
    def esRaiz (self, elemento: T) -> bool:
        pass
    
    # Verifica si el elemento es una hoja.
    def esHoja (self, elemento: T) -> bool:
        pass
    
    # Retorna una lista en órden.
    def inOrder(self) -> List[T]:
        pass