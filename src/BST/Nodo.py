from .types import T
from __future__ import annotations
from typing import Generic, Optional

class Nodo(Generic[T]):
    def __init__(self, valor: T, izquierda:Optional[Nodo[T]] = None, derecha:Optional[Nodo[T]] = None) -> None:
        self.valor: T = valor
        self.izquierda: Optional[Nodo[T]] = izquierda
        self.derecha: Optional[Nodo[T]] = derecha

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Nodo):
            return False

        return (
            self.valor == other.valor and
            self.izquierda == other.izquierda and
            self.derecha == other.derecha
        )