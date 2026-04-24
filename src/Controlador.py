import random
import sys
import os

from BST.BST import BST
from BST.SplayTree import SplayTree
from BST.RedBlack import RedBlackTree

class Controlador:
    def __init__(self):
        self.bst_simple: BST[int] = BST[int]()
        self.bst_splay: SplayTree[int] = SplayTree[int]()
        self.bst_redblack: RedBlack[int] = RedBlack[int]()

    # "Escenario A: Llegada Aleatoria"
    def realizarSimulacionA (self, procesos: int, num_busquedas: int = 100) -> dict:

        # Limpia los árboles
        self.bst_simple = BST[int]()
        self.bst_splay = SplayTree[int]()
        self.bst_redblack = RedBlack[int]()

        # Genera procesos aleatorios
        procesos_vals = [random.randint(1, 1000) for _ in range(procesos)]

        # Inserta los procesos en los árboles
        for val in procesos_vals:
            self.bst_simple.insertar(val)
            self.bst_splay.insertar(val)
            self.bst_redblack.insertar(val)

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

    def realizarSimulacionB (self, procesos: int) -> dict:
        print ("Escenario A: Llegada Secuencial")
        print ()


    def realizarSimulacionC (self, procesos: int) -> dict:
        print ("Escenario A: Proceso Frecuente de I/O")
        print ()