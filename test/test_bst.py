from BST.BST import BST

def test_inorder():
    arbol: BST[int] = BST()
    arbol.insertar(4)
    arbol.insertar(2)
    arbol.insertar(1)

    assert [1, 2, 4] == arbol.inOrder()

def test_eliminar():
    arbol: BST[int] = BST()
    arbol.insertar(4)
    arbol.insertar(2)
    arbol.insertar(5)

    assert arbol.eliminar(4)
    assert [2, 5] == arbol.inOrder()

def test_esHoja():
    arbol: BST[int] = BST()
    arbol.insertar(4)
    arbol.insertar(2)
    arbol.insertar(5)
    arbol.insertar(3)

    assert arbol.esHoja(3)

def test_buscar():
    arbol: BST[int] = BST()
    arbol.insertar(4)
    arbol.insertar(2)
    arbol.insertar(5)
    arbol.insertar(6)
    arbol.insertar(7)

    assert (True, 4) == arbol.buscar(7)