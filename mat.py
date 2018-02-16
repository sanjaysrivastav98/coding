def maxVal(R,C,Sx,Sy,x,y,board):
    x1=x
    y1=y
    res=board[Sx][Sy]
    while(len(x1)>0):
        max1=[0,Sx,Sy]
        temp=max1
        for i in range(0,len(x1)):
            list=[]
            dx=x1[i]
            dy=y1[i]
            if Sx-dx >=0:
                if Sy-dy>=0:
                    list.append([board[Sx-dx][Sy-dy],Sx-dx,Sy-dy,i])
                if Sy+dy<=C-1:
                    list.append([board[Sx-dx][Sy+dy],Sx-dx,Sy+dy,i])
            if Sx+dx<=R-1:
                if Sy-dy>=0:
                    list.append([board[Sx+dx][Sy-dy],Sx+dx,Sy-dy,i])
                if Sy+dy<=C-1:
                    list.append([board[Sx+dx][Sy+dy],Sx+dx,Sy+dy,i])
            if len(list)>0:
                temp= max(list,key=lambda z:z[0])
            if temp[0]>max1[0]:
                max1=temp
        if max1[0]==0:
            return res
        res+=max1[0]
        x1.pop(max1[3])
        y1.pop(max1[3])
        Sx=max1[1]
        Sy=max1[2]

    return res


T=int(input())
for i in range(0,T):
    next=input()
    next=next.split()
    R=int(next[0])
    C=int(next[1])
    N=int(next[2])
    nex=input()
    nex=nex.split()
    Sx=int(nex[0])
    Sy=int(nex[1])
    nL1=input()
    nL1=nL1.split()
    x=[int(j) for j in nL1]
    nL2 = input()
    nL2 = nL2.split()
    y = [int(j) for j in nL2]
    board=[]
    for j in range(0,R):
        board.append([])
        inp=input()
        inp=inp.split()
        board[j]=[int(k) for k in inp]
    res=board[Sx][Sy]
    print(maxVal(R,C,Sx,Sy,x,y,board))




