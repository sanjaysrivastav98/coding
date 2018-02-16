def func(n,l,b,h):
	x=[0,l]
	y=[0,b]
	z=[0,h]
	for i in range(n):
		[xi,yi,zi]=[int(p) for p in input().split()]
		x.append(xi)
		y.append(yi)
		z.append(zi)
	# x=list(set(x.sort()))
	# y=list(set(y.sort()))
	# z=list(set(z.sort()))
	x.sort()
	y.sort()
	z.sort()
	xdif=0
	ydif=0
	zdif=0
	for i in range(n+1):
		temp=x[i+1]-x[i]
		if temp>xdif:
			xdif=temp
		temp=y[i+1]-y[i]
		if temp>ydif:
			ydif=temp
		temp=z[i+1]-z[i]
		if temp>zdif:
			zdif=temp
	print((xdif*ydif*zdif)%1000000007)

def main():
	T=int(input())
	for i in range(T):
		nlbh=input().split()
		n=int(nlbh[0])
		l=int(nlbh[1])
		b=int(nlbh[2])
		h=int(nlbh[3])
		func(n,l,b,h)
main()