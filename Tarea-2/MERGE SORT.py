import random
import time

def OrdenMergeSort(listas):
    
    if len(listas) == 1:
        return listas
    
    medio = len(listas) / 2
    inicio = OrdenMergeSort(listas[:medio])
    ultimo = OrdenMergeSort(listas[medio:])

    if not len(inicio) or not len(ultimo):
        return inicio or ultimo
        
    resultado = []
    i = j = 0
    while (len(resultado) < len(ultimo)+len(inicio)):        
        if inicio[i] < ultimo[j]:
            resultado.append(inicio[i])
            i += 1
        else:
            resultado.append(ultimo[j])
            j += 1            
        if i == len(inicio) or j == len(ultimo):            
            resultado.extend(inicio[i:] or ultimo[j:])
            break

 
    return resultado
    
    


def reset():
    Tamlistas = input("INGRESE TAMAÑO DE NUMEROS A ORDENAR EJ:10-100-1000\n")
    listas = []
    Tiempo_inicia1 = time.clock()
    for i in range(Tamlistas):
        listas.append(random.randint(0,(Tamlistas*10)))
    print listas
    Tiempo_inicia = time.clock()
    Tiempo_Termina1 = time.clock()
    
    print ("LISTA ORDENADA")
    for i in range(10):
        Tiempo_inicia = time.clock()
        OrdenMergeSort(listas)
        Tiempo_Termina = time.clock()  
        print"Tiempo Ordenamamiento: %f"%(Tiempo_Termina - Tiempo_inicia)
        
    print"Tiempo llenado Lista Con Random: %f"%(Tiempo_Termina1 - Tiempo_inicia1)
    reset()

reset()

#Misael Armando Gutierrez Gutierrez
#Codigo: 625120
#Analisis y Diseño De Algoritmos
#Universidad Catolica De Colombia
        
    
    

