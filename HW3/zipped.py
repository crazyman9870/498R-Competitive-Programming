import sys

header = input().strip().split()
studentcount = int(header[0])
testcount = int(header[1])

testgrades = []
for i in range(testcount):
    testgrades.append(input().strip().split())
    
students = []
for grades in testgrades:
    students += [grades]
students = list(zip(*students))

avgs = []
for student in students:
    sum = 0.0
    for testgrade in student:
        sum += float(testgrade)
    avgs.append(sum/testcount) 

print('\n'.join(str(avg) for avg in avgs))