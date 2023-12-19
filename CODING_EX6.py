# -*- coding: utf-8 -*-


import time as t

#Algoritmo de contagem normal com deslocamento 1
def bpNORMAL(a, b):
    #Tamanho das strings e texto
    m, n = len(a), len(b)
    conta = 0
    #Laço que compara a string com o texto em deslocamento de tamanho 1
    for k in range(n - m + 1):
        i, j = 0, k
        #Enquanto estiver dentro da string compara termo a termo
        while i < m:
            if a[i] != b[j]: break
            i, j = i + 1, j + 1
        if i == m: conta += 1
    return conta

#Algoritmo de Boyer Moore versão 1
def bpBM1(a, b):
    m, n = len(a), len(b)
    conta = 0
    # tabela de últimas ocorrências de cada caractere em a
    ult = [-1] * 256
    # varrer a e definir as últimas ocorrências de cada caractere
    for k in range(m): ult[ord(a[k])] = k
    # procura a em b - da esquerda para a direita
    k = m - 1
    while k < n:
        j, i = k, m - 1
        while i >= 0:
            if a[i] != b[j]: break
            j, i = j - 1, i - 1
        # comparação chegou ao fim
        if i < 0: conta += 1
        # caso particular - se k é n-1 (último de b)
        # então k+1 é índice inválido
        # o if abaixo evita esse caso
        if k + 1 >= n: break
        # desloca baseado no valor de b[k+1]
        k = k + m - ult[ord(b[k+1])]
    return conta

while True:
    #Recebe nome de arquivo a ser percorrido
    filename = input("Entre com o nome de arquivo de texto:\n");
    
    if filename == 'fim':
         break     
    #abre o arquivo
    file = open(filename,'r');
    #aloca em uma única string
    text=file.read();
    #fecha o arquivo
    file.close();
    
    while True:
        #Recebe a palavra a ser buscada
        wort = input("Entre com a palavra a procurar:\n");
        if wort == 'fim':
         break
         
        #count do python
        now = t.time();
        contagem=text.count(wort);
        end= t.time()-now;
        print("count: Encontrada " + str(contagem) +" vezes em " + str(end) + " segundos");
        
        #método normal
        now = t.time();
        contagem=bpNORMAL(wort,text);
        end= t.time()-now;
        print("Normal: Encontrada " + str(contagem) +" vezes em " + str(end) + " segundos");
                        
        #método Boyer Moore versão 1
        now = t.time();
        contagem=bpBM1(wort,text);
        end= t.time()-now;
        print("BM1: Encontrada " + str(contagem) +" vezes em " + str(end) + " segundos");
        
