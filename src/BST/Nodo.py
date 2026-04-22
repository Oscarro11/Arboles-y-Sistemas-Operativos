from __future__ import annotations
from typing import Generic, TypeVar, Optional

T = TypeVar('T')

class Nodo(Generic[T]):
    def __init__(self, valor:int, izquierda:Optional[Nodo[T]], derecha:Optional[Nodo[T]]) -> None:
        self.valor = valor
        self.izquierda = izquierda
        self.derecha = derecha

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Nodo):
            return False

        return (
            self.valor == other.valor and
            self.izquierda == other.izquierda and
            self.derecha == other.derecha
        )