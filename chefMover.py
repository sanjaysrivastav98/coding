def isEqual(a):
    for i in range(0,len(a)):
        if a[i]!=a[0]:
            return 0
    return 1

def average(a):
    temp=0
    for i in range(0,len(a)):
        temp+=a[i]
    return int(temp/len(a))


T=int(input())
N=[]
D=[]
M=[]
res=[]
L=[]

for i in range(0,(T)):
    count=0
    temp=input()
    temp=temp.split()
    N.append(int(temp[0]))
    D.append(int(temp[1]))
    M.append([])
    temp = input()
    M[i].append(temp)
    M[i] = [int(x) for x in M[i][0].split()]
    L=[]
    for j in range(0,D[i]):
        L.append([])
    for j in range(0,N[i]):
        L[j%D[i]].append(M[i][j])
    av=average(L[0])
    for k in range(0, D[i]):
        flag = 0
        if(average(L[k])!=av):
            print (-1)
            flag=1
            break
        flag=0
        for j in range(0, len(L[k]) - 1):
            if(L[k][j] > av):
                L[k][j+1]+=(L[k][j]-av)
                count+=(L[k][j]-av)
                L[k][j]=av
            elif(L[k][j]<av):
                L[k][j+1]-=(av-L[k][j])
                count+=(av-L[k][j])
                L[k][j]=av
        if (L[k][len(L[k])-1]!=av):
            print (-1)
            flag=1
            break
    if(flag==1):
        continue
    print(count)




