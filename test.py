def search(a,ele):
	print(a)
	n=len(a)
	if n==1:
		if ele>a[0]:
			return a[0]
		else:
			return -1
	elif n==2:
		if a[0]>ele:
			return -1
		elif a[0]==ele:
			return a[0]
		elif a[1]<=ele:
			return a[1]
		elif a[1] > ele and a[0]<=ele:
			return a[0]
	else:
		if a[n//2]>=ele:
			return search(a[:n//2+1],ele)
		else:
			return search(a[n//2:],ele)

print(search([1,2],0))