# def func(A):
# 	cnt=0
# 	for i in range(len(A)):
# 		for j in range(i+1,len(A)):
# 			if A[i]==A[j] and i==j-1:
# 				cnt+=1
# 			elif A[i]==A[j]:
# 				temp=A[i+1]
# 				flag=0
# 				for k in range(i+1,j):
# 					if A[k]!=temp:
# 						flag=1
# 						break
# 				if flag==0:
# 					cnt+=1
# 	print(cnt)

def func(A):
	temp=A[0]
	cnt=1
	ans=0
	prev=""
	for i in range(1,len(A)):
		if temp==A[i]:
			cnt+=1
		else:
			if prev!="":
				if A[i]==prev:
					ans+=1
			prev=temp
			temp=A[i]
			ans+=int(cnt*(cnt-1)/2)
			cnt=1
		# print(A,temp,prev,cnt)
	# print(cnt)
	ans += int(cnt * (cnt - 1) / 2)
	print(ans)


def main():
	t=int(input())
	for i in range(t):
		A=input()
		func(A)

main()
