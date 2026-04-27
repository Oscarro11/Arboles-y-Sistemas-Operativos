# HDT8: Arboles-y-Sistemas-Operativos
### Yu-Fong Chen (242115) y Oscar Melchor (25216)

El propósito de este proyecto es simular y comparar el comportamiento de diferentes árboles de búsqueda binarios en la gestión de procesos de un sistema operativo. Para ello, se tienen 3 simulaciones diferentes, en donde la inserción y la búsqueda de datos es manipulada de cierta forma. El propósito de esto es destacar en qué situaciones es apropiado usar determinado arbol binario de búsqueda.


## Estructura del programa

El programa esta estructurado en 3 modulos principales, los cuales se encuentran en la carpeta de *src*. Estos modulos corresponden con la **Vista**, el **Controlador**, y los **Modelos** del programa, siendo este último una carpeta (*BST*) en donde estan los diferentes arboles a usar. 


## Requisitos

Para usar el programa, el usuario debe descargar los contenidos del repositorio y verificar que tenga instalado en su sistema las siguientes librerias, además del compilador de python v13.x:

- matplolib
- graphviz

Además, debe tener el motor de graphviz, el cual puede encontrarse [aqui](https://graphviz.org/download/)


## Ejecucion

Para ejecutar el programa, el usuario debe abrir una terminal. En ella, debe posicionarse en la carpeta:
> ..\(proyecto)\src

Y usar el comando 
> python -m Vista.py