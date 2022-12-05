import sys
import os
import string

letters = list(string.ascii_lowercase)
uppercaseletters = list(string.ascii_uppercase)
for i in uppercaseletters:
    letters.append(i)

lines = open(sys.argv[1], "r").readlines()

total = 0
for l in lines:
    l = l.replace("\n","")
    length = int(len(l)/2)
    print(length)
    pocket1 = list(l[0:length])
    pocket2 = list(l[length:])
    common = list(set(pocket1).intersection(pocket2))[0]
    value = letters.index(common)+1
    total += value

print(total)

lines = [l.replace("\n","") for l in lines]

total = 0
for l in range(0, len(lines), 3):
    group = lines[l:l+3]
    common = list(set.intersection(*map(set,group)))[0]
    value = letters.index(common)+1
    total += value
print(total)
