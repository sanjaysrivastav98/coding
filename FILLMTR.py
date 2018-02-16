import copy

def isReflexive(B,N):
    for x1 in range(N):
        if B[x1][x1]==1:
            return (0,B)
        elif B[x1][x1]==-1:
            B[x1][x1]=0
    return (1,B)

def isEqual(B1,B2,N):
    for x1 in range(N):
        for y1 in range(N):
            if B1[x1][y1]!=B2[x1][y1]:
                return 0
    return 1

def isSymmetric(B,N):
    for x1 in range(N):
        for y1 in range(x1+1,N ):
            if (B[x1][y1] != B[y1][x1] and B[x1][y1] != -1 and B[y1][x1] != -1):
                return (0,B)
            elif B[x1][y1] == -1:
                B[x1][y1] = B[y1][x1]
            elif B[y1][x1] == -1:
                B[y1][x1] = B[x1][y1]
    return(1,B)
def isTransitive(B,N):
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if(B[i][j]==B[j][k]):
                    if (B[i][j]==1):
                        if(B[i][k]==1):
                            return (1,B)
                        elif B[i][k]==-1:
                            B[i][k]=0
                    elif B[i][j]==0:
                        if B[i][k]==1:
                            return (1,B)
                        else:
                            B[i][k]=0


    return (0,B)

T=int(input())
for x in range(T):
    inp=input().split()
    N=int(inp[0])
    Q=int(inp[1])
    B=[]
    flag=0
    for x1 in range(N):
        B.append([])
        for y1 in range(N):
            B[x1].append(-1)
    for y in range(Q):
        [i,j,val]=[int(k) for k in input().split()]
        B[i-1][j-1]=val

    temp=isReflexive(B,N)
    if temp[0] ==0:
        print("no")
        continue
    B=temp[1]
    prev=[]
    while(len(prev)==0 or isEqual(B,prev,N)==0):
        temp=isSymmetric(B,N)
        if(temp[0]==0):
            flag=1
            break
        B=temp[1]
        prev=copy.deepcopy(B)
        temp=isTransitive(B,N)
        if (temp[0] == 1):
            flag = 1
            break
        B=temp[1]
    if(flag==1):
        print("no")
    else:
        print("yes")





