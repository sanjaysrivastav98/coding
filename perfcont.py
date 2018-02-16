def func():
	np=input()
	np=np.split()
	n,p=int(np[0]),int(np[1])
	m=input()
	prob=[int(x) for x in m.split()]
	countleast=0
	countmax=0
	for i in range(n):
		if prob[i]>=p//2:
			countleast+=1
		elif prob[i]<=p//10:
			countmax+=1
		if countmax>2 or countleast>1:
			return "no"
	if countleast==1 and countmax==2:
		return "yes"
	return "no"



def main():
	T=int(input())
	for i in range(T):
		print(func())
main()