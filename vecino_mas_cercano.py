from math import inf
from random import randint


def calcular_distancia(ruta: list, problema: dict): 
    if len(ruta) == 0: 
        return inf
    distancia = 0
    nodo_actual = ruta[0]
    for i in range(len(ruta)-1):
        #print(i+1)
        distancia += problema[nodo_actual][ruta[i+1]]
        nodo_actual = ruta[i+1]
    return distancia

def vecino(problema: dict, disponibles: list): 
    mejor_ruta = []
    menor_distancia = inf
    for key in problema: 
        disponibles = [i for i in problema]
        nodo_actual = key
        ruta = [key]
        disponibles.remove(key)

        while len(disponibles) > 0: 
            vecino_mas_cercano = 0
            dist = inf

            for v in disponibles: 
                if v != nodo_actual: 
                    if problema[nodo_actual][v] <= dist: 
                        dist = problema[nodo_actual][v]
                        vecino_mas_cercano = v
            ruta.append(vecino_mas_cercano)
            disponibles.remove(vecino_mas_cercano)
        ruta.append(key)
        if calcular_distancia(ruta, problema) <= menor_distancia: 
            mejor_ruta = ruta.copy()
            menor_distancia = calcular_distancia(mejor_ruta, problema)
    return mejor_ruta

if __name__ == "__main__": 
    import problemas
    from time import time
    print("Vecino más cercano")
    p = problemas.ejemplo_placa
    disponibles = [key for key in p]
    t = time()
    ruta = vecino(p, disponibles)
    print("Tiempo de ejecución: "+str(time()-t))
    print("Ruta: "+str(ruta))
    print("Distancia: "+str(calcular_distancia(ruta, p)))