from collections import defaultdict
import math
from args import example, actual
from advent.tools import V
import re

arg = actual 
pattern = '(\d+)'

ore = {}
clay = {}
obs = {}
geo = {}

blueprints = arg.split('\n')
for blueprint in blueprints:
    statements = blueprint.split('.')
    res = re.findall(pattern, statements[0])
    id = int(res[0])
    ore_cost = res[1] 
    ore[id] = int(ore_cost)
    clay[id] = int(re.search(pattern, statements[1]).group(0))
    res = re.findall(pattern, statements[2])
    obs[id] = V(int(res[0]), int(res[1]))
    res = re.findall(pattern, statements[3])
    geo[id] = V(int(res[0]), int(res[1]))

# part 1
import heapq 
def h(m, r):
    """ Look into ones with a lot of geode already.
    Geode bots is great too.
    Then weigh obsidian and obsidian robots 1/10 of it.
    So on and so forth
    """
    h = (1000 * (r[3] + r[7]) + 100 * (r[2] + r[6]) + 10 * (r[1] + r[5]) * (r[0] + r[4]))
    return -h

def h2(m, r):
    """ Look into ones with a lot of geode already.
    Geode bots is great too.
    Then weigh obsidian and obsidian robots 1/10 of it.
    So on and so forth
    """
    m = max(m, 1)
    h = (1000 * (r[3] + r[7]) + 100 * (r[2] + r[6]) + 10 * (r[1] + r[5]) + (r[0] + r[4]))
    return h

def dp_tab(bpid = 1, ease = 200):
    heap = [(0, 32, [0, 0, 0, 0, 1, 0, 0, 0])]
    g = 0
    while len(heap) != 0:
        _, m, r = heapq.heappop(heap) 

        if m == 0:
            g = max(g, r[3])
            # don't bother
            continue            

        o, c, ob = r[0], r[1], r[2]
        # first collect r
        r[0] += r[4]
        r[1] += r[5]
        r[2] += r[6]
        r[3] += r[7]


        # if geode is less than optimal at this time don't bother. 
        cmp = (m * (2 * r[7] + m - 1)) // 2 
        if g - r[3] >= cmp:
            continue

        # check all options
        ocost, obcost = geo[bpid]
        if ob >= obcost and o >= ocost:
            n = list(r)
            n[0] -= ocost 
            n[2] -= obcost
            n[7] += 1
            heapq.heappush(heap, (h(m, n), m - 1, n))

        ocost, ccost = obs[bpid]
        cmp = max(ocost, ccost)
        if c >= ccost and o >= ocost and \
            r[6] * m + r[2] <= obcost * m:
            n = list(r)
            n[0] -= ocost 
            n[1] -= ccost 
            n[6] += 1
            heapq.heappush(heap, (h(m, n), m - 1, n))

        if o >= clay[bpid] and \
            r[5] * m + r[1] <= ccost * m:
            n = list(r)
            n[0] -= clay[bpid]
            n[5] += 1
            heapq.heappush(heap, (h(m, n), m - 1, n))

        ocost = max(clay[bpid], ore[bpid], ocost)
        if o >= ore[bpid] and \
            r[4] * m + r[0] <= ocost * m:
            n = list(r)
            n[0] -= ore[bpid]
            n[4] += 1
            heapq.heappush(heap, (h(m, n), m - 1, n))

        n = list(r)
        heapq.heappush(heap, (h(m, n), m - 1, n))
    return g 

# part 1
# s = 0
# for i in range(len(blueprints)):
#     print('looking', i + 1)
#     res = dp_tab(i + 1)
#     print('optimal', res)
#     s += (i + 1) * res
# print(s)

# part 2
s = 1
for i in range(1, 4):
    print('part', i)
    res = dp_tab(i)
    print('result', res)
    s *= res
print(s)