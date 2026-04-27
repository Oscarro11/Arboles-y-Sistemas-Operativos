import random

from BST.BST import BST
from BST.SplayTree import SplayTree
from BST.RedBlackTree import RedBlackTree

class Controlador:
    def __init__(self):
        self.bst_simple: BST[int] = BST[int]()
        self.bst_splay: SplayTree[int] = SplayTree[int]()
        self.bst_redblack: RedBlackTree[int] = RedBlackTree[int]()

    # "Escenario A: Llegada Aleatoria"
    def realizarSimulacionA (self, procesos: int, num_busquedas: int = 100) -> dict:

        # Limpia los árboles
        self.bst_simple = BST[int]()
        self.bst_splay = SplayTree[int]()
        self.bst_redblack = RedBlackTree[int]()

        # Genera procesos aleatorios
        procesos_vals = random.sample(range(1, procesos+5000), procesos)

        # Inserta los procesos en los árboles
        for val in procesos_vals:
            self.bst_simple.insertar(val)
            self.bst_splay.insertar(val)
            self.bst_redblack.insertar(val)

        self.bst_simple.preOrderGraph("BST A")
        self.bst_splay.preOrderGraph("Splay A")
        self.bst_redblack.preOrderGraph("Red&Black A")

        # Busca 100 procesos aleatorios
        busquedas = random.sample(procesos_vals, min(num_busquedas, procesos))

        # Crea una lista para guardar las iteraciones
        iteraciones_bst = []
        iteraciones_splay = []
        iteraciones_redblack = []

        # Agrega los valores a sus listas
        for val in busquedas:
            # BST Simple
            encontrado, iteraciones = self.bst_simple.buscar(val)
            if encontrado:
                iteraciones_bst.append(iteraciones)
            
            # Splay Tree
            encontrado, iteraciones = self.bst_splay.buscar(val)
            if encontrado:
                iteraciones_splay.append(iteraciones)
            
            # Red-Black Tree
            encontrado, iteraciones = self.bst_redblack.buscar(val)
            if encontrado:
                iteraciones_redblack.append(iteraciones)
        
        # Calcular promedios
        promedio_bst = sum(iteraciones_bst) / len(iteraciones_bst) if iteraciones_bst else 0
        promedio_splay = sum(iteraciones_splay) / len(iteraciones_splay) if iteraciones_splay else 0
        promedio_redblack = sum(iteraciones_redblack) / len(iteraciones_redblack) if iteraciones_redblack else 0
        
        return {
            'escenario': 'A',
            'promedio_bst': promedio_bst,
            'promedio_splay': promedio_splay,
            'promedio_redblack': promedio_redblack,
            'num_busquedas': len(busquedas)
        }

    def realizarSimulacionB (self) -> dict:
        # Limpia los árboles
        self.bst_simple = BST[int]()
        self.bst_splay = SplayTree[int]()
        self.bst_redblack = RedBlackTree[int]()

        # Genera procesos de forma secuencial
        procesos_vals = [i+1 for i in range(1000)]

        # Inserta los procesos en los árboles
        for val in procesos_vals:
            self.bst_simple.insertar(val)
            self.bst_splay.insertar(val)
            self.bst_redblack.insertar(val)

        self.bst_simple.preOrderGraph("BST B")
        self.bst_splay.preOrderGraph("Splay B")
        self.bst_redblack.preOrderGraph("Red&Black B")

        # Crea una lista para guardar las iteraciones
        iteraciones_bst: int = self.bst_simple.buscar(1000)[1]
        iteraciones_splay: int = self.bst_splay.buscar(1000)[1]
        iteraciones_redblack: int = self.bst_redblack.buscar(1000)[1]
        
        return {
            'escenario': 'B',
            'promedio_bst': iteraciones_bst,
            'promedio_splay': iteraciones_splay,
            'promedio_redblack': iteraciones_redblack,
        }


    def realizarSimulacionC (self, procesos: int) -> dict:
        # Limpia los árboles
        self.bst_simple = BST[int]()
        self.bst_splay = SplayTree[int]()
        self.bst_redblack = RedBlackTree[int]()

        # Genera procesos aleatorios
        procesos_vals = random.sample(range(1, procesos+5000), procesos)

        # Inserta los procesos en los árboles
        for val in procesos_vals:
            self.bst_simple.insertar(val)
            self.bst_splay.insertar(val)
            self.bst_redblack.insertar(val)

        self.bst_simple.preOrderGraph("BST C")
        self.bst_splay.preOrderGraph("Splay C")
        self.bst_redblack.preOrderGraph("Red&Black C")

        # Busca el mismo proceso 50 veces
        busqueda = random.choice(procesos_vals)

        # Crea una lista para guardar las iteraciones
        iteraciones_bst = []
        iteraciones_splay = []
        iteraciones_redblack = []

        # Agrega los valores a sus listas
        for val in range(50):
            # BST Simple
            encontrado, iteraciones = self.bst_simple.buscar(busqueda)
            if encontrado:
                iteraciones_bst.append(iteraciones)
            
            # Splay Tree
            encontrado, iteraciones = self.bst_splay.buscar(busqueda)
            if encontrado:
                iteraciones_splay.append(iteraciones)
            
            # Red-Black Tree
            encontrado, iteraciones = self.bst_redblack.buscar(busqueda)
            if encontrado:
                iteraciones_redblack.append(iteraciones)
        
        # Calcular promedios
        promedio_bst = sum(iteraciones_bst) / len(iteraciones_bst) if iteraciones_bst else 0
        promedio_splay = sum(iteraciones_splay) / len(iteraciones_splay) if iteraciones_splay else 0
        promedio_redblack = sum(iteraciones_redblack) / len(iteraciones_redblack) if iteraciones_redblack else 0
        
        return {
            'escenario': 'C',
            'promedio_bst': promedio_bst,
            'promedio_splay': promedio_splay,
            'promedio_redblack': promedio_redblack,
            'num_busquedas': 50
        }