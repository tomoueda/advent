from collections import defaultdict, deque
from tools import V
from args import actual, example, example2

arg = actual 
inputs = arg.split('\n\n')
cube_len = len((inputs[0].split('\n'))[0]) // 3
grid = defaultdict(lambda: None) 

max_x = 0 
max_y = 0 
sides = defaultdict(lambda: defaultdict(lambda: None))

i, j = 0, 0
for c in inputs[0]:
    if c == ' ':
        i += 1
        continue
    elif c == '\n':
        j += 1
        i = 0
        continue
    else:
        grid[i, j] = c
        if (i // cube_len == 1 and j // cube_len == 0):
            sides[1][i, j] = c
        if (i // cube_len == 2 and j // cube_len == 0):
            sides[2][i, j] = c
        if (i // cube_len == 1 and j // cube_len == 1):
            sides[3][i, j] = c
        if (i // cube_len == 0 and j // cube_len == 2):
            sides[4][i, j] = c
        if (i // cube_len == 1 and j // cube_len == 2):
            sides[5][i, j] = c
        if (i // cube_len == 0 and j // cube_len == 3):
            sides[6][i, j] = c



        max_x = max(i, max_x)
        max_y = max(j, max_y)
        i += 1

for i in range(max_x + 1):
    if grid[i, 0] is not None:
        leftmost = i, 0
        break

instrs = deque()
s = ''
for c in inputs[1].strip():
    if c in '0123456789':
        s += c
    else:
        instrs.append(int(s))
        instrs.append(c)
        s = ''
instrs.append(int(s))

r = V(1, 0)
u = V(0, -1)
l = V(-1, 0)
d = V(0, 1)
score = {r: 0, d: 1, l: 2, u: 3}
    

cube_sets = {}
cube_dir = {(1, u)}

def cw(dir):
    if dir == r:
        return d
    if dir == d:
        return l 
    if dir == l:
        return u
    if dir == u:
        return r
    raise Exception()

def ccw(dir):
    if dir == r:
        return u
    if dir == d:
        return r 
    if dir == l:
        return d 
    if dir == u:
        return l 
    raise Exception()



def wraparound(curr, facing):
    # curr hit None, keeping going facing until you hit boundary.
    # if wrap around is a block then return original curr
    peek = curr
    while grid[peek] == None:
        peek += facing
        if facing == r and peek[0] > max_x:
            peek = (0, peek[1])
        if facing == d and peek[1] > max_y:
            peek = (peek[0], 0)
        if facing == l and peek[0] < 0:
            peek = (max_x, peek[1])
        if facing == u and peek[1] < 0:
            peek = (peek[0], max_y)
    if grid[peek] == '#':
        return curr
    return peek

def find_side(curr):
    for i in range(1, 7):
        if curr in sides[i]:
            return i
    raise Exception()

seen = set()
def get_dir(dir):
    if dir == u:
        return 'up'
    if dir == d:
        return 'down'
    if dir == l:
        return 'left'
    if dir == r:
        return 'right'


def wraparound2(curr, facing, cube_len=cube_len):
    # assume current is in one of the cube
    side = find_side(curr)
    peek = side
    peek_facing = facing
    if side == 1:
        if facing == u:
            peek = (0, curr[0] + cube_len * 2)
            peek_facing = r 
        elif facing == l:
            peek = (0, cube_len * 3 - 1 - curr[1])
            peek_facing = r
    elif side == 2:
        if facing == u:
            peek = (curr[0] - cube_len * 2, cube_len * 4 - 1)
            peek_facing = u
        elif facing == r:
            peek = (cube_len * 2 - 1, cube_len * 3 - 1 - curr[1])
            peek_facing = l
        elif facing == d:
            peek = (cube_len * 2 - 1, curr[0] - cube_len)
            peek_facing = l
    elif side == 3:
        if facing == l:
            peek = (curr[1] - cube_len, cube_len * 2)
            peek_facing = d
        elif facing == r:
            peek = (curr[1] + cube_len, cube_len - 1)
            peek_facing = u
    elif side == 4:
        if facing == l:
            peek = (cube_len, cube_len * 3 - 1 - curr[1])
            peek_facing = r
        elif facing == u:
            peek = (cube_len, cube_len + curr[0])
            peek_facing = r
    elif side == 5:
        if facing == r:
            peek = (cube_len * 3 - 1, cube_len * 3 - 1 - curr[1])
            peek_facing = l
        elif facing == d:
            peek = (cube_len - 1, curr[0] + cube_len * 2)
            peek_facing = l
    elif side == 6:
        if facing == r:
            peek = (curr[1] - cube_len * 2, cube_len * 3 - 1)
            peek_facing = u
        elif facing == d:
            peek = (curr[0] + cube_len * 2, 0)
            peek_facing = d
        elif facing == l:
            peek = (curr[1] - cube_len * 2, 0)
            peek_facing = d
    if grid[peek] == '#':
        return curr, facing
    other_side = find_side(peek)
    if (side, other_side, get_dir(facing), get_dir(peek_facing)) not in seen:
        print(side, other_side, get_dir(facing), get_dir(peek_facing))
        seen.add((side, other_side, get_dir(facing), get_dir(peek_facing)))

    return peek, peek_facing



def print_grid(curr, grid=grid):
    s = '' 
    sx, lx = 300, -1
    sy, ly = 300, -1
    for num in grid:
        sx = min(num[0], sx)
        sy = min(num[1], sy)
        lx = max(num[0], lx)
        ly = max(num[1], ly)
    print(sx, lx, sy, ly)
    for j in range(sy, ly + 1):
        for i in range(sx, lx + 1):
            if curr == (i, j):
                s += 'x'
            elif grid[i, j] == None:
                s += ' '
            else:
                s += grid[i, j]
        s += '\n'
    print(s)
    print()
    print()
    print()

        
def solve(wraparound=wraparound2):

    curr = leftmost
    facing = r
    while len(instrs) != 0:
        inst = instrs.popleft()
        if type(inst) == int:
            for i in range(inst):
                side = find_side(curr)
                # print(instrs)
                # print(inst, facing, side, curr, get_dir(facing))
                # print_grid(curr, grid=grid)
                peek = curr + facing 
                if grid[peek] == None:
                    # find wraparound
                    # temp = wraparound(peek, facing) # part 1
                    temp, new_facing = wraparound(curr, facing)
                    if temp == curr:
                        break
                    curr = temp
                    facing = new_facing
                    continue
                elif grid[peek] == '#':
                    # we done
                    break
                elif grid[peek] == '.':
                    curr = peek
                    continue
                raise Exception('char shoulndt be here')
        elif inst == 'R':
            facing = cw(facing)
        elif inst == 'L':
            facing = ccw(facing)

    print(curr)
    print(4 * (curr[0] + 1) +  1000 * (curr[1] + 1) + score[facing])
    print(4 * (curr[0]) +  1000 * (curr[1]) + score[facing])
    print(1000 * (curr[0]) +  4 * (curr[1]) + score[facing])

solve()

