def initialize(alphabet):

    for i in range(0,26):
        alphabet[i]=0
    return alphabet

T=int(input())
alphabet={}
for i in range(0,T):
    alphabet=initialize(alphabet)
    res=0
    cost=input()
    cost=[int(x) for x in cost.split()]
    string=input()
    for j in range(0,len(string)):
        alphabet[ord(string[j])-ord('a')]+=1
    for i in range(0,26):
        if alphabet[i]==0:
            res+=cost[i]
    print(res)