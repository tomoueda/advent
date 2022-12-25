from collections import defaultdict
from args import example, actual
from tools import V

arg = actual

n = (0, -1)
nw = (-1, -1)
ne = (1, -1)

s = (0, 1)
sw = (-1, 1)
se = (1, 1)

w = (-1, 0)
e = (1, 0)

all = {n, nw, ne, s, sw, se, w, e}
n_check = [n, nw, ne]
s_check = [s, sw, se]
w_check = [w, sw, nw]
e_check = [e, se, ne]

lines = arg.split('\n')
grid = set() 

j = 0
for line in lines:
    i = 0
    for c in line:
        if c == '#':
            grid.add(V(i, j))
        i += 1
    j += 1

priorities = [n_check, s_check, w_check, e_check]

def pgrid(curr=None):
    s = ''
    for j in range(-7, 14, 1):
        for i in range(-6, 13, 1):
            if (i, j) == curr:
                s += 'x'
            elif (i, j) in grid:
                s += '#'
            else:
                s += '.'
        s += '\n'
    print(s)

def check_dir(elf, checks):
    for check in checks:
        peek = elf + check
        if peek in grid:
            return False
    return True

def get_proposed(elf):
    for dirs in priorities:
        if check_dir(elf, dirs):
            return dirs[0] + elf
    # just stay where I am.
    return elf




rounds = 0
while True:
    proposed = defaultdict(list)
    new_grid = set() 
    for elf in grid:
        if check_dir(elf, all):
            new_grid.add(elf)
            continue
        p = get_proposed(elf)
        if p == elf:
            new_grid.add(p)
        else:
            proposed[p].append(elf)
    
    for p, elves in proposed.items():
        if len(elves) == 1:
            new_grid.add(p)
        elif len(elves) > 1:
            new_grid.update(elves)
    if grid == new_grid:
        print(rounds)
        break
    grid = new_grid
    p = priorities.pop(0)
    priorities.append(p)
    rounds += 1

# bounding xo
x_low = 10000000
x_high = 0
y_low = 10000000
y_high = 0
for elf in grid:
    x_low = min(x_low, elf[0])
    x_high = max(x_high, elf[0])
    y_low = min(y_low, elf[1])
    y_high = max(y_high, elf[1])
s = 0
pgrid()
print(x_low, x_high, y_low, y_high)

s = ''
c = 0 
for j in range(y_low, y_high + 1, 1):
    for i in range(x_low, x_high + 1, 1):
        if (i, j) not in grid:
            c += 1
            s += '.'
        else:
            s += '#'
    s += '\n'
# print(s)
# print(c)

