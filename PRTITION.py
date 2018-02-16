def func2(x,N,arr,y,t):

	if y == 0:
		return arr
	if t>=N:
		if y==0:
			return arr
		return False
	if t+1!=x:
		s=func2(x,N,arr+[t+1],y-t-1,t+1)
		if s:
			return s
		else:
			return func2(x,N,arr,y,t+1)
	else:
		s=func2(x,N,arr+[t+2],y-t-2,t+2)
		if s:
			return s
		else:
			return func2(x,N,arr,y,t+2)


def func(x,N):
	y=N*(N+1)/2- x
	if y%2!=0 or x>N:
		print("impossible")
		return
	arr=[]
	a=func2(x,N,arr,y/2,0)
	if not a:
		print("impossible")
		return
	# print(sum(a),a,y)
	s=""
	for i in range(1,N+1):
		if i in a:
			s+="0"
		elif i==x:
			s+="2"
		else:
			s+="1"
	print(s)

def main():
	T=int(input())
	for i in range(T):
		xN=input().split()
		x=int(xN[0])
		N=int(xN[1])
		func(x,N)
main()