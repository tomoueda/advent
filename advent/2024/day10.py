line = """0123
1234
8765
9876"""

line2 = """...0...
...1...
...2...
6543456
7.....7
8.....8
9.....9"""

line3 = """..90..9
...1.98
...2..7
6543456
765.987
876....
987...."""

line4 = """10..9..
2...8..
3...7..
4567654
...8..3
...9..2
.....01"""

line5 = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

from tools import *
from aoc import get_input

line = get_input(10)
grid, x, y = get_grid(line)



nodes = []
for key, val in grid.items():
    if val == '0':
        nodes.append(key)


# part 1
 #s = 0
 #def nth(start):
 #    nodes = [start]
 #    pos = set()
 #    while nodes:
 #        node = nodes.pop()
 #        for d in fourd:
 #            n = int(grid[node])
 #            mstr = grid[node + d]
 #            if mstr is None or mstr == '.':
 #                continue
 #            m = int(mstr)
 #            if m - n == 1:
 #                if m == 9:
 #                    pos.add(node + d)
 #                    continue
 #                nodes.append(node + d)
 #    return len(pos)
 #
 #for n in nodes:
 #    s += nth(n)
 #print(s)


s = 0
def nth2(start):
    nodes = [start]
    s = 0
    while nodes:
        node = nodes.pop()
        for d in fourd:
            n = int(grid[node])
            mstr = grid[node + d]
            if mstr is None or mstr == '.':
                continue
            m = int(mstr)
            if m - n == 1:
                if m == 9:
                    s += 1
                    continue
                nodes.append(node + d)
    return s 

for n in nodes:
    s += nth2(n)
print(s)


