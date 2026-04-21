from BST.Nodo import Nodo

def zig(padre:Nodo) -> Nodo:
    if padre.izquierda != None:
        hijo = padre.izquierda
        padre.izquierda = hijo.derecha
        return Nodo(hijo.valor, hijo.izquierda, padre)
    
    else:
        raise Exception(f"No puede realizarse zig debido a que {padre.valor} no tiene hijo izquierdo")

def zag(padre:Nodo) -> Nodo:
    if padre.derecha != None:
        hijo = padre.derecha
        padre.derecha = hijo.izquierda
        return Nodo(hijo.valor, padre, hijo.derecha)
    
    else:
        raise Exception(f"No puede realizarse zag debido a que {padre.valor} no tiene hijo derecho")
    
def zig_zig(abuelo:Nodo) -> Nodo:
    if abuelo.izquierda == None:
        raise Exception(f"No puede realizarse zig-zig debido a que {abuelo.valor} no tiene hijo izquierdo")
    
    else:
        padre = abuelo.izquierda
        if padre.izquierda == None:
            raise Exception(f"No puede realizarse zig-zig debido a que {padre.valor} no tiene hijo izquierdo")
        
        else:
            hijo = padre.izquierda
            
            derecha_hijo = hijo.derecha
            derecha_padre = padre.derecha

            hijo.derecha = padre
            padre.izquierda = derecha_hijo

            padre.derecha = abuelo
            abuelo.izquierda = derecha_padre

            return Nodo(hijo.valor, hijo.izquierda, padre)

def zag_zag(abuelo:Nodo) -> Nodo:
    if abuelo.derecha == None:
        raise Exception(f"No puede realizarse zag-zag debido a que {abuelo.valor} no tiene hijo derecho")
    
    else:
        padre = abuelo.derecha
        if padre.derecha == None:
            raise Exception(f"No puede realizarse zag-zag debido a que {padre.valor} no tiene hijo derecho")
        
        else:
            hijo = padre.derecha
            
            izquierda_hijo = hijo.izquierda
            izquierda_padre = padre.izquierda

            hijo.izquierda = padre
            padre.derecha = izquierda_hijo

            padre.izquierda = abuelo
            abuelo.derecha = izquierda_padre

            return Nodo(hijo.valor, padre, hijo.derecha)
        
def zig_zag(abuelo:Nodo) -> Nodo:
    if abuelo.derecha == None:
        raise Exception(f"No puede realizarse zig-zag debido a que {abuelo.valor} no tiene hijo derecho")
    
    else:
        padre = abuelo.derecha
        if padre.izquierda == None:
            raise Exception(f"No puede realizarse zig-zag debido a que {padre.valor} no tiene hijo izquierda")
        
        else:
            hijo = padre.izquierda

            abuelo.derecha = hijo.izquierda
            padre.izquierda = hijo.derecha

            return Nodo(hijo.valor, abuelo, padre)
        
def zag_zig(abuelo:Nodo) -> Nodo:
    if abuelo.izquierda == None:
        raise Exception(f"No puede realizarse zig-zag debido a que {abuelo.valor} no tiene hijo derecho")
    
    else:
        padre = abuelo.izquierda
        if padre.derecha == None:
            raise Exception(f"No puede realizarse zig-zag debido a que {padre.valor} no tiene hijo izquierda")
        
        else:
            hijo = padre.derecha

            padre.derecha = hijo.izquierda
            abuelo.izquierda = hijo.derecha

            return Nodo(hijo.valor, padre, abuelo)  