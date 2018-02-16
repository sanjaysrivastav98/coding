def remdup(l):
	l2=[l[0]]
	for i in l:
		if l2[-1]!=i:
			l2.append(i)
	return l2

def intersection(s1,s2):
	s=[]
	for i in s1:
		if i in s2:
			s+=[i]
	return s

def maxorder(s2,s):
	if len(s2)==1 and s2[0] not in s:
		return 0
	if len(s)==1 and s[0] in s2:
		return 1
	elif len(s)==1:
		return 0
	if s[0] in s2:
		if s2.index(s[0])!=len(s2)-1:
			return max(max(1+maxorder(s2[s2.index(s[0])+1:],s[1:]),maxorder(s2[s2.index(s[0])+1:],s)),maxorder(s2,s[1:]))
		else:
			return max(1,maxorder(s2,s[1:]))
	else:
		return maxorder(s2,s[1:])



def func(s1,s2):
	s1=remdup(s1)
	s2=remdup(s2)
	s=intersection(s1,s2)
	# print(s1,s2,s)
	i=maxorder(s2,s)
	# print(s1,s2,s,i)
	# i=len(s)

	return len(s1)+len(s2)-i



def main():
	T=int(input())
	for i in range(T):
		nm=input().split()
		n=int(nm[0])
		m=int(nm[1])
		s1=input()
		s2=input()
		s1=list(s1)
		s2=list(s2)
		print(func(s1,s2))
main()
