
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
from tools import V, get_grid, printg
from itertools import combinations  

grid, x, y = get_grid(lines)

locations = defaultdict(list)
for key, val in grid.items():
    if val != '.':
        locations[val].append(key)

def part1(grid):
    for nodes in locations.values():
        pairs = combinations(nodes, 2)
        for a, b in pairs:
            idx = 2 * b - a
            if idx in grid:
                grid[idx] = '#'
            idx = 2 * a - b
            if idx in grid:
                grid[idx] = '#'
    return grid

def part2(grid):
    for nodes in locations.values():
        pairs = combinations(nodes, 2)
        for a, b in pairs:
            grid[a] = '#'
            grid[b] = '#'
            idx = a 
            while idx in grid:
                grid[idx] = '#'
                idx += (b - a)
            idx = b
            while idx in grid:
                grid[idx] = '#'
                idx += (a - b)
    return grid

grid = part2(grid)
print(list(grid.values()).count('#'))
