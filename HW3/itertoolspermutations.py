import sys
import itertools
from itertools import permutations

instr = input().strip().split(' ')
seq = instr[0]
num = int(instr[1])

listPattern = []
for i in range(len(seq)):
    listPattern.append(seq[i])
#print(listPattern)

perms = list(permutations(listPattern,num))
answers = []
#print(perms)

for i in perms:
    str = ''
    for j in i:
        str += j
    answers.append(str)

answers.sort()

print('\n'.join(x for x in answers))

