def func(a,n,k):
	if k>=2:
		b=a*2
	else:
		b=a
	s=0
	maxi=-10**20-1
	for i in b:
		s+=i
		if maxi<s:
			maxi=s
		if s<0:
			s=0
	if sum(a)>=0 and k>=2:
		maxi+=(k-2)*sum(a)
	return maxi

def main():
	T=int(input())
	for i in range(T):
		nk=input().split()
		n=int(nk[0])
		k=int(nk[1])
		inp=input().split()
		a=[int(x) for x in inp]
		print(func(a,n,k))
main()