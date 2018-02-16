import copy
def func():
	n=int(input())
	s=input()
	a=[int(x) for x in s.split()]
	adj={1:[],2:[],3:[],4:[],5:[],6:[]}
	for i in range(n-1):
		if i==0:
			if a[i+1]==a[i]:
				print('-1')
				return
			adj[a[i]].append(a[i+1])
			adj[a[i+1]].append(a[i])
		else:
			if a[i-1]==a[i]:
				print('-1')
				return
			if a[i+1]==a[i]:
				print('-1')
				return
			if a[i-1] not in adj[a[i]]:
				if len(adj[a[i]])>=4:
					print('-1')
					return
				adj[a[i]].append(a[i-1])
			if a[i] not in adj[a[i-1]]:
				if len(adj[a[i-1]])>=4:
					print('-1')
					return
				adj[a[i-1]].append(a[i])
			if a[i+1] not in adj[a[i]]:
				if len(adj[a[i]])>=4:
					print('-1')
					return
				adj[a[i]].append(a[i+1])
			if a[i] not in adj[a[i+1]]:
				if len(adj[a[i+1]])>=4:
					print('-1')
					return
				adj[a[i+1]].append(a[i])
	o2={1:[2,3,4,5,6],2:[1,3,4,5,6],3:[1,2,4,5,6],4:[1,2,3,5,6],5:[1,2,3,4,6],6:[1,2,3,4,5]}
	for i in o2:
		for j in adj[i]:
			o2[i].remove(j)
	k=1
	for i in o2:
		if len(o2[i])<len(o2[k]):
			k=i
	o=copy.deepcopy(o2)
	# print(o)
	for i in o[k]:
		o1=[-1,-1,-1,-1,-1,-1]
		o1[k-1]=i
		o1[i-1]=k
		o[i].remove(k)
		o[k].remove(i)
		o3=copy.deepcopy(o)
		for j in o3:
			if j!=k and j!=i:
				for j1 in o3[j]:
					if j1!=k and j1!=i:
						o1[j1-1]=j
						o1[j-1]=j1
						o3[j1].remove(j)
						o3[j].remove(j1)
						o4=copy.deepcopy(o3)
						for l in o4:
							if l!=k and l!=i and l!=j and l!=j1:
								for l1 in o4[l]:
									if l1!=k and l1!=i and l1!=j and l1!=j1:
										o1[l1-1]=l
										o1[l-1]=l1
										o4[l1].remove(l)
										o4[l].remove(l1)
							if -1 not in o1:
								break
					if -1 not in o1:
						break
			if -1 not in o1:
				break
	# print(o1)
	if o1.count(-1)==2:
		for i in range(len(o1)):
			if o1[i]==-1:
				for j in range(i+1,len(o1)):
					if o1[j]==-1:
						if i not in adj[j]:
							o1[i]=j+1
							o1[j]=i+1
							break
				break
	# print(o1)
	if -1 in o1:
		print('-1')
		return
	for i in o1:
		print(i,end=" ")
	print()
	return


			



def main():
	t=int(input())
	for i in range(t):
		func()
main()