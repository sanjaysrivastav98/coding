def isPalindrome(a):
    if(len(a)==1):
            return 1
    elif len(a)==2:
            return a[0]==a[1]
    if a[0]==a[-1]:
            return isPalindrome(a[1:-1])

T=int(input())
N=[]
M=[]
res=[]
flag=0
for i in range(0,T):
    flag=0
    temp=int(input())
    N.append(temp)
    M.append([])
    temp=input()
    M[i].append(temp)
    M[i]=M[i][-1].split()

    if(len(M[i])==N[i] and isPalindrome(M[i]) and M[i][int((N[i])/2)]=='7' and M[i][int((N[i]-1)/2)]=='7' and M[i][0]=='1'):
        for j in range(1,int((N[i])/2)):
            if(int(M[i][j])-int(M[i][j-1])==0 or int(M[i][j])-int(M[i][j-1])==1):
                flag=1
            else:
                flag=0
                break
    if flag==1:
        print("yes")
    else:
        print("no")
	
