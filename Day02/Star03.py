with open("input.txt") as f:
    content = f.readlines()

sum = 0

for line in content:
    nums = list(map(int, line.strip().split('\t')))
    sum += max(nums) - min(nums)

print(sum)
