import os
import sys

lines = open(sys.argv[1], "r").readlines()

total = 0

for l in lines:
  l = l.replace("\n", "").split(",")
  elf1 = range(int(l[0].split("-")[0]),int(l[0].split("-")[1])+1)
  elf2 = range(int(l[1].split("-")[0]),int(l[1].split("-")[1])+1)
  if any(e in elf1 for e in elf2) or any(e in elf2 for e in elf1):
      total += 1
print(total)
