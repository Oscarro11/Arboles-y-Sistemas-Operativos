import graphviz
from pathlib import Path

from .types import T
from typing import Generic, Optional

from BST.IBinaryTree import *
from BST.Nodo import Nodo, N

class BST(Generic[T], IBinaryTree[T]):
    def __init__(self):
        self.raiz: Optional[Nodo[T]] = None

    # Para insertar un nodo
    def insertar (self, elemento: T) -> bool:

        # Si no tiene raíz, lo inserta y ya
        if self.raiz is None:
            self.raiz = Nodo(elemento)
            return True
        
        actual = self.raiz
        while actual:
            
            # Si el elemento es menor, va a izquierda
            if elemento < actual.valor:
                if actual.izquierda is None:
                    actual.izquierda = Nodo(elemento)
                    return True
                actual = actual.izquierda

            # Si el elemento es mayor, va a derecha
            elif elemento > actual.valor:
                if actual.derecha is None:
                    actual.derecha = Nodo(elemento)
                    return True
                actual = actual.derecha

            else:
                # El elemento ya existe 
                return False
        return False

    # Para eliminar un nodo existente
    def eliminar (self, elemento: T) -> bool:
        def _eliminar (raiz: Optional[Nodo[T]], valor: T) -> Tuple [Optional[Nodo[T]], bool]:
            
            # Si no tiene raíz, osea, no existe el árbol
            if raiz is None:
                return None, False
            
            if valor < raiz.valor:
                raiz.izquierda, eliminado = _eliminar (raiz.izquierda, valor)
                return raiz, eliminado
            if valor > raiz.valor:
                raiz.derecha, eliminado = _eliminar (raiz.derecha, valor)
                return raiz, eliminado
            else:

                # Encuentra el nodo
                if raiz.izquierda is None:
                    return raiz.derecha, True
                elif raiz.derecha is None:
                    return raiz.izquierda, True
                else:

                    # Nodo con dos hijos
                    sucesor = raiz.derecha
                    while sucesor.izquierda:
                        sucesor = sucesor.izquierda

                    raiz.valor = sucesor.valor
                    raiz.derecha, _ = _eliminar (raiz.derecha, sucesor.valor)
                    return raiz, True
            
        self.raiz, eliminado = _eliminar (self.raiz, elemento)
        return eliminado

    # Busca y regresa comparaciones_realizadas
    def buscar (self, elemento: T) -> Tuple[bool, int]:
        search_count = 0
        actual = self.raiz

        while actual:
            search_count += 1
            if elemento == actual.valor:
                return (True, search_count)
            elif elemento < actual.valor:
                actual = actual.izquierda
            else:
                actual = actual.derecha

        return (False, search_count)

    # Para buscar, pero no retornar algo específicamente a diferencia de "buscar"
    def _buscar(self, elemento: T) -> Optional[Nodo[T]]:
        actual = self.raiz
        while actual:
            if elemento == actual.valor:
                return actual
            elif elemento < actual.valor:
                actual = actual.izquierda
            else:
                actual = actual.derecha
        return None

    # Verifica si el elemento es raíz
    def esRaiz (self, elemento: T) -> bool:
        # Si el árbol sí tiene raíz Y el valor de la raiz es igual al elemento...
        return self.raiz is not None and self.raiz.valor == elemento
        
    # Verifica si el elemento es hoja
    def esHoja (self, elemento: T) -> bool:
        nodo = self._buscar(elemento)
        # Si encuentra el nodo Y no tiene nodo en la izq Y der
        return nodo is not None and nodo.izquierda is None and nodo.derecha is None

    # Recorre el árbol In-Order
    def inOrder (self) -> List[T]:
        resultado = []

        def _inorder (nodo: Optional[Nodo[T]]):
            if nodo:
                _inorder(nodo.izquierda)
                resultado.append(nodo.valor)
                _inorder(nodo.derecha)
            
        _inorder(self.raiz)
        return resultado
    
    def preOrderGraph (self, name: str) -> None:
        dot = graphviz.Digraph(comment=f"{self.__class__}")
        if self.raiz is not None: self._preOrderGraph(self.raiz, dot)

        script_location = Path(__file__).resolve().parent
        save_file = script_location / ".." / ".." / "resources" / "structures" / f"{name} structure.gv"

        dot.render(save_file)
    
    def _preOrderGraph (self, node: N, graph: graphviz.Digraph) -> None:
        if node is None:
            return
        else:
            graph.node(f"{node.valor}", f"{node.valor}")

            if node.derecha is not None:
                graph.node(f"{node.derecha.valor}", f"{node.derecha.valor}")
                graph.edge(f"{node.valor}", f"{node.derecha.valor}", constraint='true')
                self._preOrderGraph(node.derecha, graph)

            if node.izquierda is not None:
                graph.node(f"{node.izquierda.valor}", f"{node.izquierda.valor}")
                graph.edge(f"{node.valor}", f"{node.izquierda.valor}", constraint='true')
                self._preOrderGraph(node.izquierda, graph)