from math import inf

def calcular_distancia(ruta: list, problema: dict): 
    distancia = 0
    nodo_actual = ruta[0]
    for i in range(len(ruta)-1):
        #print(i+1)
        distancia += problema[nodo_actual][ruta[i+1]]
        nodo_actual = ruta[i+1]
    return distancia

def probar_caminos(problema: dict, disp: list, ruta = [])->list:

    if len(disp) == 0: 
        ruta.append(ruta[0])
        return ruta
        

    mejor_ruta = []
    menor_distancia = inf
    for nodo in disp: 
        ruta.append(nodo)
        #print(ruta)
        temp_d = disp.copy()
        temp_d.remove(nodo)
        r = probar_caminos(problema, temp_d, ruta.copy())
        distancia = calcular_distancia(r, problema)
        if distancia <= menor_distancia: 
            mejor_ruta = r.copy()
            menor_distancia = distancia
        ruta.pop()
    return mejor_ruta
if __name__ == "__main__": 
    import problemas
    from time import time
    print("Fuerza bruta")
    p = problemas.problema_2
    disponibles = [key for key in p]
    inicio = time()
    ruta = probar_caminos(p, disponibles)
    print("Tiempo de ejecución: "+str(time()-inicio))
    print("Mejor ruta: "+str(ruta))
    print("Distancia: "+str(calcular_distancia(ruta, p)))