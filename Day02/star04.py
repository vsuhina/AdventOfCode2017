import itertools

with open("input.txt") as f:
    content = f.readlines()

sum = 0

for line in content:
    nums = list(map(int, line.strip().split('\t')))
    pair = [a / b for (a,b) in itertools.product(nums, nums) if a % b == 0 and a != b]
    sum += int(pair[0]) #we expect only one result (specified in task)

print(sum)
