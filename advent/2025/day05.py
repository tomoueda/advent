lines = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

from aoc import get_input
lines = get_input(5)

ranges, ingredients = lines.split('\n\n')
freshes = []

for fresh in ranges.split('\n'):
    start, end = map(int, fresh.split('-'))
    freshes.append((start, end))
freshes.sort()

def in_fresh(n):
    for start, end in freshes:
        if n >= start and n <= end:
            return True
    return False

s = 0
for i in ingredients.split('\n'):
    if in_fresh(int(i)):
        s += 1
print(s)

print('part 2')

s = 0
curr_start = freshes[0][0]
curr_end = freshes[0][1]

for fresh in freshes[1:]:
    if curr_end < fresh[0]:
        s += curr_end - curr_start + 1
        curr_start = fresh[0]
    curr_end = max(curr_end, fresh[1])
s += curr_end - curr_start + 1
print(s)
