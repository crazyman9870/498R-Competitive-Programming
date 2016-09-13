import sys

num = int(input().strip())

fibonacci = []

for i in range(num):
    if i == 0:
        fibonacci.append(0)
    elif i == 1:
        fibonacci.append(1)
    else:
        fibonacci.append(fibonacci[i-2] + fibonacci[i-1])

cube = lambda a: a**3
answers = []
for x in fibonacci:
    answers.append(cube(x))
    
print(answers)