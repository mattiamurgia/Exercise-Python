#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 09:11:13 2022

@author: MattiaMurgia
"""
from random import randint

#Parte 1
def esercizio1(L,m,soglia):
    M=[]
    for x in L:
        if x * m <= soglia:
            M.append(x);
    return M
    
print(esercizio1([1,5,7],2,10))




def esercizio2(s1, s2):
   s3=[]
   if len(s1) > len(s2):
       lunghezza= len(s2)
   else:
       lunghezza=len(s1)
   for i in range(lunghezza):
       s3.append((s1[i]+ s2[i]))
   return "".join(s3)

print(esercizio2("ciao","casa"))
print(esercizio2("buon","natale"))
    

def esercizio3(n,k):
    D={}
    for i in range(n):
        D[i]= k+ randint(1,6)
    return D

print(esercizio3(4,6))




#Parte 2
import pandas as pd

DF=pd.read_csv("bici.csv",sep=";")
DF.info()

#Pie Chart
Pie=DF.groupby(["weather"]).count().copy()
Pie["id"].plot.pie()

#Istogramma
DF["windspeed"].hist()

#BoxPlot
BoxPlot=pd.DataFrame(DF["windspeed"]).boxplot()

#Terzo Quartile
Q3 = DF["count"].quantile([0.75])





        
        
        
        
        
        
        
        
        
        
        
        
        