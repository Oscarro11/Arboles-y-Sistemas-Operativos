from BST.SplayTree import SplayTree

def test_visitas():
    tree: SplayTree[int] = SplayTree[int]()

    tree.insertar(7)
    tree.insertar(27)
    tree.insertar(14)
    tree.insertar(11)
    tree.insertar(78)
    
    if tree.raiz != None:
        assert 78 == tree.raiz.valor

def test_visitas2():
    tree: SplayTree[int] = SplayTree[int]()

    tree.insertar(15)
    tree.insertar(85)
    tree.insertar(90)
    tree.insertar(7)
    tree.insertar(2)
    tree.insertar(11)
    
    tree.eliminar(4)
    if tree.raiz != None:
        assert 11 == tree.raiz.valor