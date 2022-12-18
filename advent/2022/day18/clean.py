from args import example, actual
from advent.tools import V

arg = actual

dirs = [(0, 1, 0), (1, 0, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]

# part 1
def solve(arg):
    lines = arg.split('\n')
    cubes = {V(*map(int, line.split(','))) for line in lines}
    s = 0
    for cube in cubes:
        s += sum([0 if cube + dir in cubes else 1 for dir in dirs])
    return s
print(solve(arg))