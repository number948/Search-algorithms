
def busquedaLineal(lista, valor, largo):
    #largo = 5
    
    for i in range(0, largo):
        if (lista[i] == valor):
            return i
    return -1

if __name__ == "__main__":
    lista = [1,2,3,4,5] 
    valor = 1
    largo = 5
    
    resultado = busquedaLineal(lista, valor, largo)
    
    print("posicion de la lista en que se encuentra el elemento es: ", resultado)