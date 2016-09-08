#https://www.hackerrank.com/challenges/pangrams

import sys

pangram = input().strip().lower()
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

if len(pangram) < 1 or len(pangram) > 1000:
    print('not pangram')
else:
    result = True
    for i in range(len(alphabet)):
        if pangram.find(alphabet[i]) == -1:
            result = False
    if result == True:
        print('pangram')
    else:
        print('not pangram')