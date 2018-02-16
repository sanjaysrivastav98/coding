def func(N):
	num=2**32-1
	num=num//N
	a=[num for i in range(N-1)]
	a[0]-=2
	a.append(1)
	z=2**32-2-sum(a)
	if z<N:
		kl=1
	else:
		kl=2
	# print(z)
	# for i in range(z//kl):
	# 	a[i]+=kl
	a[0]+=z
	# print("wrongsol's ans = ",wrongsol(a))
	for i in a:
		print(i,end=" ")
	print(" ")
	# print('hello',sum(a)-2**32+1)

	return	
	# for i in range(N):
	# 	a.append(num)
	# z=2**32+10-sum(a)
	# a[0]-=z//2
	# a[N-1]-=z//2
	# print(z)
	# for i in range(1,N):
	# 	a[i]+=1
	# print("wrongsol's ans = ",wrongsol(a))
	# for i in a:
	# 	print(i,end=" ")
	# print(" ")
	# print('hello',sum(a)-2**32+1)


# int wrongSolver(std::vector <unsigned int> a) {
# 	int n = a.size();
# 	std::vector<unsigned int> prefSum(n), sufSum(n);
# 	prefSum[0] = a[0];
# 	for (int i = 1; i < n; i++) {
# 		prefSum[i] = prefSum[i - 1] + a[i];
# 	}
# 	sufSum[n - 1] = a[n - 1];
# 	for (int i = n - 2; i >= 0; i--) {
# 		sufSum[i] = sufSum[i + 1] + a[i];
# 	}
# 	unsigned int mn = prefSum[0] + sufSum[0];
# 	int where = 1;
# 	for (int i = 1; i < n; i++) {
# 		unsigned int val = prefSum[i] + sufSum[i];
# 		if (val < mn) {
# 			mn = val;
# 			where = i + 1;
# 		}
# 	}
# 	return where;
# }
def mysum(a,b):
	# if(a+b>2**32):
	# 	print('hello',a,b,(a+b)%(2**32))
	return (a+b)%(2**32)
def wrongsol(a):
	n=len(a)
	# print(n)
	prefsum=[0 for x in range(n)]
	sufsum=[0 for x in range(n)]
	prefsum[0]=a[0]
	for i in range(1,n):
		# print('1')
		prefsum[i]=mysum(prefsum[i-1],a[i])
	sufsum[n-1]=a[n-1]
	for i in range(n-2,-1,-1):
		# print('2')
		sufsum[i]=mysum(sufsum[i+1],a[i])
	mn=mysum(sufsum[0],prefsum[0])
	where=1
	for i in range(1,n):
		val=mysum(prefsum[i],sufsum[i])
		if val <mn:
			print(mn,i,val)	
			mn=val
			where=i+1
	# print(where)
	return where



def main():
	T=int(input())
	for i in range(T):
		N=int(input())
		func(N)
main()