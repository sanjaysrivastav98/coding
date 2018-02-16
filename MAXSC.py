def search(a,ele):
	n=len(a)
	if n==1:
		if ele>a[0]:
			return a[0]
		else:
			return -1
	elif n==2:
		if a[0]>=ele:
			return -1
		elif a[1]<ele:
			return a[1]
		elif a[1] >= ele and a[0]<ele:
			return a[0]
	else:
		if a[n//2]>=ele:
			return search(a[:n//2+1],ele)
		else:
			return search(a[n//2:],ele)


def func():
	N=int(input())
	A=[]
	for i in range(N):
		temp=[int(x) for x in input().split()]
		A.append(sorted(temp))
	temp2=A[-1][-1]
	s=temp2
	for i in range(N-2,-1,-1):
		temp2=search(A[i],temp2)
		if temp2==-1:
			return -1
		s+=temp2

	return s
		

def main():
	T=int(input())
	for i in range(T):
		print(func())

main()