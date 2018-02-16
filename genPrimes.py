# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 14:19:33 2016

@author: Sanjay
"""

def genPrimes():
    p=[2]
    yield 2
    n=2
    while True:
        n+=1
        flag=0
        for i in p:
            if n%i==0:
                flag=1
                break
        if flag==0:
            p+=[n]
            yield n