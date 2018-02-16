import copy
T=int(input())
for i in range(T):
    N=input()
    L=list(N)
    res=""
    if '6' in L:
        L.remove('6')
        for j in range(5,10):
            if(str(j) in L):
                temp='6'+str(j)
                res+=chr(int(temp))
        L.append('6')
    if '7' in L:
        L.remove('7')
        for j in range(0,10):
            if(str(j) in L):
                temp='7'+str(j)
                res+=chr(int(temp))
        L.append('7')
    if '8' in L:
        L.remove('8')
        for j in range(0,10):
            if(str(j) in L):
                temp='8'+str(j)
                res+=chr(int(temp))
        L.append('8')
    if '9' in L and '0' in L:
        res+="Z"
    print(res)
