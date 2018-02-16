# import copy
# def func(s,x,y):
# 	dic={'a':0,'b':0}
# 	dic2={'a':0,'b':0}
# 	for i in s:
# 		if i=='a':
# 			dic['a']+=1
# 			dic2['a']+=1
# 		else:
# 			dic['b']+=1
# 			dic2['b']+=1
# 	res=""
# 	cnt=0
# 	flag=0
# 	while(dic['a']>0):
# 		temp=x
# 		while(temp>0 and dic['a']>0):
# 			res+='a'
# 			temp-=1
# 			dic['a']-=1
# 		flag=0
# 		if dic['b']>0:
# 			res+='b'
# 			dic['b']-=1
# 			flag=1
# 		elif dic['a']>0:
# 			res+='*'
# 			cnt+=1
# 			flag=0
# 	while(dic['b']>0):
# 		temp=y
# 		temp-=flag
# 		flag=0
# 		while(temp>0 and dic['b']>0):
# 			res+='b'
# 			temp-=1
# 			dic['b']-=1
# 		if dic['b']>0:
# 			res+="*"
# 			cnt+=1
# 	res2=copy.deepcopy(res)
# 	res=""
# 	cnt2=0
# 	flag=0
# 	while(dic2['b']>0):
# 		temp=y
# 		while(temp>0 and dic2['b']>0):
# 			res+='b'
# 			temp-=1
# 			dic2['b']-=1
# 		flag=0
# 		if dic2['a']>0:
# 			res+='a'
# 			dic2['a']-=1
# 			flag=1
# 		elif dic2['b']>0:
# 			res+='*'
# 			cnt2+=1
# 			flag=0
# 	while(dic2['a']>0):
# 		temp=x
# 		temp-=flag
# 		flag=0
# 		while(temp>0 and dic2['a']>0):
# 			res+='a'
# 			temp-=1
# 			dic2['a']-=1
# 		if dic2['a']>0:
# 			res+="*"
# 			cnt2+=1
# 	if cnt>=cnt2 and cnt2!=0:
# 		return res
# 	else:
# 		return res2






# def main():
# 	T=int(input())
# 	for i in range(T):
# 		s=input()
# 		nk=input().split()
# 		x=int(nk[0])
# 		y=int(nk[1])
# 		print(func(s,x,y))
# main()

def func(s,x,y):
	dic={'a':0,'b':0}
	dic2={'a':0,'b':0}
	for i in s:
		if i=='a':
			dic['a']+=1
			dic2['a']+=1
		else:
			dic['b']+=1
			dic2['b']+=1
	res=""
	flag=0
	cnt1=0
	while(dic['a']>0):
		temp=x
		while(temp>0 and dic['a']>0):
			res+='a'
			temp-=1
			dic['a']-=1
		flag=0
		if dic['b']>0:
			res+='b'
			flag=1
			dic['b']-=1
		elif dic['a']>0:
			res+='*'
			cnt1+=1
			flag=0
	while(dic['b']>0):
		temp=y
		temp-=flag
		while(temp>0 and dic['b']>0):
			res+='b'
			temp-=1
			flag=0
			dic['b']-=1
		if dic['b']>0:
			res+="*"
			cnt1+=1
			flag=0
	
	res2=""
	cnt2=0
	while(dic2['b']>0):
		temp=y
		flag=0
		while(temp>0 and dic2['b']>0):
			res2+='b'
			temp-=1
			dic2['b']-=1
		flag=0
		if dic2['a']>0:
			res2+='a'
			dic2['a']-=1
			flag=1
		elif dic2['b']>0:
			res2+='*'
			cnt2+=1
			flag=0
	while(dic2['a']>0):
		temp=x
		temp-=flag
		while(temp>0 and dic2['a']>0):
			res2+='a'
			temp-=1
			dic2['a']-=1
			flag=0
		if dic2['a']>0:
			res2+="*"
			flag=0
			cnt2+=1
	if cnt1<=cnt2:
		return res
	else:
		return res2
 
 
 
 
 
 
def main():
	T=int(input())
	for i in range(T):
		s=input()
		nk=input().split()
		x=int(nk[0])
		y=int(nk[1])
		print(func(s,x,y))
main() 