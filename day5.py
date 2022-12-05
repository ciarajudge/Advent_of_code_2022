import os
import sys

lines = open(sys.argv[1], "r").readlines()

stacks = [["B", "S", "V", "Z", "G", "P", "W"],
["J", "V", "B", "C", "Z", "F"],
["V", "L", "M", "H", "N", "Z", "D", "C"],
["L", "D", "M", "Z", "P", "F", "J", "P"],
["V", "F", "C", "G", "J", "B", "Q", "H"],
["G", "F", "Q", "T", "S", "L", "B"],
["L", "G", "C", "Z", "V"],
["N", "L", "G"],
["J", "F", "H", "C"]]

for l in lines:
    num = int(l.split(" ")[1])
    origin = int(l.split(" ")[3])-1
    destination = int(l.split(" ")[5].replace("\n", ""))-1
    snippet = stacks[origin][-num:]
    stacks[origin] = stacks[origin][0:len(stacks[origin])-num]
    stacks[destination].extend(snippet)
    print(stacks)

print([l[-1] for l in stacks])
