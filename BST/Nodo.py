from __future__ import annotations

class Nodo[T]:
    def __init__(self, valor:int, izquierda:Nodo[T], derecha:Nodo[T]) -> None:
        self.valor = valor
        self.izquierda = izquierda
        self.derecha = derecha