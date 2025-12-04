
lines = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""
from aoc import get_input
lines = get_input(4)

grid = lines.split('\n')
x = len(grid[0])
y = len(grid)


directions = [(1, 0), (1, 1), (0, 1), (0, -1), (-1, 0), (-1, -1), (1, -1), (-1, 1)]


print('part 1')
c = 0
for i in range(x):
    for j in range(y):
        if grid[j][i] == '@':
            neighbors = 0
            for dx, dy in directions:
                if i + dx >= 0 and i + dx < x and j + dy >= 0 and j + dy < y:
                    if grid[j + dy][i + dx] == '@':
                        neighbors += 1
            if neighbors < 4:
                c += 1
print(c)

from collections import defaultdict

dgrid = defaultdict(lambda: None)
rolls = set()
for i in range(x):
    for j in range(y):
        dgrid[(i, j)] = grid[j][i]
        if dgrid[(i, j)] == '@':
            rolls.add((i, j))

prev = None
c = 0
i = 0
while len(rolls) != prev:
    curr = set(rolls)
    prev = len(rolls)
    for i, j in curr:
        neighbors = 0
        for dx, dy in directions:
           if i + dx >= 0 and i + dx < x and j + dy >= 0 and j + dy < y:
               if dgrid[(i + dx, j + dy)] == '@':
                   neighbors += 1
        if neighbors < 4:
            rolls.remove((i, j))
            dgrid[(i, j)] = '.'
            c += 1
print(c)



