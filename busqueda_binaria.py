

def busquedaBinaria(lista, elemento_a_buscar):
   
    izq = 0
    der = len(lista) -1
    
    while izq <= der:
        medio = int((izq+der)/2)
        
        
        
        if lista[medio] == elemento_a_buscar:
            return medio
        elif lista[medio] > elemento_a_buscar:
            der = medio - 1
        else:
            izq = medio + 1
            
    return -1
                   

if __name__ == "__main__": 
   
   print("ingrese una lista ordenada: ")
   lista = input()
   while lista != [[]]:
        print("ingrese el elemento a buscar: ")
        elemento_a_buscar = input()
        
        resultado = busquedaBinaria(lista, elemento_a_buscar)
        
        print("resultado", resultado)
  
        
    
        
        
        
            
            
