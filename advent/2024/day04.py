line = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

from aoc import get_input
line = get_input(4).rstrip()

lines = line.splitlines()
from collections import defaultdict
from tools import V
grid = defaultdict(lambda: None) 

DIRS = [V(1, 0), V(0, 1), V(-1, 0), V(0, -1), V(1, 1), V(-1, 1), V(-1, -1), V(1, -1)]

for x in range(len(lines)):
    for y in range(len(lines[0])):
        grid[V(x, y)] = lines[y][x]

key = 'XMAS'

# part 1
# s = 0
# idx = list(grid.keys())
# for pos in idx:
#     for d in DIRS:
#         i = 0
#         curr = V(*pos)
#         while True:
#             if i == 4:
#                 s += 1
#                 break
#             if grid[curr] != key[i]:
#                 break
#             curr += d
#             i += 1
# print(s)
        

# part 2
idx = list(grid.keys())
dir1 = [(V(1, 1), V(-1, -1)), (V(-1, 1), V(1, -1))]

s = 0
for pos in idx:
    if grid[pos] != 'A':
        continue
    try:
        for ds in dir1:
            d1, d2 = ds
            m = grid[pos + d1] + grid[pos + d2]
            if m != 'MS' and m != 'SM':
                raise
        s += 1
    except:
        pass
print(s)
