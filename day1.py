import os
import sys

input = open(sys.argv[1]).readlines()

cals = []
temp = 0
for i in input:
    if i=="\n":
        cals.append(temp)
        temp = 0
    else:
        temp+=int(i.replace("\n",""))
cals.append(temp)

print(cals)
cals.sort()
top3 = sum(cals[-3:])
print(top3)
