class node:
	prob_list=[]
	val_list={}
	value=0
	index=0
	name=''
	def __repr__(self):
		return self.name+","+ str(self.value)+","+str(self.index)

def func(n,m):
	ques=input().split()
	dic={}
	for i in range(n):
		uqs=input().split()
		user=uqs[0]
		code=uqs[1]
		score=int(uqs[2])
		if user not in dic:
			dic[user]=node()
			dic[user].name=user
			dic[user].value=score
			dic[user].prob_list.append(code)
			dic[user].val_list[code]=score
			dic[user].index=i
		else:
			if code not in dic[user].prob_list:
				if (score>0):
					dic[user].value += score
					dic[user].prob_list.append(code)
					dic[user].val_list[code] = score
					dic[user].index = i

			else:
				# if dic[user].val_list[code] < score:
				dic[user].value-=dic[user].val_list[code]
				dic[user].val_list[code]=score
				dic[user].value+=score
				dic[user].index=i
	# a=sorted(dic.values(),key= lambda x: x.value,reverse=True)

	b={}
	new=[]
	count=0
	for i in dic.values():
		if (i.value in b):
			b[i.value].append(i)
		else:
			new.append(i.value)
			b[i.value]=[i]
		count+=1


	a=sorted(new,reverse=True)
	print (count)
	for i in a:
		asd=sorted(b[i],key=lambda x:x.index)
		for j in asd:
			print (j.name,j.value)


	# z=[]
	# start=0
	# temp=a[0].value
	# for i in range(1,len(a)):
	# 	if (temp!=a[i].value):
	# 		z+=sorted(a[start:i],key=lambda x:x.index)
	# 		start=i
	# 	temp=a[i].value
	# z += sorted(a[start:i+1], key=lambda x: x.index)
	# print(len(z))
	# for i in z:
	# 	print(i.name,i.value)
def main():
	T=int(input())
	for i in range(T):
		nm=input().split()
		n=int(nm[0])
		m=int(nm[1])
		func(n,m)
main()