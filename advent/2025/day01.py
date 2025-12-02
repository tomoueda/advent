lines = """L68
L30
R48
L5
R60
L155
L1
L99
R14
L82"""

from aoc import get_input

# lines = get_input(1)

rs = []
for line in lines.split('\n'):
    rs.append((line[0], int(line[1:])))

n = 50
mod = 100

p2 = 0
 
for r in rs:
    if r[0] == 'L':
        n = n % 100
    else:
        n = -n % 100
    h = 100 if n == 0 else n
    if h <= r[1]:
        p2 += 1 + (r[1] - h) // 100
    n = 
print(p2)
