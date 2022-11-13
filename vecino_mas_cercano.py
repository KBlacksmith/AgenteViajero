from math import inf
from random import randint
import problemas
from time import time

def calcular_distancia(ruta: list, problema: dict): 
    distancia = 0
    nodo_actual = ruta[0]
    for i in range(len(ruta)-1):
        #print(i+1)
        distancia += problema[nodo_actual][ruta[i+1]]
        nodo_actual = ruta[i+1]
    return distancia

def vecino(problema: dict, disponibles: list, inicio: int): 
    nodo_actual = inicio
    ruta = [inicio]
    disponibles.remove(inicio)
    while len(disponibles) > 0: 
        vecino_mas_cercano = 0
        dist = inf
        #print(problema[nodo_actual])
        for v in disponibles: 
            if v != nodo_actual: 
                if problema[nodo_actual][v] <= dist: 
                    dist = problema[nodo_actual][v]
                    vecino_mas_cercano = v
        ruta.append(vecino_mas_cercano)
        disponibles.remove(vecino_mas_cercano)
    ruta.append(inicio)
    return ruta

if __name__ == "__main__": 
    p = problemas.problema_3
    disponibles = [key for key in p]
    inicio = randint(0, len(disponibles)-1)
    print("Punto de partida: "+str(inicio))
    t = time()
    ruta = vecino(p, disponibles, inicio)
    print("Tiempo de ejecución: "+str(time()-t))
    print("Ruta: "+str(ruta))
    print("Distancia: "+str(calcular_distancia(ruta, p)))