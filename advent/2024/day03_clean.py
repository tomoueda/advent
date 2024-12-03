import re
from aoc import get_input
line = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'

line = get_input(3)
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
matches = re.findall(pattern, line)


s = 0
for a, b in matches:
    s += int(a) * int(b)
print(s)

