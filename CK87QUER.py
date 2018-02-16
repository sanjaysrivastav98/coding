def main():
	T=int(input())
	for i in range(T):
		Y=int(input())
		cnt=0
		temp=int((Y-1)**0.5)
		if Y>700:
			temp2=int((Y-700)**0.5)
		else:
			temp2=0
		cnt+=temp2*700
		cnt+=(temp-temp2)*Y
		cnt+=int((temp2)*(temp2+1)*(temp2*2+1)//6)
		cnt-=int((temp)*(temp+1)*(temp*2+1)//6)

		# j=temp
		# while(j>0):
		# 	if Y-j*j >700 or Y-j*j <0:
		# 		break
		# 	cnt+=(Y-j*j)
		# 	j-=1
		# cnt+=j*700
		print(cnt)
main()