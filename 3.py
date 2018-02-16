# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 21:49:30 2016

@author: Sanjay
"""

trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}
def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    s=us_num
    if len(s)==1 or s=='10':
        return trans[s]
    
    elif s[0]=='1':
        return trans['10']+" " +trans[s[1]]
    elif s[1]=='0':
        return trans[s[0]]+" "+trans['10']
    else:
        return trans[s[0]]+" "+trans['10']+" "+trans[s[1]]

    