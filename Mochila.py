# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 10:50:22 2019

@author: Manuel
"""

def calcular_mochila(peso_maximo, *monton):
    numobj=0
    numobjquedarse=0
    valpess=[]
    mochila=[]
    quedarse=[]
    descartes=[]
    dejar=[]
    for objeto in monton:
        valpes=objeto["valor"]/objeto["peso"] #valpes calcula la relación entre el valor y el peso.
        objeto["valpes"]=valpes
        valpess.append(valpes)
        numobj+=1
    valpess.sort() #Esto permitirá empezar por los objetos más valiosos.
    while numobj != 0:
        obj_prueba=valpess.pop()
        for objeto in monton:
            if obj_prueba==objeto["valpes"]:
                objeto["valpes"]=-1 #Esto evita problemas cuando hay más de un objeto con el mismo valor de valpes.
                if peso_maximo>=objeto["peso"]:
                    quedarse.append(objeto)
                    numobjquedarse+=1
                    peso_maximo-=objeto["peso"]               
                else: #Para, cuando esté casi llena, comparar el valor de los últimos objetos a meter.
                    if numobjquedarse!=0: #Esto es por si el objeto más valioso es muy grande y no se puede llevar, que no se saque de una lista vacía.
                        comparar=quedarse.pop()
                        peso_maximo+=comparar["peso"]
                        if peso_maximo >= objeto["peso"]:
                            if comparar["valor"] > objeto["valor"]:
                                quedarse.append(comparar)
                                numobjquedarse+=1
                                peso_maximo-=comparar["peso"]
                                dejar.append(objeto)
                            else:
                                quedarse.append(objeto)
                                numobjquedarse+=1
                                peso_maximo-=objeto["peso"]
                                dejar.append(comparar)
                        else:
                            quedarse.append(comparar)
                            numobjquedarse+=1
                            peso_maximo-=comparar["peso"]
                            dejar.append(objeto)

                    else:
                        dejar.append(objeto)
        numobj-=1
    
    valor_llevo=0
    peso_llevo=0
    valor_dejo=0
    peso_dejo=0
    
    for objeto in quedarse:
        mochila.append(objeto["nombre"])
        valor_llevo+=objeto["valor"]
        peso_llevo+=objeto["peso"]
    for objeto in dejar:
        descartes.append(objeto["nombre"])
        valor_dejo+=objeto["valor"]
        peso_dejo+=objeto["peso"]
    
    
    print("En la mochila me llevo los siguientes objetos: ",mochila, ",con un valor total de",valor_llevo,"y un peso de",peso_llevo)
    print("Dejo los siguientes objetos: ",descartes, ",con un valor total de",valor_dejo,"y un peso de",peso_dejo)
        
#Ahora una prueba con diferentes objetos
moneda={"nombre":"moneda","peso":1,"valor":3}
piedra={"nombre":"piedra","peso":5,"valor":1}
anillo={"nombre":"anillo","peso":1,"valor":10}
talisman={"nombre":"talismán","peso":4,"valor":10}
estatua={"nombre":"estatua","peso":10,"valor":100}
corona={"nombre":"corona","peso":3,"valor":100}
amuleto={"nombre":"amuleto","peso":1,"valor":1}

calcular_mochila(5,moneda, piedra, anillo, talisman, estatua,corona,amuleto)