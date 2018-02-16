def main():
	T=int(input())
	for i in range(T):
		nk=input().split()
		n=int(nk[0])
		k=int(nk[1])
		m=input().split()
		m=[int(x) for x in m]
		m.sort()
		print(m[(n+k)//2])
main()