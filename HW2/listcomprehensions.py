#https://www.hackerrank.com/challenges/list-comprehensions

import sys

x = int(input().strip())
y = int(input().strip())
z = int(input().strip())
n = int(input().strip())

listofpos = []

for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if (i+j+k) != n:
                pos = [i,j,k]
                listofpos.append(pos)
                
print(listofpos)