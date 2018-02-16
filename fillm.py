
T=int(input())
for x in range(T):
    inp=input().split()
    N=int(inp[0])
    Q=int(inp[1])
    A=[]
    flag=0
    for i in range(N):
        A.append(-1)
    for y in range(Q):
        [i,j,val]=[int(k) for k in input().split()]
        if i==j and val!=0:
            flag=1

        if A[i-1]==-1 or A[j-1]==-1:
            if A[j-1]==-1 and A[i-1]==-1:
                if i>j:
                    A[j-1]=0
                    A[i-1]=val
                else:
                    A[i-1]=0
                    A[j-1]=val
            elif A[i-1]==-1:
                if val==0:
                    A[i-1]=A[j-1]
                else:
                    A[i-1]=1-A[j-1]
            else:
                if val==0:
                    A[j-1]=A[i-1]
                else:
                    A[j-1]=1-A[i-1]
        else:
            if A[i-1]-A[j-1] !=val and A[i-1]-A[j-1]!=-1*val:
                flag=1
    print(A)
    if flag==0:
        print("yes")
    else:
        print("no")

