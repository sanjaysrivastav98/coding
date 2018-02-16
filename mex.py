def func():
	nk=input().split()
	n,k=int(nk[0]),int(nk[1])
	s=[int(x) for x in input().split()]
	s=list(set(s))
	s.sort()
	# print(s)
	k=k-s[0]
	if k<0:
		return s[0]+k
	for i in range(1,n):
		k=k-(s[i]-s[i-1]-1)
		if k<0:
			return s[i]+k
	if k<0:
		k=0
	return s[n-1]+k+1

def main():
	T=int(input())
	for i in range(T):
		print(func()

)main()