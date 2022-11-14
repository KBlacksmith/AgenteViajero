from math import inf
from random import randint

#ALGUNOS PROBLEMAS DE EJEMPLO

problema_1 = {
    0: {0: 0, 1: 10, 2: 15, 3: 20},
    1: {0: 5, 1: 0, 2: 9, 3: 10},
    2: {0: 6, 1: 13, 2: 0, 3: 12},
    3: {0: 8, 1: 8, 2: 9, 3: 0}
}

problema_2 = {
    0: {0: 0, 1: 12, 2: 10, 3: 19, 4: 8}, 
    1: {0: 12, 1: 0, 2: 3, 3: 7, 4: 6},
    2: {0: 10, 1: 3, 2: 0, 3: 2, 4: 20},
    3: {0: 19, 1: 7, 2: 2, 3: 0, 4: 4}, 
    4: {0: 8, 1: 6, 2: 20, 3: 4, 4: 0}
}

problema_3 = {
    0: {0: 0, 1: 12, 2: 10, 3: inf, 4: inf, 5: inf, 6: 12}, 
    1: {0: 12, 1: 0, 2: 8, 3: 12, 4: inf, 5: inf, 6: inf}, 
    2: {0: 10, 1: 8, 2: 0, 3: 11, 4: 3, 5: inf, 6: 9}, 
    3: {0: inf, 1: 12, 2: 11, 3: 0, 4: 11, 5: 10, 6: inf},
    4: {0: inf, 1: inf, 2: 3, 3: 11, 4: 0, 5: 6, 6: 7}, 
    5: {0: inf, 1: inf, 2: inf, 3: 10, 4: 6, 5: 0, 6: 9}, 
    6: {0: 12, 1: inf, 2: 9, 3: inf, 4: 7, 5: 9, 6: 0}, 
}

problema_4 = {
    0: {0: 0, 1: 13, 2: 25, 3: 15, 4: 21, 5: 9, 6: 19, 7: 18, 8: 8, 9: 15}, 
    1: {0: 13, 1: 0, 2: 26, 3: 21, 4: 29, 5: 21, 6: 31, 7: 23, 8: 16, 9: 10}, 
    2: {0: 25, 1: 26, 2: 0, 3: 11, 4: 18, 5: 23, 6: 28, 7: 44, 8: 34, 9: 35}, 
    3: {0: 15, 1: 21, 2: 11, 3: 0, 4: 10, 5: 13, 6: 19, 7: 34, 8: 24, 9: 29}, 
    4: {0: 21, 1: 29, 2: 18, 3: 10, 4: 0, 5: 12, 6: 11, 7: 37, 8: 27, 9: 36}, 
    5: {0: 9, 1: 21, 2: 23, 3: 13, 4: 12, 5: 0, 6: 10, 7: 25, 8: 14, 9: 25}, 
    6: {0: 19, 1: 31, 2: 28, 3: 19, 4: 11, 5: 10, 6: 0, 7: 32, 8: 23, 9: 35}, 
    7: {0: 18, 1: 23, 2: 44, 3: 34, 4: 37, 5: 25, 6: 32, 7: 0, 8: 10, 9: 16}, 
    8: {0: 8, 1: 16, 2: 34, 3: 24, 4: 27, 5: 14, 6: 23, 7: 10, 8: 0, 9: 14},
    9: {0: 15, 1: 10, 2: 35, 3: 29, 4: 36, 5: 25, 6: 35, 7: 16, 8: 14, 9: 0}, 
}

#EJEMPLOS PARA CLASE

