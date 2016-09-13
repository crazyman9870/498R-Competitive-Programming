import sys

lines = int(input().strip())

dictionary = {}
order = []
for i in range(lines):
    word = input().strip()
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1
        order.append(word)

print(len(dictionary))
print(' '.join(str(dictionary[x]) for x in order))