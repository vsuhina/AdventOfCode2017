with open("input.txt") as f:
    content = f.readlines()

nums = list(map(int, [line.strip() for line in content]))

curr = 0
count = 0
l = len(nums)

while curr >= 0 and curr < l:
    tcurr = curr
    offset = nums[curr]
    curr += offset
    if offset >= 3:
        nums[tcurr] += -1
    else:
        nums[tcurr] += 1
    
    count += 1

print(count)


