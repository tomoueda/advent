lines = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

from collections import defaultdict
from tools import V
from aoc import get_input
lines = get_input(6)


lines = lines.splitlines()

def get_grid():
    pos = None
    grid = defaultdict(lambda: None)
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            node = lines[i][j]
            grid[V(j, i)] = node
            if node == '^':
                pos = V(j, i) 
    return pos, grid

pos, grid = get_grid()

d = [V(0, -1), V(1, 0), V(0, 1), V(-1, 0)]

# part 1
i = 0
#while grid[pos] is not None:
#    next_pos = pos + d[i]
#    if grid[next_pos] == '#':
#        i += 1
#        if i == 4:
#            i = 0
#        continue
#    grid[pos] = 'x'
#    pos = next_pos
#print(sum([1 if x == 'x' else 0 for x in grid.values()]))

def print_grid(grid, slow, fast):
    s = ''
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            n = V(j, i)
            if n == slow: 
                s += 's'
            elif n == fast:
                s += 'f'
            else:
                s += grid[n]
        s += '\n'
    print(s)




def traverse(pos, grid):
    collide = 0
    si = 0
    fi = 0
    slow = pos + d[si]
    fast = pos + 2 * d[fi]
    while True:
        #print(slow, fast)
        #print_grid(grid, slow, fast)

        moves = 0
        while moves < 1:
            # move slow
            next_slow = slow + d[si]
            if grid[next_slow] == '#':
                si += 1 
                si %= 4
                continue
            if grid[next_slow] is None:
                # no cycle
                return False
            moves += 1
            slow = next_slow

        # move fast
        moves = 0
        while moves < 2:
            next_fast = fast + d[fi]
            if grid[next_fast] == '#':
                fi += 1
                fi %= 4
                continue
            if grid[next_fast] is None:
                return False
            moves += 1
            fast = next_fast

        if fast == slow:
            collide += 1
            # print(slow, fast)
            # print_grid(grid, slow, fast)

        if collide == 2:
            return True

# pos, grid = get_grid()
# grid[V(3, 6)] = '#'
# traverse(pos, grid)

s = 0
for i in range(len(lines)):
    for j in range(len(lines[0])):
        pos, grid = get_grid()
        grid[V(j, i)] = '#'
        if traverse(pos, grid):
            print(V(j, i))
            s += 1
print(s)


#(5, 1)
#(8, 2)
#(2, 5)
#(3, 6)
#(6, 7)
#(7, 7)
#(1, 8)
#(3, 8)
#(7, 9)
