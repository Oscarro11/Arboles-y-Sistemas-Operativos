from BST.Nodo import N

def zig(padre: N) -> N:
    hijo = padre.izquierda

    if hijo is None:
        raise Exception(f"No puede hacerse la operacion de zig, debido a que {padre.valor} no tiene hijo izquierdo")
    else:
        padre.izquierda = hijo.derecha
        hijo.derecha = padre
        return hijo
            
def zag(padre: N) -> N:
    hijo = padre.derecha

    if hijo is None:
        raise Exception(f"No puede hacerse la operacion de zag, debido a que {padre.valor} no tiene hijo derecho")
    else:
        padre.derecha = hijo.izquierda
        hijo.izquierda = padre
        return hijo
    
def zig_zig(abuelo: N) -> N:
    padre = abuelo.izquierda

    if padre is None:
        raise Exception(f"No puede realizarse zig-zig debido a que {abuelo.valor} no tiene hijo izquierdo")
    else:
        hijo = padre.izquierda

        if hijo is None:
            raise Exception(f"No puede realizarse zig-zig debido a que {padre.valor} no tiene hijo izquierdo")
        else:
            derecha_hijo = hijo.derecha
            derecha_padre = padre.derecha

            hijo.derecha = padre
            padre.izquierda = derecha_hijo

            padre.derecha = abuelo
            abuelo.izquierda = derecha_padre

            return hijo

def zag_zag(abuelo: N) -> N:
    padre = abuelo.derecha

    if padre is None:
        raise Exception(f"No puede realizarse zag-zag debido a que {abuelo.valor} no tiene hijo derecho")
    else:
        hijo = padre.derecha

        if hijo is None:
            raise Exception(f"No puede realizarse zag-zag debido a que {padre.valor} no tiene hijo derecho")
        else:
            izquierda_hijo = hijo.izquierda
            izquierda_padre = padre.izquierda

            hijo.izquierda = padre
            padre.derecha = izquierda_hijo

            padre.izquierda = abuelo
            abuelo.derecha = izquierda_padre

            return hijo
        
def zig_zag(abuelo: N) -> N:
    padre = abuelo.derecha

    if padre is None:
        raise Exception(f"No puede realizarse zig-zag debido a que {abuelo.valor} no tiene hijo derecho")
    else:
        hijo = padre.izquierda

        if hijo is None:
            raise Exception(f"No puede realizarse zig-zag debido a que {padre.valor} no tiene hijo izquierdo")
        else:
            abuelo.derecha = hijo.izquierda
            padre.izquierda = hijo.derecha

            hijo.izquierda = abuelo
            hijo.derecha = padre

            return hijo
        
def zag_zig(abuelo: N) -> N:
    padre = abuelo.izquierda

    if padre is None:
        raise Exception(f"No puede realizarse zag-zig debido a que {abuelo.valor} no tiene hijo izquierdo")
    else:
        hijo = padre.derecha

        if hijo is None:
            raise Exception(f"No puede realizarse zag-zig debido a que {padre.valor} no tiene hijo derecho")
        else:
            abuelo.izquierda = hijo.derecha
            padre.derecha = hijo.izquierda

            hijo.izquierda = padre
            hijo.derecha = abuelo

            return hijo