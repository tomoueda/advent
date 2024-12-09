line = '2333133121414131402'
from aoc import get_input
line = get_input(9)

from collections import Counter, defaultdict


occ = True
disk = []
i = 0
for c in line:
    n = int(c)
    if (occ):
        for j in range(n):
            disk.append(i)
        i += 1
        occ = False
    else:
        for j in range(n):
            disk.append('.')
        occ = True

def swaps(disk):

    i = 0
    j = len(disk) - 1

    while i < j:
        if disk[i] != '.':
            i += 1
        elif disk[j] == '.':
            j -= 1
        else:
            disk[i] = disk[j]
            disk[j] = '.'
            i += 1
    return disk

c = Counter(disk)


def construct(c):
    d = defaultdict(list)    
    for key, val in c.items():
        d[val].append(key)
    for k in d.keys():
        d[k].sort()
    return d 

c = Counter(c) 


highest = i - 1
print(highest)
def filldisk(disk, c):
    curr = -1
    s = 0
    e = 0
    
    seen = set()
    while s < len(disk):
        if disk[s] != '.':
            curr = max(disk[s], curr)
        if e != len(disk) and disk[e] == disk[s]:
            e += 1
        elif disk[s] == '.':
            diff = e - s
            def find_fill():
                for i in range(highest, curr, -1):
                    if c[i] <= diff and c[i] > 0:
                        return i
                return None

            fill = find_fill() 
            if fill is None:
                s = e
                continue
            num = c[fill]
            seen.add(fill)
            for i in range(s, s + num):
                disk[i] = fill
                s += 1
            del c[fill]
        else:
            if disk[s] in seen:
                disk[s] = '.'
            s += 1
    return disk

disk = filldisk(disk, c)
# disk = swaps(disk)

s = 0
for i in range(len(disk)):
    val = disk[i]
    if val == '.':
        continue
    s += val * i
print(s)
