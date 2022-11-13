from random import randint
from math import inf
import problemas
from time import time

def calcular_distancia(solucion: str, problema: dict): 
    distancia = 0
    for i in range(len(solucion)-1): 
        distancia += problema[int(solucion[i])][int(solucion[i+1])]
    return distancia
    

def generar_solucion(p: dict): 
    solucion = ""
    disp = [key for key in p]
    for i in range(len(p)): 
        solucion += str(disp.pop(randint(0, len(disp)-1)))
    solucion += solucion[0]
    return solucion

def seleccion(pob: list, problema: dict, n_muestra = 2):
    solucion = ""
    dist = inf
    for i in range(n_muestra): 
        m = pob[randint(0, len(problema)-1)]
        if calcular_distancia(m, problema) <= dist: 
            dist = calcular_distancia(m, problema)
            solucion = m
            
    return solucion

def correccion(sol: str, problema: dict):
    faltan = [key for key in problema]
    sobran = []
    for s in sol: 
        if int(s) in faltan: 
            faltan.remove(int(s))
        elif int(s) not in faltan: 
            sobran.append(int(s))
    while len(sobran) > 0: 
        s = randint(0, len(sobran)-1)
        f = randint(0, len(faltan)-1)

        n = sol.find(str(sobran[s]))
        nueva_sol = sol[:n]
        nueva_sol += str(faltan[f])
        nueva_sol += sol[n+1:]
        sobran.pop(s)
        faltan.pop(f)
        sol = nueva_sol

    return sol

def cruce(p: str, m: str, problema: dict, probabilidad = 90): 
    if randint(1, 100) <= probabilidad: 
        pivot_1 = len(problema)//3
        pivot_2 = len(problema)*2//3

        h1 = p[:pivot_1]
        h1 += m[pivot_1:pivot_2]
        h1 += p[pivot_2:len(problema)]

        h2 = m[:pivot_1]
        h2 += p[pivot_1:pivot_2]
        h2 += p[pivot_2:len(problema)]
        
        h1 = correccion(h1, problema)
        h2 = correccion(h2, problema)
        h1 += h1[0]
        h2 += h2[0]
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
        nueva_solucion = solucion[:pivote_1] + solucion[pivote_2] + solucion[pivote_1+1:pivote_2] + solucion[pivote_1] + solucion[pivote_2+1:len(solucion)-1]
        nueva_solucion += nueva_solucion[0]
        return nueva_solucion
    return solucion


def genetic(problema: dict, n_gen: int, n_pob: int): 
    poblacion = [generar_solucion(problema) for i in range(n_pob)]
    
    print("Población Inicial\tDistancia")
    for individuo in poblacion: 
        print("\t"+individuo+"\t\t"+str(calcular_distancia(individuo, problema)))
    mejor_solucion = ""
    mejor_valor = inf
    
    for g in range(n_gen): 
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
        print("Mejor solución\tDistancia")
        print(mejor_solucion_local+"\t\t"+str(mejor_valor_local))
        if mejor_valor_local <= mejor_valor: 
            mejor_solucion = mejor_solucion_local
            mejor_valor = mejor_valor_local
    return mejor_solucion
    

if __name__=="__main__": 
    p = problemas.problema_3
    inicio = time()
    solucion = genetic(p, 5, 100)
    print("Tiempo de ejecución: "+str(time()-inicio))
    print("Mejor Solucion: " +str(solucion))
    print("Distancia: "+str(calcular_distancia(solucion, p)))