import random
import time

def ordenamientoSort(listas,TamLista):
    Tiempo_inicia = time.clock()
    for j in range(TamLista):
        inicial = listas[j]
        ubicacion = j-1
        while(ubicacion >= 0 and listas[ubicacion] > inicial):
            listas[ubicacion + 1] = listas[ubicacion]
            ubicacion += -1
        listas[ubicacion + 1] = inicial
    print listas
    Tiempo_Termina = time.clock()
    print"Tiempo Ordenamamiento: %f"%(Tiempo_Termina - Tiempo_inicia)
    
    
def reset():
    TamLista = input("INGRESE TAMAÑO DE NUMEROS A ORDENAR EJ:10-100-1000\n")
    listas = []
    Tiempo_inicia1 = time.clock()
    for i in range(TamLista):
        listas.append(random.randint(0,(TamLista*10)))
    print listas
    Tiempo_inicia = time.clock()
    Tiempo_Termina1 = time.clock()
    
    print ("LISTA ORDENADA")
    ordenamientoSort(listas,TamLista)
    print"Tiempo llenado Lista Con Random: %f"%(Tiempo_Termina1 - Tiempo_inicia1)
   
    
    reset()

reset()



               



#Misael Armando Gutierrez Gutierrez
#Codigo: 625120
#Analisis y Diseño De Algoritmos
#Universidad Catolica De Colombia
        
    
    

