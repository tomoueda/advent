line = """AAAA
BBCD
BBCC
EEEC"""

line2 = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""

from tools import get_grid, fourd
from collections import defaultdict
from aoc import get_input 

line = get_input(12)



grid, x, y = get_grid(line)


def get_regions(grid):
    seen = set()
    regions = []
    for i in range(x):
        for j in range(y):
            if (j, i) not in seen:
                region_key = grid[(j, i)]
                region_nodes = [(j, i)]
                seen.add((j, i))
                t = [(j, i)]
                while t:
                    n = t.pop()
                    for d in fourd:
                        if n + d not in seen:
                            if grid[n + d] == region_key:
                                seen.add(n + d)
                                region_nodes.append(n + d)
                                t.append(n + d)
                regions.append((region_key, region_nodes))
    return regions

                

regions = get_regions(grid)

nodes = defaultdict(list)
for key, val in grid.items():
    nodes[val].append(key)


# part 1 
s = 0
for key, val in regions:
    a = 0
    p = 0
    for node in val:
        a += 1
        for d in fourd:
            e = grid[node + d]
            if e is None or e != key:
                n = node + d
                p += 1
    s += a * p
print(s)

def not_seq(l):
    s = 0
    l.sort()
    prev = None
    for i in l:
        if prev is None:
            prev = i
            continue
        if i - prev != 1:
            s += 1
        prev = i
    return s


def find_edges(key, val):
    c = 0
    for d in fourd:
        # is it x or y?
        idx = 1 if d[0] == 0 else 0
        odx = 1 - idx
        seen = defaultdict(list)
        for v in val:
            n = v + d
            if grid[n] !=  key:
                seen[n[idx]].append(n[odx])
        c += len(seen)
        for v in seen.values():
            c += not_seq(v)
    return c


s = 0
for key, val in regions:
    a = len(val)
    e = find_edges(key, val)
    s += a * e
print(s)


