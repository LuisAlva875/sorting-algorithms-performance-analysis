import random # libreria para generar el arreglo random
import math # libreria para dividir merge en enteros
import time # libreria para calcular tiempos de ejecucion


def BubbleSort (A): # definicion de la funcion bubble
    
    n = len (A) # pasa arreglo 
    comparacion=0 # inicia contador

    for i in range (1, n):
        for j in range (0, n-i):
            comparacion+=1
            if A [j] > A [j+1]: # verifica que sea anterior sea menor a despues
                aux = A [j] # define auxiliar
                A [j] = A [j+1] 
                A [j+1] = aux # cambian posicion
    
    print("Comparaciones realizadas: ", comparacion)


def BubbleSort_Optimizado( A ): #define la funcion bubble optimizadp

    bandera=True # variable vandera para verficicar correctos
    pasada=0 #inicia el contador

    while pasada<len(A)-1 and bandera:
        bandera =False # detiene si estan en orden
        for j in range (len(A)-1-pasada):
            if(A[j]>A[j+1]): # verifica que sean menor a despues
                bandera=True
                temp=A[j] #toma el valor para cambio
                A[j]=A[j+1] #cambia
                A[j+1]=temp #pone en posicion
        pasada=pasada+1
    
    print("Comparaciones realizadas: ", pasada)


def Merge(A, iInicio, q, iFinal): # funcion merge

    global comparaciones # contador
    x = q - iInicio + 1
    y = iFinal- q 
  
    izq = [0] * (x) # arreglo temporal
    der = [0] * (y) 
  
    for i in range(0 , x): # Toma los datos divididos en los arreglos
        izq[i] = A[iInicio + i] 
  
    for j in range(0 , y): # Toma los datos divididos en los arreglos
        der[j] = A[q + 1 + j] 
  
    i = 0     # primera posicion del primer arreglo
    j = 0     # primera posicion del segundo arreglo
    k = iInicio     # Iprimera posicion del arreglo convinado
    comparaciones=0 # inicia contador
  
    while i < x and j < y : # cambia posiciones
        comparaciones += 1 # imcrementa contador
        if izq[i] <= der[j]: 
            A[k] = izq[i] 
            i += 1
        else: 
            A[k] = der[j] 
            j += 1
        k += 1
  
    while i < x: # copia elementos restantes de lado izquierdo
        A[k] = izq[i] 
        i += 1
        k += 1
  
    while j < y: #copia elementos restantes de lado derecho
        A[k] = der[j] 
        j += 1
        k += 1
 
def MergeSort(A,iInicio,iFinal): 

    if iInicio < iFinal: 

        q = math.floor ((iInicio+(iFinal-1))/2) # divide los elementos en enteros
  
        MergeSort(A, iInicio, q) # ordena la primera y segunda mitad
        MergeSort(A, q+1, iFinal) 
        Merge(A, iInicio, q, iFinal)


def OrdenadaAsc(lista): # funcion para verificar el orden

    ordenada = True
    for i in range(1, len(lista)): # pasa las posiciones
        if lista[i] < lista[i - 1]: # revisa la lista
            ordenada = False
            break
    return ordenada


elementos = 10
lista = []
lista1 = []
lista2 = []  

for i in range (elementos): # genera las listas aleatorias
    lista.append (random.randint (0,9))
    lista1.append (random.randint (0,9))
    lista2.append (random.randint (0,9))

print("Para una lista de ", elementos, "elementos\n")

print (">>> METODO BUBBLE SORT<<<\n")

print("Caso Promedio\n")
tInicial = time.time () # inicia tiempo
BubbleSort (lista) # llama funcion
tFinal=time.time () # cierra tiempo
if not OrdenadaAsc(lista): # verifica orden
    print("Correcta = FALSE")
else:
    print("Correcta = TRUE")
print ("Tiempo = ", tFinal-tInicial)
print ("")

print("Mejor Caso\n")
tInicial = time.time () #inicia tiempo
BubbleSort (lista) # llama funcion
tFinal=time.time () # cierra tiempo
if not OrdenadaAsc(lista): # verifica orden
    print("Correcta = FALSE")
else:
    print("Correcta = TRUE")
print ("Tiempo = ", tFinal-tInicial)
print ("")

print("Peor Caso\n")
lista.reverse() # hace la lista al revez
tInicial = time.time () # inicia tiempo
BubbleSort (lista) # llama a la funcion
tFinal=time.time () # cierra tiempo
if not OrdenadaAsc(lista): # verifica orden
    print("Correcta = FALSE")
else:
    print("Correcta = TRUE")
print ("Tiempo = ", tFinal-tInicial)
print ("")


print (">>> METODO BUBBLE SORT OPTIMIZADO <<<\n")

print("Caso Promedio\n")
tInicial = time.time ()# inicia tiempo
BubbleSort_Optimizado (lista1)# llama funcion
tFinal=time.time () #cierra tiempo
if not OrdenadaAsc(lista1): # verifica orden
    print("Correcta = FALSE")
else:
    print("Correcta = TRUE")
print ("Tiempo = ", tFinal-tInicial)
print ("")

print("Mejor Caso\n")

tInicial = time.time () # inicia tiempo
BubbleSort_Optimizado (lista1) # llama a la funcion
tFinal=time.time () #cierra tiempo
if not OrdenadaAsc(lista1):# verfics orden
    print("Correcta = FALSE")
else:
    print("Correcta = TRUE")
print ("Tiempo = ", tFinal-tInicial)
print ("")

print("Peor Caso\n")

lista.reverse() # hace la inversa de la lista
tInicial = time.time ()# inicia tiempo
BubbleSort_Optimizado (lista1) # llama funcion
tFinal=time.time () # tiempo final
if not OrdenadaAsc(lista1): # verifica orden
    print("Correcta = FALSE")
else:
    print("Correcta = TRUE")
print ("Tiempo = ", tFinal-tInicial)
print ("")


A = lista2
n = len(A) 

print (">>> METODO MERGE SORT <<<\n")   

print("Caso Promedio\n")
tInicial = time.time ()# inicia tiempo
MergeSort(A,0,n-1)# llama funcion
tFinal=time.time ()# termina tiempo
print ("Comparaciones realizadas:", comparaciones)  
if not OrdenadaAsc(lista2):# verifica el orden
    print("Correcta = FALSE")
else:
    print("Correcta = TRUE")
print ("Tiempo = ", tFinal-tInicial)
print ("")

print("Mejor Caso\n")
tInicial = time.time ()# inicia tiempo
MergeSort(A,0,n-1)# llama funcion
tFinal=time.time ()# cierra tiempo
print ("Comparaciones realizadas:", comparaciones)  
if not OrdenadaAsc(lista2):# verifica el orden
    print("Correcta = FALSE")
else:
    print("Correcta = TRUE")
print ("Tiempo = ", tFinal-tInicial)
print ("")

print("Peor Caso\n")
lista.reverse() # hace la lista al revez
tInicial = time.time () #inicia tiepo
MergeSort(A,0,n-1) # llama a la funcion
tFinal=time.time () # termina tiempo
print ("Comparaciones realizadas:", comparaciones)  
if not OrdenadaAsc(lista2): # verifica el orden
    print("Correcta = FALSE")
else:
    print("Correcta = TRUE")
print ("Tiempo = ", tFinal-tInicial)