from typing import Protocol, TypeVar

T_contract = TypeVar("T_contract", contravariant=True)
class Comparable(Protocol[T_contract]):
    def __lt__(self, other: T_contract, /) -> bool: ...
    def __gt__(self, other: T_contract, /) -> bool: ...

T = TypeVar("T", bound=Comparable)