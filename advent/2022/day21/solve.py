from args import example, actual
import re

arg = actual 

lines = arg.split('\n')
monkeys = {}

def add(a, b):
    return a + b

def mult(a, b):
    return a * b

def sub(a, b):
    return a - b

def div(a, b):
    return a // b

ops = {'+': add, '-': sub, '*': mult, '/': div}


for line in lines:
    parsed = line.split(': ')
    name = parsed[0]
    val = parsed[1]
    isop = False
    for op in ops.keys():
        if op in val:
            isop = True
            others = val.split(op)
            monkeys[name] = (others[0].strip(), op, others[1].strip())
            break
    if not isop:
        monkeys[name] = int(val)

def solve(monkey='root'):
    val = monkeys[monkey]
    if isinstance(val, int):
        return val
    a = solve(val[0])
    op = ops[val[1]]
    b = solve(val[2])
    return op(a, b)

# print(solve())

rev = {'*': div, '/': mult, '-': add, '+': sub}

def solve2(monkey='root'):
    val = monkeys[monkey]
    if monkey == 'root':
        has_humn, stack, ans = solve2(val[0])
        _, stack2, ans2 = solve2(val[2])
        print(ans, ans2)
        look = stack if has_humn else stack2
        c = ans2 if has_humn else ans 
        print(look, c)
        while len(look):
            i, j = look.pop()
            a, o, b = None, None, None
            #  4 + x = w
            if type(i) == int or type(i) == float:
                if j in {'/', '-'}:
                    a = i
                    b = c
                    o = ops[j]
                else:
                    a = c
                    b = i
                    o = rev[j]
            # x + 4 = w
            else:
                a = c 
                b = j
                o = rev[i]
            c = o(a, b)
            print(c)
        return c
    if monkey == 'humn':
        return True, [], 0
    if isinstance(val, int):
        return False, [], val
    has_humn, stack, ans = solve2(val[0])
    has_humn2, stack2, ans2 = solve2(val[2])
    op = ops[val[1]]
    if has_humn:
        stack.append((val[1], ans2))
        return has_humn, stack, ans
    if has_humn2:
        stack2.append((ans, val[1]))
        return has_humn2, stack2, ans2
    return False, None, op(ans, ans2)
    
print(solve2())


