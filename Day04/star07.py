from collections import Counter

with open("input.txt") as f:
     input = [line.split() for line in f]

valid = 0

for line in input:
    c = Counter(line);
    occurances = list(c.values())
    occurances.sort()
    if occurances[-1] == 1:
        valid +=1

print(valid)