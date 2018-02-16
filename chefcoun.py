def main():
	T=int(input())
	for i in range(T):
		N=int(input())
		# m=[10**5 for x in range(N)]
		# k=[]
		# l=k+m
		for j in range(N):
			print(int(((2**32)/N)+1),end=" ")
		print()
main()