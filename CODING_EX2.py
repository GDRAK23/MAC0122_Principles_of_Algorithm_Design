#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Exercício Programa II – MAC 122 – PDA
# Guilherme Augusto Martins
# NUSP: 7199162

#bibilotecas usadas
import time as t
import datetime as dt

#Algoritmo de Classificação Bubble Sort
def ClassificarBolha(TAB,ordem):
    indx= {1:0,2:3,3:4}
       
    for k in ordem:
        for j in range(len(TAB) - 1):
            for i in range(len(TAB) - 1): 
                #Primeira ordenação
                if ordem.index(k)==0:
                    if TAB[i][indx.get(k)] > TAB[i+1][indx.get(k)]:
                        TAB[i], TAB[i+1] = TAB[i+1], TAB[i]     
                #Demais ordenações,mantem a ordem das colunas ja ordenadas anteriormente      
                elif ordem.index(k)==1:
                    if TAB[i][indx.get(k)] > TAB[i+1][indx.get(k)] and TAB[i][indx.get(ordem[ordem.index(k)-1])] == TAB[i+1][indx.get(ordem[ordem.index(k)-1])] :
                        TAB[i], TAB[i+1] = TAB[i+1], TAB[i]
                elif ordem.index(k)==2:
                    if TAB[i][indx.get(k)] > TAB[i+1][indx.get(k)] and TAB[i][indx.get(ordem[ordem.index(k)-1])] == TAB[i+1][indx.get(ordem[ordem.index(k)-1])] and TAB[i][indx.get(ordem[ordem.index(k)-2])] == TAB[i+1][indx.get(ordem[ordem.index(k)-2])]:
                        TAB[i], TAB[i+1] = TAB[i+1], TAB[i]                    

#Algoritmo de Classificação Quick Sort
#Define a classe pilha
class PilhaLista:
    
    def __init__(self):
        self._pilha=[]
   
    def __len__(self):
        return len(self._pilha)

    def is_empty(self):
        return len(self._pilha)==0
    
    def pop(self):
        if self.is_empty():
            raise Exception("Pilha vazia")
        return self._pilha.pop()

    def push(self,e):
        self._pilha.append(e)
    
    def top(self):
        if self.is_empty():
            raise Exception("Pilha vazia")
        return self._pilha[-1]  



#Função que particiona a tabela e coordena as ordenações em diferentes níveis
def ClassificarQuick(TAB,ordem):
    
    indx= {1:0,2:3,3:4}

