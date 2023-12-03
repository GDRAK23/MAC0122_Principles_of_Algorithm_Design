#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nome: Guilherme Augusto Martins 
NUSP: 7199162
Exercícios 1
"""

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
if __name__ == '__main__':
    x = Fração(10,20)    
    y = Fração(2,1)   
    print(x+y)
    print(x-y)
    print(x*y)
    print(x/y)
    print(x**2)
    print((x+y+(x-y))**2)
    print(x==y)
    print(x!=y)
    print(x<y)
    print(x<=y)
    print(x>y)
    print(x>=y)
    