ejemplo_placa = {
    "A": {"A": 0, "B": 80, "C": 55, "D": inf, "E": inf, "F": inf, "G": inf, "H": inf, "I": inf, "J": inf, "K": inf, "L": 50}, 
    "B": {"A": 80, "B": 0, "C": 60, "D": 80, "E": inf, "F": inf, "G": inf, "H": inf, "I": inf, "J": inf, "K": inf, "L": inf}, 
    "C": {"A": 55, "B": 60, "C": 0, "D": 55, "E": inf, "F": inf, "G": inf, "H": inf, "I": inf, "J": inf, "K": inf, "L": inf}, 
    "D": {"A": inf, "B": 80, "C": 55, "D": 0, "E": 25, "F": 20, "G": 35, "H": inf, "I": inf, "J": inf, "K": inf, "L": 50}, 
    "E": {"A": inf, "B": inf, "C": inf, "D": 25, "E": 0, "F": 20, "G": 20, "H": inf, "I": inf, "J": inf, "K": 20, "L": 35}, 
    "F": {"A": inf, "B": inf, "C": inf, "D": 20, "E": 20, "F": 0, "G": 20, "H": inf, "I": inf, "J": inf, "K": inf, "L": inf}, 
    "G": {"A": inf, "B": inf, "C": inf, "D": 35, "E": 20, "F": 20, "G": 0, "H": 20, "I": inf, "J": inf, "K": inf, "L": inf}, 
    "H": {"A": inf, "B": inf, "C": inf, "D": inf, "E": inf, "F": inf, "G": 20, "H": 0, "I": 10, "J": 15, "K": inf, "L": inf}, 
    "I": {"A": inf, "B": inf, "C": inf, "D": inf, "E": inf, "F": inf, "G": inf, "H": 10, "I": 0, "J": 10, "K": inf, "L": inf}, 
    "J": {"A": inf, "B": inf, "C": inf, "D": inf, "E": inf, "F": inf, "G": inf, "H": 15, "I": 10, "J": 0, "K": 10, "L": 30}, 
    "K": {"A": inf, "B": inf, "C": inf, "D": inf, "E": 20, "F": inf, "G": inf, "H": inf, "I": inf, "J": 10, "K": 0, "L": 25}, 
    "L": {"A": 50, "B": inf, "C": inf, "D": 50, "E": 35, "F": inf, "G": inf, "H": inf, "I": inf, "J": 30, "K": 25, "L": 0}
}

#for i in ejemplo_placa: 
#    for j in ejemplo_placa: 
#        print("i: "+str(i)+", j: "+str(j))
#        if ejemplo_placa[i][j] != ejemplo_placa[j][i]: 
#            print("i: "+str(i)+", j: "+str(j))

#FUNCION PARA EVALUAR UN RUTA EN PARTICULAR

def calcular_distancia(ruta: list, problema: dict): 
    if len(ruta) == 0: 
        return inf
    distancia = 0
    nodo_actual = ruta[0]
    for i in range(len(ruta)-1):
        distancia += problema[nodo_actual][ruta[i+1]]
        nodo_actual = ruta[i+1]
    return distancia

#METODO DE RAMIFICACION Y ACOTAMIENTO

def ramificar_acotar(problema: dict, disp: list, ruta = [], alfa = inf)->list:
    if len(disp) == 0: 
        ruta.append(ruta[0])
        return ruta
    mejor_ruta = []
    menor_distancia = inf
    for nodo in disp: 
        ruta.append(nodo)
        if calcular_distancia(ruta, problema) >= alfa:
            break
        temp_d = disp.copy()
        temp_d.remove(nodo)
        r = ramificar_acotar(problema, temp_d, ruta.copy(), alfa)
        
        distancia = calcular_distancia(r, problema)
        alfa = min(alfa, distancia)
        if distancia <= menor_distancia: 
            mejor_ruta = r.copy()
            menor_distancia = distancia
        ruta.pop()
    return mejor_ruta

#MÉTODO DEL VECINO MÁS CERCANO

def vecino_mas_cercano(problema: dict, disponibles: list): 
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


#ALGORITMO GENÉTICO

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

def algoritmo_genetico(problema: dict, n_gen: int, n_pob: int, explicito = False): 
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
        print("\nGeneración #" + str(g+1))
        print("Solución: "+str(mejor_solucion_local))
        print("Valor: "+str(mejor_valor_local))
    return mejor_solucion

if __name__=="__main__": 
    from time import time
    p = ejemplo_placa
    #print("Fuerza bruta: ")
    #t = time()
    #ruta = probar_caminos(p, [key for key in p])
    #print("Tiempo de ejecución: "+str(time()-t))
    #print("Solución Óptima: "+str(ruta))
    #print("Valor Óptimo: "+str(calcular_distancia(ruta, p)))
    print("-"*5)
    print("Ramificación y acotamiento: ")
    t = time()
    ruta = ramificar_acotar(p, [key for key in p])
    print("Tiempo de ejecución: "+str(time()-t))
    print("Solución Óptima: "+str(ruta))
    print("Valor Óptimo: "+str(calcular_distancia(ruta, p)))

    print("-"*5)
    print("Vecino más cercano: ")
    t = time()
    ruta = vecino_mas_cercano(p, [key for key in p])
    print("Tiempo de ejecución: "+str(time()-t))
    print("Solución: "+str(ruta))
    print("Valor: "+str(calcular_distancia(ruta, p)))
    
    print("-"*5)
    print("Alforitmo genetico: ")
    t = time()
    ruta = algoritmo_genetico(p, 5, 100)
    print("\nTiempo de ejecución: "+str(time()-t))
    print("Solución: "+str(ruta))
    print("Valor: "+str(calcular_distancia(ruta, p)))
