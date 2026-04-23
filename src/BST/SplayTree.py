from .types import T
from typing import Generic
from BST.BST import BST
from BST.BST import Nodo

import BST.Rotations as rot

class SplayTree(Generic[T], BST[T]):

    def insertar(self, elemento: T) -> bool:
        if self.raiz is None:
            self.raiz = Nodo(elemento)
            return True
        
        visitas: list[tuple[bool, Nodo]] = []
        encontrado = False
        actual = self.raiz

        while actual:

            # Si el elemento es menor, va a izquierda
            if elemento < actual.valor:
                visitas.append((False, actual))

                if actual.izquierda is None:
                    actual.izquierda = Nodo(elemento)
                    encontrado = True
                    actual = None

                else:
                    actual = actual.izquierda

            # Si el elemento es mayor, va a derecha
            elif elemento  > actual.valor:
                visitas.append((True, actual))

                if actual.derecha is None:
                    actual.derecha = Nodo(elemento)
                    encontrado = True
                    actual = None
                
                else:
                    actual = actual.derecha

            else:
                encontrado = False
                actual = None

        self._reordenar(visitas)
        return encontrado
    
    def buscar (self, elemento: T) -> tuple[bool, int]:
        search_count = 0
        encontrado = False
        visitas: list[tuple[bool, Nodo]] = []
        actual = self.raiz

        while actual:
            search_count += 1

            if elemento == actual.valor:
                encontrado = True
                actual = None

            elif elemento < actual.valor:
                visitas.append((False, actual))
                actual = actual.izquierda

            else:
                visitas.append((True, actual))
                actual = actual.derecha

        self._reordenar(visitas)
        return (encontrado, search_count)


    def _reordenar(self, recorrido: list[tuple[bool, Nodo[T]]]) -> None:
        i = len(recorrido)-1

        while(i >= 2):
            padre = recorrido[i]
            abuelo = recorrido[i-1]
            bisabuelo = recorrido[i-2]

            match padre[0], abuelo[0]:
                case True, True: 
                    if bisabuelo[0]:
                        bisabuelo[1].derecha = rot.zag_zag(abuelo[1])
                    else:
                        bisabuelo[1].izquierda = rot.zag_zag(abuelo[1])
                        
                case True, False: 
                    if bisabuelo[0]:
                        bisabuelo[1].derecha = rot.zag_zig(abuelo[1])
                    else:
                        bisabuelo[1].izquierda = rot.zag_zig(abuelo[1])
                    
                case False, True: 
                    if bisabuelo[0]:
                        bisabuelo[1].derecha = rot.zig_zag(abuelo[1])
                    else:
                        bisabuelo[1].izquierda = rot.zig_zag(abuelo[1])

                case False, False: 
                    if bisabuelo[0]:
                        bisabuelo[1].derecha = rot.zig_zig(abuelo[1])
                    else:
                        bisabuelo[1].izquierda = rot.zig_zig(abuelo[1])
            
            i += -2

        if i == 1:
            padre = recorrido[1]
            abuelo = recorrido[0]
            match padre[0], abuelo[0]:
                case True, True: self.raiz = rot.zag_zag(abuelo[1])
                case True, False: self.raiz = rot.zag_zig(abuelo[1])
                case False, True: self.raiz = rot.zig_zag(abuelo[1])
                case False, False: self.raiz = rot.zig_zig(abuelo[1])
        
        else:
            if recorrido[0][0]: self.raiz = rot.zag(recorrido[0][1])
            else: self.raiz = rot.zig(recorrido[0][1])