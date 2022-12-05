import os
import sys

runs = open(sys.argv[1], "r").readlines()

scoredict = {"A Y" : 8, "B X" :1, "C Z" : 6,
"A X" : 4, "A Z" : 3, "B Y" : 5, "B Z" : 9, "C X" : 7, "C Y" : 2}

total = 0
for l in runs:
    total += scoredict[l.replace("\n", "")]

print(total)

total = 0
outcomedict = {"X": 1, "Y": 2, "Z":0}
dict = {"A":[2,3,1], "B":[3,1,2], "C":[1,2,3]}
scores = [6,0,3]
for l in runs:
    outcome = l.replace("\n", "").split(" ")[1]
    played = l.replace("\n", "").split(" ")[0]
    ind = outcomedict[outcome]
    total += dict[played][ind] + scores[ind]

print(total)
