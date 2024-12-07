lines = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""


import re
from aoc import get_input
lines = get_input(7)

combo_set1 = [['*'], ['+']]
op_set1 = ['*', '+']

combo_set2 = [['*'], ['+'], ['||']]
op_set2 = ['*', '+', '||']

def get_combos(n):
    if n == 0:
        return []
    if n == 1:
        return combo_set2
    else:
        combos = get_combos(n - 1)
        _next = []
        for e in op_set2:
            for combo in combos:
                _next.append([e] + combo)
        return _next


def solver(t, ns, combo):
    i = 0
    s = ns[i]
    for op in combo:
        i += 1
        if op == '*':
            s *= ns[i]
        if op == '+':
            s += ns[i]
    if s == t:
        return True
    return False
            

def solve(t, ns):
    combos = get_combos(len(ns) - 1)
    for combo in combos:
        if solver(t, ns, combo):
            return True
    return False

# part 2
def remake(combo, ns):
    i = 1 
    s = ns[0] 
    while i < len(ns):
        if combo[i-1] == '||':
            s = int(str(s) + str(ns[i]))
        elif combo[i - 1] == '*':
            s *= ns[i]
        elif combo[i - 1] == '+':
            s += ns[i]
        i += 1
    return s


def solve2(t, ns):
    combos = get_combos(len(ns) - 1)
    for combo in combos:
        if t == remake(combo, ns):
            return True
    return False


s = 0
for line in lines.splitlines():
    t, args = line.split(':')
    ns = args.split()
    t = int(t)
    ns = list(map(int, ns))
    if solve2(t, ns):
        s += t 
print(s)


