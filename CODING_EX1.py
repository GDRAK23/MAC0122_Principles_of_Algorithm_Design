#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Função que devolve o máximo divisor comum entre dois números
def mdc(x,y):  
    resto = x%y
    while resto !=0:
        x=y
        y=resto
        resto = x%y    
    return y

#Define a classe fração
class Fração:
    
    #inicializa a classe    
    def __init__(self,a,b):        
        if b==0:
            raise ValueError("Denominador nulo")
        self._num=a
        self._den=b
    
    #redefine a soma
    def __add__(self,fra2):     
        anum = (self._num*fra2._den+fra2._num*self._den)
        aden = (self._den*fra2._den)
        amdc = mdc(anum,aden)
        return Fração(anum//amdc,aden//amdc)
    
    #redefine a subtração
    def __sub__(self,fra2):       
        snum = (self._num*fra2._den-fra2._num*self._den)
        sden = (self._den*fra2._den)
        smdc = mdc(snum,sden)
        return Fração(snum//smdc,sden//smdc)    

    #redefine a multiplicação
    def __mul__(self,fra2):       
        mnum = (self._num*fra2._num)
        mden = (self._den*fra2._den)
        mmdc = mdc(mnum,mden)
        return Fração(mnum//mmdc,mden//mmdc)    
    
    #redefine a divisão real                
    def __truediv__(self,fra2):
        tdnum = (self._num*fra2._den)
        tdden = (self._den*fra2._num)
        tdmdc = mdc(tdnum,tdden)
        return Fração(tdnum//tdmdc,tdden//tdmdc) 

    #redefine a potenciação a um inteiro                
    def __pow__(self,pot):
        pwnum = pow(self._num,pot)
        pwden = pow(self._den,pot)
        pwmdc = mdc(pwnum,pwden)
        return Fração(pwnum//pwmdc,pwden//pwmdc) 
    #redefine a comparação equivalente a ==
    def __eq__(self,fra2):   
        return self._num*fra2._den == self._den*fra2._num
    
    #redefine a comparação menor que: <  
    def __lt__(self,fra2):
        
        if self._den<0 or fra2._den<0:
            exp = self._num*fra2._den > self._den*fra2._num
        else: 
            exp = self._num*fra2._den < self._den*fra2._num
        return exp
    
    #redefine a comparação menor ou igual que: <=
    def __le__(self,fra2): 
        
        if self._den<0 or fra2._den<0:
            exp = self._num*fra2._den >= self._den*fra2._num
        else: 
            exp = self._num*fra2._den <= self._den*fra2._num
        return exp    
    
    #redefine a comparação maior que: >
    def __gt__(self,fra2):
        if self._den<0 or fra2._den<0:
            exp = self._num*fra2._den < self._den*fra2._num
        else: 
            exp = self._num*fra2._den > self._den*fra2._num
        return exp
    
    #redefine a comparação maior que: >=
    def __ge__(self,fra2):   
        if self._den<0 or fra2._den<0:
            exp = self._num*fra2._den <= self._den*fra2._num
        else: 
            exp = self._num*fra2._den >= self._den*fra2._num
        return exp
    
    #redefine a comparação diferente de  !=
    def __ne__(self,fra2):   
        return self._num*fra2._den != self._den*fra2._num
    
    #redefine o print    
    def __str__(self):
        
        if self._num==self._den:
            exp=str(1)
        elif self._den==1:
            exp=str(self._num)
        elif self._num!=0:
            exp=str(self._num) +"/"+str(self._den)
        else:
            exp=str(0)
        return exp  
#------------------------------------------------------------------------------

#Define a classe pilha lista
class Pilha:
    
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

#Função que define a precedência de operadores
def prioridade(x):
    if x == '+': return 1
    elif x == '-': return 1
    elif x == '*': return 2
    elif x == '/': return 2
    elif x == '**': return 3
    elif x == '(': return 4 
    elif x == ')': return 5 
    else: return 0     

#Função que traduz uma expressão de notação in-fixa para pós-fixa
def TraduzPosFixa(exp):
    
    #desmembra a expressão em caracteres individuais usando regex
    import re
    r = re.findall(r"(\b\w*[\.]?\w+\b|[\(\)\+\*\-\/])", exp)
    
    #instancia as pilhas usadas no processo e uma lista contendo os operadores    
    psfx = Pilha()
    pilha = Pilha()
    op = ['+','-','*','**','/','^']  

   #inicializa contador do while
    i=0
    
    #verifica se a expressão é não vazia
    if len(r)>0:
        #percorre a expressão traduzindo para pós fixa
        while i<len(r):
            
            #próximo elemento da expressão
            p=r[i]
            
            #1 - se p for numérico empilha na pós fixa
            if p.isnumeric():
                psfx.push(p)
            
            #2 - se p for abre parênteses empilha na pilha
            if p =="(":
                pilha.push(p)
                
            #3 - se p for operador
            if p in op:
                
                #3.1 - se p for potência
                prox = r[i+1]
                if p+prox == "**":
                    
                    for el in range(len(pilha)):
                        if pilha.top() in op:
                            if prioridade(pilha.top())>=prioridade(p+prox):
                                psfx.push(pilha.top())
                                pilha.pop()
                                
                    pilha.push(p+prox)
                    i+=1
                    
                #3.2 se p não for potência
                else: 
                    for el in range(len(pilha)):
                        if pilha.top() in op:
                            if prioridade(pilha.top())>=prioridade(p):
                                psfx.push(pilha.top())
                                pilha.pop()
                                
                    pilha.push(p)
                    
            #3.3 - se p for fecha parênteses
            if p == ')' :   
                el = pilha.pop()
                
                while el != '(':
                    psfx.push(el)
                    el = pilha.pop()            
            
            #proximo elemento da expresão        
            i+=1     

        #chegou ao fim desempilha operadores
        j=0
        while(j<len(pilha)):
            
            psfx.push(pilha.top())
            pilha.pop()        
            
       #devolve a expressão
        return psfx._pilha
        
    #caso a expressão seja vazia retorna erro
    else:
        raise Exception("Expressão vazia")

#Função que calcula o valor de uma expressão em notação pós-fixa
def CalcPosFixa(listaexp):
    
    opers = Pilha()
    #função que executa a operação aritimética
    def calcula(el,op1,op2):
        
        if el=="+":
            return op1+op2
        elif el=="-":
            return op1-op2
        elif el=="*":
            return op1*op2
        elif el=="**":
            return op1**op2._num  
        elif el=="/":
            return op1/op2        
        
    if len(listaexp)>0:
        #percorre a expressão pós-fixa e fazendo as operações com os elementos dois a dois
        for el in listaexp:
            
            if el.isnumeric():
                opers.push(Fração(int(el),1))
            else:
                op2 = opers.pop()
                op1 = opers.pop()
                result = calcula(el,op1,op2)
                opers.push(result)
        #retorna o valor calculado em forma de fração
        return opers.pop()
    #caso a expressão seja vazia retorna erro
    else:
        raise Exception("Expressão vazia")
#------------------------------------------------------------------------------
#Inicializar a variável de controle
comando = 0    
    
#Executa o programa enquanto a variável de controle não for igual a fim
while(comando!="fim"):
    
    #Recebe a expressão a ser calculada
    comando = input("Insira a expressão para ser traduzida e calculada ou digite fim para encerrar:\n")
    
    if comando != "fim":
        exp_psfx = TraduzPosFixa(comando)
        print(CalcPosFixa(exp_psfx)) 
