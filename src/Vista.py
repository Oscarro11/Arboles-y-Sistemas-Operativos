from Controlador import Controlador
from pathlib import Path
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(2000)

def graficar(name: str, resBST: float, resSplay: float, resRedBlack: float) -> None:
    #categories = ["BST", "Splay Tree", "Red & Black Tree"]
    #values = [resBST, resSplay, resRedBlack]

    categories = ["Splay Tree", "Red & Black Tree"]
    values = [resSplay, resRedBlack]

    plt.bar(categories, values, color="skyblue")
    plt.xlabel('Data Structure')
    plt.ylabel('Iterations average in data search')
    plt.title(f'Performance of BST in scenario {name}')

    script_location = Path(__file__).resolve().parent
    save_file = script_location / ".." / "resources" / "graphs" / f"Performance {name}.pdf"

    plt.savefig(save_file)

controlador = Controlador()
opcion = "0"

while opcion != "4":
    print("\nBienvenido al menu principal, por favor elija que opcion desea realizar\n")
    print("""1. Realizar simulacion A
2. Realizar simulacion B
3. Realizar simulacion C
4. Salir""")
    
    opcion = input()
    match opcion:
        case "1": 
            print("Ingrese la cantidad de procesos con los que desea realizar la simulacion\n")
            cant_procesos = 0

            try:
                cant_procesos = int(input())
            except:
                print("La entrada que ha ingresado no es un numero natural, intentelo de nuevo\n")

            if cant_procesos <= 0: print("La cantidad de procesos a usar debe ser mayor de 0, intentelo de nuevo\n")
            resultados = controlador.realizarSimulacionA(cant_procesos)

            graficar(resultados["escenario"], resultados["promedio_bst"], resultados["promedio_splay"], resultados["promedio_redblack"])

            print(f"""
                    RESULTADOS
                    Escenario: {resultados["escenario"]}

                    Promedio de iteraciones en BST estandar: {resultados["promedio_bst"]}
                    Promedio de iteraciones en Splay Tree: {resultados["promedio_splay"]}
                    Promedio de iteraciones en Red & Black Tree: {resultados["promedio_redblack"]}
                    """)

        case "2": 
            resultados = controlador.realizarSimulacionB()

            graficar(resultados["escenario"], resultados["promedio_bst"], resultados["promedio_splay"], resultados["promedio_redblack"])

            print(f"""
                        RESULTADOS
                        Escenario: {resultados["escenario"]}
                        
                        Promedio de iteraciones en BST estandar: {resultados["promedio_bst"]}
                        Promedio de iteraciones en Splay Tree: {resultados["promedio_splay"]}
                        Promedio de iteraciones en Red & Black Tree: {resultados["promedio_redblack"]}
                        """)

        case "3":
            print("Ingrese la cantidad de procesos con los que desea realizar la simulacion\n")
            cant_procesos = 0

            try:
                cant_procesos = int(input())
            except:
                print("La entrada que ha ingresado no es un numero natural, intentelo de nuevo\n")

            if cant_procesos <= 0: print("La cantidad de procesos a usar debe ser mayor de 0, intentelo de nuevo\n")
            resultados = controlador.realizarSimulacionC(cant_procesos)

            graficar(resultados["escenario"], resultados["promedio_bst"], resultados["promedio_splay"], resultados["promedio_redblack"])

            print(f"""
                    RESULTADOS
                    Escenario: {resultados["escenario"]}
                    
                    Promedio de iteraciones en BST estandar: {resultados["promedio_bst"]}
                    Promedio de iteraciones en Splay Tree: {resultados["promedio_splay"]}
                    Promedio de iteraciones en Red & Black Tree: {resultados["promedio_redblack"]}
                    """)

        case "4": 
            print("Gracias por usar el programa, esperamos verlo pronto\n")

        case _: 
            print("La opcion elegida no corresponde con ninguna del programa, intentelo de nuevo\n")