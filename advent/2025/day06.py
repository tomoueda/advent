lines = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

from aoc import get_input
lines = get_input(6)

lines = lines.split('\n')
operations = lines[-1]

operations = operations.split()
n = len(operations)

ans = 0
for i in range(n):
    operation = operations[i]
    s = 0
    if operation == '*':
        s = 1 
    for j in lines[:len(lines)-1]:
        num = int(j.split()[i])
        if operation == '+':
            s += num
        else:
            s *= num
    ans += s
print(ans)

print('part 2')
def compute(operation, strings):
    print(operation, strings)
    return 0

max_ls = {}
for i in range(n):
    operation = operations[i]
    max_l = 0
    for j in lines[:len(lines)-1]:
        num = j.split()[i]
        max_l = max(max_l, len(num))
    max_ls[i] = max_l

from collections import defaultdict
num_strings = defaultdict(list)
for j in lines[:len(lines)-1]:
    start = 0
    for i in range(n):
        max_l = max_ls[i]
        num_strings[i].append(j[start:start+max_l])
        start += max_l + 1

ans = 0
for i in range(n):
    operation = operations[i]
    p = 0
    if operation == '*':
        p = 1
    for j in range(max_ls[i]):
        s = ''
        for num_string in num_strings[i]:
            if num_string[j] != ' ':
                s += num_string[j]
        s = int(s)
        if operation == '+':
            p += s
        else:
            p *= s
    ans += p
print(ans)


