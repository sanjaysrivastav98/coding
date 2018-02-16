def isPalindrome(a):
	if(len(a)==1):
		return 1
	elif len(a)==2:
		return a[0]==a[1]
	if a[0]==a[-1]:
		return isPalindrome(a[1:-1])

