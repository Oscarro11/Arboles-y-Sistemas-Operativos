from BST.RedBlackTree import RedBlack, NodoRedBlack

def test_insertion():
    tree: RedBlack[int] = RedBlack[int]()

    tree.insertar(7)
    tree.insertar(27)
    tree.insertar(14)
    tree.insertar(11)
    tree.insertar(78)
    tree.insertar(55)
    tree.insertar(60)   
    tree.insertar(59)
    tree.insertar(58)
    tree.insertar(79)
    tree.insertar(80)
    tree.insertar(57)
    tree.insertar(56)

    nodo_esperado = NodoRedBlack(55, 
                                 NodoRedBlack(14, 
                                              NodoRedBlack(7,
                                                           None,
                                                           NodoRedBlack(11, None, None, True), False), 
                                              NodoRedBlack(27, None, None, False), False),
                                 NodoRedBlack(60, 
                                              NodoRedBlack(58,
                                                           NodoRedBlack(57, 
                                                                        NodoRedBlack(56, None, None, True), 
                                                                        None, False), 
                                                           NodoRedBlack(59, None, None, False), True), 
                                              NodoRedBlack(79, 
                                                           NodoRedBlack(78, None, None, True), 
                                                           NodoRedBlack(80, None, None, True), False), False), 
                                 False)

    assert nodo_esperado == tree.raiz