# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 21:52:04 2016

@author: Sanjay
"""
def primes(h):
    d=[2,3]
    for i in range(5,h+1,2):
        flag=0
        for j in d:
            if i%j==0:
                flag=1
        if flag ==0:
            d+=[i]
    return d
n=(input)('')
c={}
l={}
h={}
list={}
a={}
for i in range(int(n)):
    a[i]=(input)('')
    list[i]=a[i].split()
    l[i]=int(list[i][0])
    h[i]=int(list[i][1])
    sum=0    
    for j in range(l[i],h[i]+1):
        if j in primes(h[i]):
            sum+=j
    c[i]=sum
for i in range(int(n)):
    print(c[i])
