line = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'

from aoc import get_input
line = get_input(3)

# part 1
inps = line.split('mul')
def part1(inps):
    s = 0
    for elem in inps:
        try: 
            idx1 = elem.index('(')
            if idx1 != 0:
                raise
            idx2 = elem.index(')')
            substr = elem[idx1+1:idx2]
            if ' ' in substr:
                raise
    
    
            num1, num2 = list(map(int, elem[idx1+1:idx2].split(',')))
    
            if num1 >= 1000 or num1 < 0:
                raise
    
            if num2 >= 1000 or num2 < 0:
                raise
    
            s += int(num1) * int(num2)
        except Exception as e:
            pass
    return s
s = part1(inps)
# print(s)

# line='xmul(2,4)&mul[3,7]!^don\'t()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'

# part 2
inps = line.split('do')
s = part1(inps[0].split('mul'))
for elem in inps[1:]:
    if elem[:2] == '()':
        s += part1(elem.split('mul'))
print(s)
