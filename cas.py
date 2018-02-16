T=int(input())
for i in range(T):
    N=int(input())
    arr=input().split()
    arr=[int(x) for x in arr]
    minInd=1
    sum1=sum(arr)
    min=2*sum1
    for j in range(0,N):
        if(min>sum1+arr[j]):
            min=sum1+arr[j]
            minInd=j+1
    print(minInd)