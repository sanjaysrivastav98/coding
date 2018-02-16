# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 22:04:26 2016

@author: Sanjay
"""


def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
   
    inc=1
    dec=1
    count=1
    N=L[:]
    M=[]
    k=0
    l=0
    N1=L[:]
    M1=[]
    k1=0
    l1=0
    count1=1
   
        
    for i in range(k,len(L)-1):
        if L[i]<=L[i+1]:
            count+=1
            l=i+1
            if l==len(L)-1 and count>inc:
                inc = count
                M=[]
                for t in range(len(L)-count,len(L)):
                    M+=[N[t]]
            elif l==len(L)-1:
                break
                
        else:
            k+=count
            
            i=k
            if count>inc :
                inc=count
                M=[]
                for t in range(l-count+1,l+1):
                    M+=[N[t]]
        
            count=1
        if inc==1:
            M=[N[0]]
    for i in range(k1,len(L)-1):
        
                
        if L[i]>=L[i+1]:
            count1+=1
            l1=i+1
            if l1==len(L)-1 and count1>dec:
                dec=count1
                M1=[]
                for t in range(len(L)-count1,len(L)):
                    M1+=[N1[t]]
            elif l1==len(L)-1:
                break
        else:
            k1+=count
            i=k
            if count1>dec :
                dec =count1
                M1=[]
                for t in range(l1-count1+1,l1+1):
                    M1+=[N1[t]]
            count1=1
        if dec==1:
            M1=[N[0]]
    sum=0
    if inc>dec  :
        for i in range(inc):
            sum+=M[i]
    elif inc==dec:
        if L.index(M[0])<L.index(M1[0]):
            for i in range(inc):
                sum+=M[i]
        else:
            for i in range(inc):
                sum+=M1[i]
        
    else:
        for i in range(dec):
            sum+=M1[i]
    return sum
    
L=[5,4,10]
print(longest_run(L))        
                    

        
        
            
        