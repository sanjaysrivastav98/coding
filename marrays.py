def mod(a,b):
	if a>b:
		return a-b
	else:
		return b-a
def func(M,A,N):
	mini=[]
	maxi=[]
	for j in range(N):
		mini.append(min(A[j]))
		maxi.append(max(A[j]))
	s=0
	if mod(maxi[N-1],mini[N-2])>=mod(maxi[N-2],mini[N-1]):
		for j in range(1,N):
			s+=j*mod(maxi[j],mini[j-1])
	else:
		for j in range(1,N):
			s+=j*mod(maxi[j-1],mini[j])
	return s
		

	if mod(mini[0],maxi[1])>mod(mini[1],maxi[0]):
		return mod(mini[0],maxi[1])
	else:
		return mod(mini[1],maxi[0])
	s=0
	for j in range(1,N):
		s+=(mod(A[j-1][M[j-1]-1],A[j][0])*(j))
	print(s)



def main():
	T=int(input())
	for i in range(T):
		N=int(input())
		A=[]
		M=[]
		for j in range(N):
			s=input().split()
			M.append(int(s[0]))
			A.append([int(s[k]) for k in range(1,M[j]+1)])
		print(func(M,A,N))

main()