from typing import List, Tuple, Generic
from abc import ABC, abstractmethod

from .types import T

class IBinaryTree(Generic[T], ABC):

    # Inserta un elemento. True si se inserto y false si ya existe.
    @abstractmethod
    def insertar (self, elemento: T) -> bool:
        pass

    # Elimina un elemento. True si se elimino y false si no existe.
    @abstractmethod
    def eliminar (self, elemento: T) -> bool:
        pass

    # Busca un elemento. Retorna si lo encontro y cuantas comparaciones hizo.
    @abstractmethod
    def buscar (self, elemento: T) -> Tuple[bool, int]:
        pass
    
    # Verifica si el elemento es la raiz.
    @abstractmethod
    def esRaiz (self, elemento: T) -> bool:
        pass
    
    # Verifica si el elemento es una hoja.
    @abstractmethod
    def esHoja (self, elemento: T) -> bool:
        pass
    
    # Retorna una lista en orden.
    @abstractmethod
    def inOrder(self) -> List[T]:
        pass