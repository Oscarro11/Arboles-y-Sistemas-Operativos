class BST (IBinaryTree[T]):

    def __init__():
        self.raiz: Optional[Nodo[T]] = None
        self.search_count: int = 0


# Para insertar un nodo
def insertar (self, elemento: T) -> bool:
    
    # Si no tiene raíz, lo inserta y ya
    if self.raiz is None:
        self.raiz = Nodo(elemento)
        return True
    
    actual = self.raiz
    while actual:
        
        # Si el elemento es menor, va a izquierda
        if elemento < actual.valor:
            if actual.left is None:
                actual.left = Nodo(elemento)
                return True
            actual = actual.left

        # Si el elemento es mayor, va a derecha
        elif elemento > actual.valor:
            if actual.right is None:
                actual.right = Nodo(elemento)
                return True
            actual = actual.right

        else:
            # El elemento ya existe 
            return False

# Para eliminar un nodo existente
def eliminar (self, elemento: T) -> bool:
    def _eliminar (raiz: Optional[Nodo[T]], valor: T) -> Tuple [optional[Nodo[T]], bool]:
          
        # Si no tiene raíz, osea, no existe el árbol
        if raiz is None:
            return None, False
        
        if valor < raiz.valor:
            raiz.left, eliminado = _eliminar (raiz.left, valor)
            return raiz, eliminado
        if valor > raiz.valor:
            raiz.right, eliminado = _eliminar (raiz.right, valor)
            return raiz, eliminado
        else:

            # Encuentra el nodo
            if raiz.left is None:
                return raiz.right, True
            elif raiz.right is None:
                return raiz.left, True
            else:

                # Nodo con dos hijos
                sucesor = raiz.right
                while sucesor.left:
                    sucesor = sucesor.left
                raiz.valor = sucesor.valor
                raiz.right, _ = _eliminar (raiz.right, sucesor.valor)
                return raiz, True
        
        self.raiz, eliminado = _eliminar (self.raiz, elemento)
        return eliminado

# Busca y regresa comparaciones_realizadas
def buscar (self, elemento: T) -> Tuple[bool, int]:
    self.search_count = 0
    actual = self.raiz

    while actual:
        self.search_count += 1
        if elemento == actual.valor:
            return (True, self.search_count)
        elif elemento < actual.valor:
            actual = actual.left
        else:
            actual = actual.right
    return (False, self.search_count)

# Para buscar, pero no retornar algo específicamente a diferencia de "buscar"
def _buscar(self, elemento: T) -> Optional[Nodo[T]]:
    actual = self.raiz
    while actual:
        if elemento == actual.valor:
            return actual
        elif elemento < actual.valor:
            actual = actual.left
        else:
            actual = actual.right
    return None

# Verifica si el elemento es raíz
def esRaiz (self, elemento: T) -> bool:
    # Si el árbol sí tiene raíz Y el valor de la raiz es igual al elemento...
    return self.raiz is not None and self.raiz.valor == elemento
     
# Verifica si el elemento es hoja
def esHoja (self, elemento: T) -> bool:
    nodo = self._buscar_nodo(elemento)
    # Si encuentra el nodo Y no tiene nodo en la izq Y der
    return nodo is not None and nodo.left is None and nodo.right is None

# Recorre el árbol In-Order
def inOrder () -> List[T]:
    resultado = []
    
    def _inorder (nodo: Optional[Nodo[T]]):
        if nodo:
            _inorder(nodo.left)
            resultado.apped(nodo.valor)
            _inorder(nodo.right)
        
        _inorder(self.raiz)
        return resultado