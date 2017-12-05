with open("input.txt") as f:
    content = f.readlines()

nums = list(map(int, [line.strip() for line in content]))

curr = 0
count = 0

while curr >= 0 and curr < len(nums):
    tcurr = curr
    curr += nums[curr]
    nums[tcurr] += 1
    count += 1

print(count)

