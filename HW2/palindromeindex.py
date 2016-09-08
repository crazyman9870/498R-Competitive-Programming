#https://www.hackerrank.com/challenges/palindrome-index

import sys

def isPalindrome(str):
    for a in range(int(len(str) / 2)):
        if str[a] != str[len(str) - (a + 1)]:
            return False;
    return True;

numCases = int(input().strip())

list = []
results = []
for i in range(numCases):
    list.append(input().strip().lower())

#print('\n'.join(list))
    
for pal in list:
    index = -1
    for j in range(int(len(pal) / 2)):
        if pal[j] != pal[len(pal) - (j + 1)]:
            pos1 = j
            pos2 = len(pal) - (j + 1)
            #test first index
            teststr = pal[:pos1] + pal[(pos1+1):]
            if isPalindrome(teststr) == True:
                index = j
                break
            #test second index
            teststr = pal[:pos2] + pal[(pos2+1):]
            if isPalindrome(teststr) == True:
                index = (len(pal) - (j + 1))
                break
    results.append(index)
print('\n'.join(str(x) for x in results))