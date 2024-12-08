
lines = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

from collections import defaultdict
from tools import V
from aoc import get_input

lines = get_input(8)


grid = defaultdict(lambda: None)
locations = defaultdict(list)

rows = lines.splitlines()

for i in range(len(rows)):
    for j in range(len(rows[0])):
        grid[V(j, i)] = rows[i][j]
        if rows[i][j] != '.':
            locations[rows[i][j]].append(V(j, i))

def part1(grid):
    for val in locations.values():
        for l in val:
            for j in val:
                if l != j:
                    if grid[2 * j - l] is not None:
                        grid[2 * j - l] = '#'
    return grid

def part2(grid):
    for val in locations.values():
        for l in val:
            grid[l] = '#'
            for j in val:
                if l != j:
                    # positive
                    offset = j + j
                    while grid[offset - l] is not None:
                        grid[offset - l] = '#'
                        offset += (j - l)
    return grid




def print_grid(grid):
    s = ''
    for i in range(len(rows)):
        for j in range(len(rows[0])):
            s += grid[(j, i)]
        s += '\n'
    print(s)


grid = part2(grid)

s = 0
for c in grid.values():
    if c == '#':
        s += 1
print(s)
