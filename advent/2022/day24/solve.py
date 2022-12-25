from collections import defaultdict
import heapq
from args import example2, actual
from tools import V

arg = actual 

lines = arg.split('\n')
start = (1, 0)
u = V(0, -1)
d = V(0, 1)
r = V(1, 0)
l = V(-1, 0)
noop = V(0, 0)
all = {u, d, r, l, noop}
dirmap = {'>': r, '<': l, '^': u, 'v': d}
grid = defaultdict(lambda: None)

j = 0
for line in lines:
    i = 0
    for c in line:
        if c != '.':
            grid[i, j] = c
        i += 1
    j += 1
end = V(i-2, j - 1)

hurricane_memo = {0: grid}
def next_state(i):
    if i + 1 in hurricane_memo:
        return hurricane_memo[i + 1]
    state = hurricane_memo[i]
    n = defaultdict(lambda: None)
    for pos, node in state.items():
        def move_hurricane(pos, node):
            dir = dirmap[node]
            next_pos = pos + dir

            # if hit a wall wrap
            if next_pos in state and state[next_pos] == '#':
                if dir == r:
                    next_pos = (1, next_pos[1])
                elif dir == l:
                    next_pos = (end[0], next_pos[1])
                elif dir == u:
                    next_pos = (next_pos[0], end[1] - 1)
                elif dir == d:
                    next_pos = (next_pos[0], 1)

            if next_pos in n and type(n[next_pos]) == list:
                n[next_pos].append(node)
            elif next_pos in n and n[next_pos] in dirmap:
                # create a list
                n[next_pos] = [node, n[next_pos]]
            else:
                n[next_pos] = node
        if type(node) == list:
            for hurr in node:
                move_hurricane(pos, hurr)
        elif node in dirmap:
            move_hurricane(pos, node)
        else:
            n[pos] = node
    hurricane_memo[i + 1] = n
    return n

def pgrid(grid=grid, curr=None):
    s = '' 
    for j in range(end[1] + 1):
        for i in range(end[0] + 2):
            if (i, j) == curr:
                s += 'X'
            elif (i, j) in grid:
                if type(grid[i, j]) == list:
                    s += str(len(grid[i, j]))
                else:
                    s += grid[i, j]
            else:
                s += '.'
        s += '\n'
    print(s)

def solve():
    def get_dist(curr, state):
        return abs(curr[0] - end[0]) + abs(curr[1] - end[1]) + state
    heap = [(get_dist(start, 0), start, 0)]
    visited = set() 
    while len(heap) != 0:
        h, curr, state = heapq.heappop(heap)
        if curr == end:
            print(state)
            break
        if (curr, state) not in visited:
            visited.add((curr, state))
            grid = next_state(state)
            for dir in all:
                n = curr + dir 
                nh = get_dist(n, state)
                if n not in grid and n[0] > 0 and n[1] > 0:
                    heapq.heappush(heap, (nh, n, state + 1))

def solve2():
    final = end
    def get_dist(curr, state):
        return abs(curr[0] - final[0]) + abs(curr[1] - final[1]) + state
    heap = [(get_dist(start, 0), start, 0)]
    visited = set() 
    goals = 0
    while len(heap) != 0:
        _, curr, state = heapq.heappop(heap)
        if curr == final:
            heap = [(get_dist(curr, state), curr, state)]
            goals += 1
            if final == end:
                final = start
            elif final == start:
                final = end
            if goals == 3:
                print(state)
                break
            continue
        if (curr, state) not in visited:
            visited.add((curr, state))
            grid = next_state(state)
            for dir in all:
                n = curr + dir 
                nh = get_dist(n, state)
                if n not in grid and n[0] >= 0 and n[1] >= 0 and n[0] < end[0] + 2 and n[1] < end[1] + 1:
                    heapq.heappush(heap, (nh, n, state + 1))
    visited = set()
solve2()