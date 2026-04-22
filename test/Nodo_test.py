from BST.Nodo import Nodo
import BST.Rotations as rot

def test_zig():
    nodo1 = Nodo(1)
    nodo2 = Nodo(2)
    nodo3 = Nodo(3)
    nodo4 = Nodo(4)

    nodo2.izquierda = nodo1
    nodo2.derecha = nodo3
    nodo3.derecha = nodo4

    nodo_esperado = Nodo(1, None, Nodo(2, None, Nodo(3, None, Nodo(4, None, None))))
    assert nodo_esperado == rot.zig(nodo2)

def test_zag():
    nodo1 = Nodo(1)
    nodo2 = Nodo(2)
    nodo3 = Nodo(3)
    nodo4 = Nodo(4)
    
    nodo2.derecha = nodo1
    nodo2.izquierda = nodo3
    nodo3.izquierda = nodo4

    nodo_esperado = Nodo(1, Nodo(2, Nodo(3, Nodo(4, None, None), None), None), None)
    assert nodo_esperado == rot.zag(nodo2)

def test_zig_zig():
    nodo1 = Nodo(1)
    nodo2 = Nodo(2)
    nodo3 = Nodo(3)
    nodo4 = Nodo(4)

    nodo3.izquierda = nodo2
    nodo2.izquierda = nodo1
    nodo3.derecha = nodo4

    nodo_esperado = Nodo(1, None, Nodo(2, None, Nodo(3, None, Nodo(4, None, None))))
    assert nodo_esperado == rot.zig_zig(nodo3)

def test_zag_zag():
    nodo1 = Nodo(1)
    nodo2 = Nodo(2)
    nodo3 = Nodo(3)
    nodo4 = Nodo(4)

    nodo3.derecha = nodo2
    nodo2.derecha = nodo1
    nodo3.izquierda = nodo4

    nodo_esperado = Nodo(1, Nodo(2, Nodo(3, Nodo(4, None, None), None), None), None)
    assert nodo_esperado == rot.zag_zag(nodo3)

def test_zig_zag():
    nodo1 = Nodo(1)
    nodo2 = Nodo(2)
    nodo3 = Nodo(3)
    nodo4 = Nodo(4)

    nodo1.derecha = nodo2
    nodo2.izquierda = nodo3
    nodo3.izquierda = nodo4

    nodo_esperado = Nodo(3, Nodo(1, None, Nodo(4, None, None)), Nodo(2, None, None))
    assert nodo_esperado == rot.zig_zag(nodo1)

def test_zag_zig():
    nodo1 = Nodo(1)
    nodo2 = Nodo(2)
    nodo3 = Nodo(3)
    nodo4 = Nodo(4)

    nodo1.izquierda = nodo2
    nodo2.derecha = nodo3
    nodo3.derecha = nodo4

    nodo_esperado = Nodo(3, Nodo(2, None, None), Nodo(1, Nodo(4, None, None), None))
    assert nodo_esperado == rot.zag_zig(nodo1)