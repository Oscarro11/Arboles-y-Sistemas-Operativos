from __future__ import annotations
from .types import T
from typing import Generic, Optional, Self
from BST.Nodo import Nodo
from BST.BST import BST
import BST.Rotations as rot

class NodoRedBlack(Generic[T], Nodo[T]):
    def __init__(self, valor: T, izquierda: Optional[Self] = None, derecha: Optional[Self] = None, rojo: bool = True) -> None:
        self.valor: T = valor
        self.izquierda: Optional[Self] = izquierda
        self.derecha: Optional[Self] = derecha
        self.rojo: bool = rojo


class RedBlackTree(Generic[T], BST[T]):
    def __init__(self):
        self.raiz: Optional[NodoRedBlack[T]] = None

    def insertar(self, elemento: T) -> bool:
        if self.raiz == None:
            self.raiz = NodoRedBlack(elemento, None, None, False)
            return True
        
        visitas: list[tuple[bool, NodoRedBlack[T]]] = []
        encontrado = False
        actual = self.raiz
        while actual:
            
            # Si el elemento es menor, va a izquierda
            if elemento < actual.valor:
                visitas.append((False, actual))

                if actual.izquierda is None:
                    actual.izquierda = NodoRedBlack(elemento)
                    encontrado = True
                    actual = None

                else:
                    actual = actual.izquierda

            # Si el elemento es mayor, va a derecha
            elif elemento > actual.valor:
                visitas.append((True, actual))

                if actual.derecha is None:
                    actual.derecha = NodoRedBlack(elemento)
                    encontrado = True
                    actual = None
                else:    
                    actual = actual.derecha

            else:
                encontrado = False
                actual = None

        visitas.append((False, NodoRedBlack(elemento)))
        self._reordenar(visitas)
        return encontrado
    
    
    def _reordenar(self, recorrido: list[tuple[bool, NodoRedBlack[T]]]) -> None:
        i = len(recorrido)-1
        continuar = True

        if i < 2:
            return
        else:
            while(i >= 3 and continuar):
                padre = recorrido[i-1]

                if not padre[1].rojo:
                    continuar = False
                else:
                    abuelo = recorrido[i-2]
                    bisabuelo = recorrido[i-3]

                    if abuelo[0]: tio = abuelo[1].izquierda
                    else: tio = abuelo[1].derecha 
                

                    if tio is None or not tio.rojo:
                        match padre[0], abuelo[0]:
                            case True, True:
                                padre_modificado = rot.zag(abuelo[1])

                                if bisabuelo[0]:
                                    bisabuelo[1].derecha = padre_modificado
                                else:
                                    bisabuelo[1].izquierda = padre_modificado

                                padre_modificado.rojo = False
                                abuelo[1].rojo = True
                                    
                            case True, False: 
                                hijo_modificado = rot.zag_zig(abuelo[1])

                                if bisabuelo[0]:
                                    bisabuelo[1].derecha = hijo_modificado
                                else:
                                    bisabuelo[1].izquierda = hijo_modificado
                                
                                hijo_modificado.rojo = False
                                padre[1].rojo = True
                                abuelo[1].rojo = True

                                i += -1
                                
                            case False, True: 
                                hijo_modificado = rot.zig_zag(abuelo[1])

                                if bisabuelo[0]:
                                    bisabuelo[1].derecha = hijo_modificado
                                else:
                                    bisabuelo[1].izquierda = hijo_modificado

                                hijo_modificado.rojo = False
                                padre[1].rojo = True
                                abuelo[1].rojo = True

                                i += -1

                            case False, False: 
                                padre_modificado = rot.zig(abuelo[1])

                                if bisabuelo[0]:
                                    bisabuelo[1].derecha = padre_modificado
                                else:
                                    bisabuelo[1].izquierda = padre_modificado
                                
                                padre_modificado.rojo = False
                                abuelo[1].rojo = True
                
                    else:
                        padre[1].rojo = False
                        tio.rojo = False
                        abuelo[1].rojo = True

                        i += -1

                    i += -2

        if i == 2:
            padre = recorrido[1]
            abuelo = recorrido[0]

            if padre[1].rojo:
                if abuelo[0]: tio = abuelo[1].izquierda
                else: tio = abuelo[1].derecha

                if tio is None or not tio.rojo:
                    match padre[0], abuelo[0]:
                        case True, True: 
                            padre_modificado = rot.zag(abuelo[1])
                            self.raiz = padre_modificado

                            padre_modificado.rojo = False
                            abuelo[1].rojo = True
                                
                        case True, False: 
                            hijo_modificado = rot.zag_zig(abuelo[1])
                            self.raiz = hijo_modificado
                            
                            hijo_modificado.rojo = False
                            padre[1].rojo = True
                            abuelo[1].rojo = True
                            
                        case False, True: 
                            hijo_modificado = rot.zig_zag(abuelo[1])
                            self.raiz = hijo_modificado

                            hijo_modificado.rojo = False
                            padre[1].rojo = True
                            abuelo[1].rojo = True

                        case False, False:
                            padre_modificado = rot.zig(abuelo[1]) 
                            self.raiz = padre_modificado
                            
                            padre_modificado.rojo = False
                            abuelo[1].rojo = True
            
                else:
                    padre[1].rojo = False
                    tio.rojo = False
                    abuelo[1].rojo = True

        if self.raiz: self.raiz.rojo = False