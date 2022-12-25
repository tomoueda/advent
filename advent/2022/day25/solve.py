from args import example, actual

arg = actual 

lines = arg.split('\n')

base = 5
def from_snafu(line):
    m = len(line) - 1
    s = 0
    for c in line:
        if c == '=':
            s -= 2 * (5 ** m)
        elif c == '-':
            s -= (5 ** m)
        else:
            s += int(c) * (5 ** m)
        m -= 1
    return s

# each one could be =, -, 0, 1, 2
def to_snafu(i):
    s = '' 
    p = 0
    while (5 ** p) < i:
        r = (i % 5 ** (p + 1)) // 5 ** p
        if r > 2:
            carry = 5 - r
            i += carry * 5 ** p 
            if carry == 1: 
                r = '-'
            if carry == 2:
                r = '='
        s = str(r) + s
        p += 1
    return s
        
def solve():
    s = 0
    for line in lines:
        s += from_snafu(line) 
    return to_snafu(s)
print(solve())



