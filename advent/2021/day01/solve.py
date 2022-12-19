from args import example, actual

arg = actual 

ints = [int(x) for x in arg.split('\n')] 
def part1():
    print(sum([ints[i-1] < ints[i] for i in range(1, len(ints))]))
part1()

def part2():
    print(sum([sum(ints[i-1:i+2]) < sum(ints[i:i+3]) for i in range(1, len(ints) - 2)]))
part2()