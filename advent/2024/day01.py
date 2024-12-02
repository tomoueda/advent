lines = """3   4
4   3
2   5
1   3
3   9
3   3"""

import requests
from collections import defaultdict
from aoc import get_input

lines = get_input(1) 


l = []
r = []
for line in lines.split('\n'):
    if not line:
        continue
    i = list(map(int, line.split()))
    l.append(i[0])
    r.append(i[1])
l.sort()
r.sort()

# part 1
s = 0
for i in range(len(l)):
    s += abs(l[i] - r[i])
print(s)


# part 2
s = 0
d = defaultdict(lambda: 0) 
for m in r:
    d[m] += 1

for n in l:
    if n in d:
        s += n * d[n]
print(s)
