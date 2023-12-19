# -*- coding: utf-8 -*-

"""
Mover n discos de ORIGEM para DESTINO, é o mesmo que:
1-Mover n-1 discos de ORIGEM para AUXILIAR, usando DESTINO como auxiliar
2-Mover disco n de ORIGEM para DESTINO
3-Mover n-1 discos de AUXILIAR para DESTINO, usando ORIGEM como auxiliar

"""

def Movimente(k,origem,destino):
    print("mover disco ",k,"da torre ",origem," para a torre " , destino)
    hastes[destino].append(hastes[origem].pop())
    print(hastes)
    


def Hanoi(n,torreA,torreB,torreAux):
    if n==1:
        Movimente(1,torreA,torreB)
    else:
        
        Hanoi(n-1, torreA, torreAux, torreB)
        
        Movimente(n,torreA,torreB)
        
        Hanoi(n-1,torreAux,torreB,torreA)
    

hastes = [[],[],[]]
n=4
for i in range(n,0,-1):
    hastes[0].append(i)

Hanoi(n,0,1,2)
