lines = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

from aoc import get_input
lines = get_input(2)


c = 0
inp = lines.split('\n')


def safe(inc, diff):
    if diff == 0:
        return False
    if abs(diff) > 3:
        return False
    if inc and diff < 0:
        return False
    if not inc and diff > 0:
        return False
    return True

def safe2(nums):
    prev = nums[0]
    inc = nums[1] > nums[0]
    for num in nums[1:]:
        diff = num - prev
        if not safe(inc, diff):
            return False
        prev = num
    return True

def safe3(nums):
    if safe2(nums):
        return True
    for i in range(len(nums)):
        copy = list(nums)
        del copy[i]
        if safe2(copy):
            return True
    return False


for line in inp:
    if not line:
        continue
    nums = list(map(int, line.split()))
    # part 1
    # if safe2(nums):

    # part 2
    if safe3(nums):
        c += 1

print(c)



