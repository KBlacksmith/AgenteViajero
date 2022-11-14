from random import randint
from math import inf

def calcular_distancia(solucion: list, problema: dict): 
    distancia = 0
    for i in range(len(solucion)-1): 
        distancia += problema[solucion[i]][solucion[i+1]]
    return distancia
    

def generar_solucion(p: dict): 
    disp = [key for key in p]
    ruta = []
    for i in range(len(p)): 
        ruta.append(disp.pop(randint(0, len(disp)-1)))
    ruta.append(ruta[0])
    return ruta

def seleccion(pob: list, problema: dict, n_muestra = 2):
    solucion = ""
    dist = inf
    for i in range(n_muestra): 
        m = pob[randint(0, len(problema)-1)]
        if calcular_distancia(m, problema) <= dist: 
            dist = calcular_distancia(m, problema)
            solucion = m
            
    return solucion

def correccion(sol: list, problema: dict):
    faltan = [key for key in problema]
    sobran = []
    sol.pop()
    for s in sol: 
        if s in faltan: 
            faltan.remove(s)
        elif s not in faltan and s not in sobran: 
            sobran.append(s)
    while len(sobran) > 0: 
        s = randint(0, len(sobran)-1)
        f = randint(0, len(faltan)-1)

        n = sol.index(sobran[s])

        nueva_sol = [sol[i] for i in range(n)]
        
        nueva_sol.append(faltan[f])
        
        for i in range(n+1, len(sol)): 
            nueva_sol.append(sol[i])

        sobran.pop(s)
        faltan.pop(f)
        sol = nueva_sol

    return sol

def cruce(p: list, m: list, problema: dict, probabilidad = 90): 
    if randint(1, 100) <= probabilidad: 
        pivot_1 = len(problema)//3
        pivot_2 = len(problema)*2//3

        h1 = list()
        h2 = list()
        
        for i in range(pivot_1): 
            h1.append(p[i])
            h2.append(m[i])
        for i in range(pivot_1, pivot_2): 
            h1.append(m[i])
            h2.append(p[i])
        for i in range(pivot_2, len(p)): 
            h1.append(p[i])
            h2.append(p[i])
        
        h1 = correccion(h1, problema)
        h2 = correccion(h2, problema)
        h1.append(h1[0])
        h2.append(h2[0])
        return h1, h2
    return p, m

def mutacion(solucion: str, problema: dict, probabilidad = 5): 
    if randint(1, 100) <= probabilidad: 
        pivote_1 = randint(0, len(problema)-1)
        pivote_2 = pivote_1
        while pivote_2 == pivote_1: 
            pivote_2 = randint(0, len(problema)-1)
        if pivote_2 < pivote_1: 
            temp = pivote_1
            pivote_1 = pivote_2
            pivote_2 = temp

        temp = solucion[pivote_1]
        solucion[pivote_1] = solucion[pivote_2]
        solucion[pivote_2] = temp
        solucion[len(solucion)-1] = solucion[0]
    return solucion


def genetic(problema: dict, n_gen: int, n_pob: int, explicito = False): 
    poblacion = [generar_solucion(problema) for i in range(n_pob)]
    if explicito: 
        print("Población Inicial\tDistancia")
        for individuo in poblacion: 
            print("\t"+str(individuo)+"\t\t"+str(calcular_distancia(individuo, problema)))
    mejor_solucion = ""
    mejor_valor = inf
    
    for g in range(n_gen): 
        if explicito:
            print("-"*10)
            print("Genración "+str(g+1))
        mejor_solucion_local = ""
        mejor_valor_local = inf
        padres = [seleccion(poblacion, problema) for i in range(n_pob)]
        hijos = list()
        for i in range(0, n_pob, 2): 
            padre, madre = padres[i], padres[i+1]
            for h in cruce(padre, madre, problema): 
                h = mutacion(h, problema)
                hijos.append(h)
                d = calcular_distancia(h, problema)
                #print("\t"+h+"\t\t"+str(d))
                if d <= mejor_valor_local: 
                    mejor_valor_local = d
                    mejor_solucion_local = h
        poblacion = hijos
        if explicito: 
            print("Mejor solución\tDistancia")
            print(str(mejor_solucion_local)+"\t"+str(mejor_valor_local))
        if mejor_valor_local <= mejor_valor: 
            mejor_solucion = mejor_solucion_local
            mejor_valor = mejor_valor_local
    return mejor_solucion
    

if __name__=="__main__": 
    import problemas
    from time import time
    print("Algoritmo genético")
    p = problemas.ejemplo_placa
    inicio = time()
    solucion = genetic(p, 10, 50000, True)
    print("-"*5)
    print("Tiempo de ejecución: "+str(time()-inicio))
    print("Mejor Solucion: " +str([int(s) for s in solucion]))
    print("Distancia: "+str(calcular_distancia(solucion, p)))