from collections import Counter

with open("input.txt") as f:
     input = [line.split() for line in f]

valid = 0

for line in input:
    line_sorted = [''.join(sorted(w)) for w in line] # sort letters in each word
    c = Counter(line_sorted);
    occurances = list(c.values())
    occurances.sort()
    if occurances[-1] == 1:
        valid +=1

print(valid)
