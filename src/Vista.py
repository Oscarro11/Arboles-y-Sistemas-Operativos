from Controlador import Controlador

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
            try:
                cant_procesos = int(input())
                if cant_procesos <= 0: print("La cantidad de procesos a usar debe ser mayor de 0, intentelo de nuevo\n")
                resultados = controlador.realizarSimulacionA(cant_procesos)

                print(f"""
                        RESULTADOS
                        Escenario: {resultados["escenario"]}

                        Promedio de iteraciones en BST estandar: {resultados["promedio_bst"]}
                        Promedio de iteraciones en Splay Tree: {resultados["promedio_splay"]}
                        Promedio de iteraciones en Red & Black Tree: {resultados["promedio_redblack"]}
                        """)

            except:
                print("La entrada que ha ingresado no es un numero natural, intentelo de nuevo\n")

        case "2": 
            resultados = controlador.realizarSimulacionB()

            print(f"""
                        RESULTADOS
                        Escenario: {resultados["escenario"]}
                        
                        Promedio de iteraciones en BST estandar: {resultados["promedio_bst"]}
                        Promedio de iteraciones en Splay Tree: {resultados["promedio_splay"]}
                        Promedio de iteraciones en Red & Black Tree: {resultados["promedio_redblack"]}
                        """)

        case "3":
            print("Ingrese la cantidad de procesos con los que desea realizar la simulacion\n")
            try:
                cant_procesos = int(input())
                if cant_procesos <= 0: print("La cantidad de procesos a usar debe ser mayor de 0, intentelo de nuevo\n")
                resultados = controlador.realizarSimulacionC(cant_procesos)

                print(f"""
                        RESULTADOS
                        Escenario: {resultados["escenario"]}
                        
                        Promedio de iteraciones en BST estandar: {resultados["promedio_bst"]}
                        Promedio de iteraciones en Splay Tree: {resultados["promedio_splay"]}
                        Promedio de iteraciones en Red & Black Tree: {resultados["promedio_redblack"]}
                        """)

            except:
                print("La entrada que ha ingresado no es un numero natural, intentelo de nuevo\n")

        case "4": 
            print("Gracias por usar el programa, esperamos verlo pronto\n")

        case _: 
            print("La opcion elegida no corresponde con ninguna del programa, intentelo de nuevo\n")