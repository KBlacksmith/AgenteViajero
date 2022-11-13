from math import inf
import problemas

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
        

    peor_ruta = []
    mayor_distancia = -inf
    for nodo in disp: 
        ruta.append(nodo)
        temp_d = disp.copy()
        temp_d.remove(nodo)
        r = probar_caminos(problema, temp_d, ruta.copy())
        distancia = calcular_distancia(r, problema)
        if distancia > mayor_distancia: 
            peor_ruta = r.copy()
            mayor_distancia = distancia
        ruta.pop()
    return peor_ruta
if __name__ == "__main__": 
    print("Peor solucion")
    p = problemas.problema_4
    disponibles = [key for key in p]
    ruta = probar_caminos(p, disponibles)
    print("Peor ruta: "+str(ruta))
    print("Distancia: "+str(calcular_distancia(ruta, p)))