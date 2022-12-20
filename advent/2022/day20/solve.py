from args import example, actual
arg = actual 

ints = [int(x) for x in arg.split('\n')]
i = 1 
seq = []
for x in ints:
    if x == 0:
        seq.append((0, x))
        continue
    seq.append((i, x))
    i += 1

def swap_left(curr, i):
    t = curr[i]
    left = i - 1
    if left == -1:
        left = len(seq) - 1
    curr[i] = curr[left]
    curr[left] = t
    return left 
    
def swap_right(curr, i):
    t = curr[i]
    right = i + 1
    if right == len(seq):
        right = 0
    curr[i] = curr[right]
    curr[right] = t
    return right

def solve():
    curr = list(seq)
    for elem in seq:
        i = curr.index(elem)
        f = swap_right if elem[1] > 0 else swap_left
        for _ in range(abs(elem[1]) % (len(seq) - 1)):
            i = f(curr, i)
    idx0 = curr.index((0, 0))
    print(sum([curr[(idx0 + i * 1000) % len(seq)][1] for i in range(1, 4)]))
# solve()

def solve2(seq=seq):
    decrypt = 811589153
    seq = [(x[0], x[1] * decrypt) for x in seq]
    curr = list(seq)
    # print(curr)
    for _ in range(10):
        for elem in seq:
            i = curr.index(elem)
            f = swap_right if elem[1] > 0 else swap_left
            for _ in range(abs(elem[1]) % (len(seq) - 1)):
                i = f(curr, i)
        # print(curr)
    idx0 = curr.index((0, 0))
    print(sum([curr[(idx0 + i * 1000) % len(seq)][1] for i in range(1, 4)]))
solve2()
