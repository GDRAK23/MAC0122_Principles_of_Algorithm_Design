#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Exercício Programa III – MAC 122 – PDA
# Guilherme Augusto Martins
# NUSP: 7199162

#Função que trata as nomes
def tratanome(string):
    return string.lower();

#Função que determina se x e y são primos entre si
def primos(x,y):
    mfc=1;
    for i in range(1,x+1):
        if x%i==0 and y%i==0:
            mfc=i;
    return mfc==1;

#Devolve hash de acordo com o tamanho da string e da tabela
def hash(word,size):
    k = len(word);
    return (k*23 +k*29)%size;

#Cria a segunda função de hash de acordo com o tamanho da tabela, onde
#o valor da segunda hash e da tabela são primos entre si
def hash_2(tab):
    k=2;
    while k<len(tab):
        if primos(k,len(tab)):
            break;
        k=k+1;
    return k;

#Função que insere elementos na tabela hash de acordo com as funções hash acima descritas
#bem como o índice onde o elemento ocorre para posterior exibição destes
def insere_hash(a,x,p):
    #parâmetros iniciais
    M = len(a);
    cont = 0;
    i = hash(x, M);
    k = hash2;
    #procura a próxima posição livre
    while a[i] != None:
        if a[i][0] == x: 
            #guarda linha onde o encontrou
            a[i].append(p);
            #valor já existente na tabela
            return -1;
        #conta os elementos da tabela
        cont += 1; 
        #tabela cheia
        if cont == M: return -2 ;
        #obtém próximo indice de acordo com as funções de hash
        i = (i + k) % M; 
    #achamos uma posição livre - coloque x nesta posição
    a[i] = [x];
    #guarda primeira linha onde achou x
    a[i].append(p);
    return i

#Função que busca elementos na tabela hash criada
def busca_hash(a, x):
    #parâmetros iniciais
    M = len(a);
    cont = 0;
    i = hash(x, M);
    k = hash2;
    # procura x a partir da posição i
    #Se não encontrou na primeira iteração
    if a[i]==None:
        i=-1;
        cont=0;
        return i,cont;
    
    #enquanto não encontrar
    while a[i][0] != x:
        #obtém próximo indice de acordo com as funções de hash
        i = (i + k) % M; 
        #se caiu numa casela vazia
        if a[i] == None: 
            i=-1;
            cont=0;
            return i,cont;
        #conta os elementos da tabela
        cont += 1;
        #tabela cheia
        if cont == M: 
            i=-2;
            cont=0;
            return i,cont;

    #saiu do while então encontrou
    return i,cont;

#Laço principal
while True:
    
    #obtém nome do arquivo
    filename = input(">>>Entre com o nome do arquivo de origem:\n");
    if filename == 'fim':
        break
  
    #abre o arquivo
    file = open(filename,'r')
    tab= [];
    row=0;
    #lê o arquivo linha a linha e coloca na tabela tab
    while row != "":
        row = file.readline()
        if len (row)>1:
            tab.append(row.split(','));
    #fecha o arquivo
    file.close();
     
    #cria a segunda função de hash conforme o tamanho da tabela
    hash2=hash_2(tab);
    
    #cria coluna auxiliar de nome
    [tab[k].append(tratanome(tab[k][1])) for k in range(len(tab))];
    #separando os nomes
    [tab[k].append(tab[k][3].split()) for k in range(len(tab))];  
    #cria tabela hash
    tab_hash = [None]*5*len(tab);
    
    #insere nomes na tabela criada, conforme funções supradefinidas
    for p in range(len(tab)):
        for x in tab[p][4]:
            insere_hash(tab_hash,x,p);
    
    #laço de busca na tabela
    while True:
        #obtém valor a buscar
        name= input(">>>Entre com um valor para localizar:\n");
        if name=='fim':
            break
        print('\n');
        #coloca em minúsculas
        name= tratanome(name);
        #procura na tabela
        pos,comp=busca_hash(tab_hash,name);
        #se achou imprime as linhas onde está e quantas comparações foram feitas para acha-lo
        if pos != -1:
            for n in range(len(tab_hash[pos])-1):
                string=tab[tab_hash[pos][1+n]];
                print(string[0]+","+string[1]+","+string[2]);
            print("*** "+str(comp)+" comparações para localizar os nomes\n");
        #se não achou devolve mensagem    
        else:
            print(">>>Elemento "+name+" não encontrado na tabela\n");
