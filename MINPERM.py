def printList(L):
    for i in L:
        print(i,end=" ")
T=int(input())
L=[]
for i in range(T):
    L=[]
    N=int(input())
    if (N%2==0):

        for j in range(N):
            if j%2==0:
                L.append(j+2)
            else:
                L.append(j)
    else:
        for j in range(N-3):
            if j%2==0:
                L.append(j+2)
            else:
                L.append(j)
        L.extend([N-1,N,N-2])
    printList(L)
    print()

