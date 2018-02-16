# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 18:28:57 2016

@author: Sanjay
"""

s=int((input)("Enter the number of numbers"))
it={}
for i in range(s):
    it[i]=int((input)(''))
    if it[i]<1 or it[i] > 1000000000:
        i-=1
        
for i in range(s):
    n=1
    noz=0
    while it[i]//(5**n)!=0:
        noz+=it[i]//(5**n)
        n+=1
    print (noz)
