def pos(K,N,res):
    if K==0:
        return res
    if K%2==0:
        return pos(K//2,N//2,res)
    else:
        return pos(K//2,N//2,res+N//2)
Q=int(input())
for i in range(0,Q):
    inp=(input())
    inp=inp.split()
    N=int(inp[0])
    K=int(inp[1])
    print(pos(K,pow(2,N),0))

