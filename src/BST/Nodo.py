from __future__ import annotations
from .types import T
from typing import Generic, Optional, Self, TypeVar

class Nodo(Generic[T]):
    def __init__(self, valor: T, izquierda:Optional[Self] = None, derecha:Optional[Self] = None) -> None:
        self.valor: T = valor
        self.izquierda: Optional[Self] = izquierda
        self.derecha: Optional[Self] = derecha

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Nodo):
            return False

        return (
            self.valor == other.valor and
            self.izquierda == other.izquierda and
            self.derecha == other.derecha
        )
    
N = TypeVar("N", bound=Nodo)