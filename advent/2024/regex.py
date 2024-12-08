lines = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

import re

r = re.compile(r'(\d+): ([\d\s]+)')

def combos(n):
    if n == 0:
        return []
    c = []
    nc = combos(n - 1)
    for s in ['*', '+']:
        for combo in nc:
            c.append([s] + combo)
    return c
        

for line in lines.splitlines():
    m = r.match(line)
    t = int(m.group(1))
    ns = list(map(int, m.group(2).split()))
    c = combos(len(ns))
    print(c)

