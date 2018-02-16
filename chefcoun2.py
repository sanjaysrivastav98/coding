import sys
def func(N):

		num=2**32//(N)
		a=[]
		# num2=(2**32-2*num)//(N-3)
		for j in range(N):
			a.append(num)
		z=(2**32-sum(a))//2

		for j in range(N):
			if j<z or j>=N-z:
				a[j]+=1

		a[0]+=5
		s=0
		for i in range(N-1):
			s+=a[i]
		print(s-2**32)
		a[N-1]+=5
		for i in a:
			print(i,end=" ")
		print()
		print(sum(a)-2**32)
			# print(sum(a[0:N]))
		return sum(a)-2**32
		
t=int(input())
# t=10
# N=99991
a = []
for i in range(t):
	N = int(input())

	a.append(func(N))
	N+=1
# print(a)