def func(a,b,c,d):
	if a==b and c==d or a==c and b==d or a==d and b==c:
		print("YES")
	else:
		print("NO")

def main():
	T=int(input())
	for i in range(T):
		abcd=input().split()
		a=int(abcd[0])
		b=int(abcd[1])
		c=int(abcd[2])
		d=int(abcd[3])
		func(a,b,c,d)
main()