#Função que particiona tabela deixando elementos menores à esquerda do pivo e maiores à direita
    def particiona(TAB, start, end,k):
        i, j = start, end
        pivo = TAB[end]
        while True:
            # Aumentando i
            while i < j and TAB[i][indx.get(k)] <= pivo[indx.get(k)]: 
                i = i + 1
            if i < j:
                TAB[i], TAB[j] = pivo, TAB[i]
                # TAB[j] é maior que o pivô – avança 1
                j = j - 1
            else: break
            # Diminuindo j
            while i < j and TAB[j][indx.get(k)] >= pivo[indx.get(k)]: 
                j = j - 1
            if i < j:
                TAB[i], TAB[j] = TAB[j], pivo
                # TAB [i] é maior que o pivô – avança 1
                i = i + 1
            else: break
        return i
    
    for k in ordem:
        #Gera as subdivisões da tabela de acordo com o nível de ordenação
        #Primeira ordenação
        if ordem.index(k)==0:
            # Cria a pilha de sub-TABs e inicia com TAB completa
            Pilha = PilhaLista()
            Pilha.push((0, len(TAB) - 1))   
            # Repete até que a pilha de sub-TABs esteja vazia
            while not Pilha.is_empty():
                start ,end = Pilha.pop()
                # Só particiona se há mais de 1 elemento
                if end - start > 0:
                    n = particiona(TAB, start, end,k)
                    # Empilhe as sub-TABs resultantes
                    Pilha.push((start, n - 1))
                    Pilha.push((n + 1, end))       
                        
        #Segunda ordenação
        if ordem.index(k)==1:
            # Cria a pilha de sub-TAB de repspeitando com a ordenação anterior
            Particoes = [(x,TAB[x][indx.get(ordem[ordem.index(k)-1])]>=TAB[x+1][indx.get(ordem[ordem.index(k)-1])]) for x in range(0,len(TAB)-1)]
            Particoes.append((len(TAB)-1,TAB[len(TAB)-2][indx.get(ordem[ordem.index(k)-1])]>=TAB[len(TAB)-1][indx.get(ordem[ordem.index(k)-1])])) 
            cont=0
            ctl=0
            Pilha = PilhaLista()
            #Gera subdivisões da tabela principal de acordo com a ordenação anterior
            while cont<len(TAB):
                if Particoes[cont][1]==True:
                    inicio = Particoes[cont][0]
                    aux= cont+1                    
                    while Particoes[aux][1]!=False:
                        aux+=1
                        if aux>=len(TAB):           
                            fim= Particoes[aux-1][0]
                            cont=aux
                            Pilha.push((inicio,fim))
                            ctl=1
                            break                  
                    if ctl !=1:    
                        fim= Particoes[aux][0]
                        cont=aux
                        Pilha.push((inicio,fim))
                else:
                    cont+=1
                                           
            PilhaAux = PilhaLista()   
            for p in range(len(Pilha)):
                PilhaAux.push(Pilha.pop())
                # Repete até que cada sub-bloco seja ordenado respeitando à ordenação anterior
                while not PilhaAux.is_empty():
                    start ,end = PilhaAux.pop()
                    # Só particiona se há mais de 1 elemento
                    if end - start > 0:
                        n = particiona(TAB, start, end,k)
                        # Empilhe as sub-TABs resultantes
                        PilhaAux.push((start, n - 1))
                        PilhaAux.push((n + 1, end))     
                    
        #Terceira ordenação
        if ordem.index(k)==2:
            # Cria a pilha de sub-TAB de acordo com a ordenação anterior
            Particoes = [(x,(TAB[x][indx.get(ordem[ordem.index(k)-1])]>=TAB[x+1][indx.get(ordem[ordem.index(k)-1])]) and (TAB[x][indx.get(ordem[ordem.index(k)-2])]>=TAB[x+1][indx.get(ordem[ordem.index(k)-2])])) for x in range(0,len(TAB)-1)]
            Particoes.append((len(TAB)-1,(TAB[len(TAB)-2][indx.get(ordem[ordem.index(k)-1])]>=TAB[len(TAB)-1][indx.get(ordem[ordem.index(k)-1])]) and (TAB[len(TAB)-2][indx.get(ordem[ordem.index(k)-2])]>=TAB[len(TAB)-1][indx.get(ordem[ordem.index(k)-2])]))) 
            cont=0
            ctl=0
            Pilha = PilhaLista()    
            #Gera subdivisões da tabela principal de acordo com a ordenação anterior
            while cont<len(TAB):
                if Particoes[cont][1]==True:
                    inicio = Particoes[cont][0]
                    aux= cont+1
                    
                    while Particoes[aux][1]!=False:
                        aux+=1
                        if aux>=len(TAB):           
                            fim= Particoes[aux-1][0]
                            cont=aux
                            Pilha.push((inicio,fim))
                            ctl=1
                            break
                    
                    if ctl !=1:    
                        fim= Particoes[aux][0]
                        cont=aux
                        Pilha.push((inicio,fim))
                else:
                    cont+=1
                              
            PilhaAux = PilhaLista()   
            for p in range(len(Pilha)):
                PilhaAux.push(Pilha.pop())
                # Repete até que cada sub-bloco seja ordenado respeitando às ordenaçõesanterior
                while not PilhaAux.is_empty():
                    start ,end = PilhaAux.pop()
                    # Só particiona se há mais de 1 elemento
                    if end - start > 0:
                        n = particiona(TAB, start, end,k)
                        # Empilhe as sub-TABs resultantes
                        PilhaAux.push((start, n - 1))
                        PilhaAux.push((n + 1, end))    

#Algoritmo de Classificação Tim Sort(intrínseco do python)
def ClassificarSort(TAB,ordem):
    indx= {1:0,2:3,3:4}
    TAB.sort(key=lambda tab: (tab[indx.get(ordem[0])],tab[indx.get(ordem[1])],tab[indx.get(ordem[2])]))

#Função que trata as nomes
def tratanome(string):
    return string.lower()

#Função que trata as datas
def tratadata(data):
    return dt.date(int(data[6:10]),int(data[3:5]),int(data[0:2]))

while True:
    
    filename = input("Entre com o nome do arquivo de origem:\n")
    if filename == 'fim':
        break
    
    #abre o arquivo
    file = open(filename,'r')
    tab= []
    row=0
    #lê o arquivo linha a linha e coloca na tabela tab
    while row != "":
        row = file.readline()
        if len (row)>1:
            tab.append(row.split(',') )
    #fecha o arquivo
    file.close()

    #cria coluna auxiliar de nome
    [tab[k].append(tratanome(tab[k][1])) for k in range(len(tab))]
    #cria coluna auxiliar de data
    [tab[k].append(tratadata(tab[k][2])) for k in range(len(tab))]
    
    while True:
    
        #cria cópias auxiliares da tabela original
        tab1 = tab.copy()
        tab2 = tab.copy()
        tab3 = tab.copy()
        
        ordem = input("Entre com a ordem de classificação:\n")
        if ordem == 'fim':
            break
        
        ordem = list(ordem)
        for numero in ordem:
            ordem[ordem.index(numero)]=int(ordem[ordem.index(numero)])
        
        #Classifica pelo intrínseco do Python, mostra tempo decorrido
        now = t.time()
        ClassificarSort(tab1,ordem)
        print("Tempo de classificação Sort() =","{:.20f}\n".format(t.time()-now))
        
        #Classifica pela Bolha, mostra tempo decorrido
        now = t.time()
        ClassificarBolha(tab2,ordem)
        print("Tempo de classificação Bolha() =","{:.20f}".format(t.time()-now))
        if tab1==tab2:print("*** Classificação correta\n")
        
        #Classifica pelo Quick
        now = t.time()
        ClassificarQuick(tab3,ordem)
        print("Tempo de classificação Quick() = ", "{:.20f}".format(t.time()-now))
        if tab1==tab3:print("*** Classificação correta\n")
