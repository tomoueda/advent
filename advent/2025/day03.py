lines="""987654321111111
811111111111119
234234234234278
818181911112111"""
from aoc import get_input
lines = get_input(3)

s = 0
for line in lines.split('\n'):

    m = 0
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            m = max(m, int(line[i]) * 10 + int(line[j]))
    s += m
print(s)

print('part 2')

from itertools import combinations

def pick_largest(num):
    last_leftmost = -1 
    n = len(num)
    indices = []
    for i in range(12):
        m = 0
        idx = n - 12 + i
        curr_leftmost = idx
        while idx > last_leftmost:
            if int(line[idx]) >= m:
                curr_leftmost = idx
                m = int(line[idx])
            idx -= 1
        last_leftmost = curr_leftmost
        indices.append(curr_leftmost)
    exp = 11
    s = 0
    for i in indices:
        s += int(num[i]) * 10 ** exp
        exp -= 1
    return s

s = 0
for line in lines.split('\n'):
    s += pick_largest(line)
print(s)


