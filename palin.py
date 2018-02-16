def countLetters(word):
    letterdict={}
    for letter in word:
        letterdict[letter] = 0
    for letter in word:
        letterdict[letter] += 1
    return letterdict

T=int(input())
for i in range(0,T):
    flag=0
    s=input()
    t=input()
    freqA=countLetters(s)
    freqB=countLetters(t)
    for j in freqA.keys():
        if freqA[j]>=2:
            if j not in freqB.keys():
                print("A")
                flag=1
            if flag==1:
                break
    if (flag==0):
        print("B")



