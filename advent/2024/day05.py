lines = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

from collections import defaultdict
from aoc import get_input
lines = get_input(5)
rules, sections = lines.split('\n\n')


graph = defaultdict(list)

for rule in rules.splitlines():
    b, a = rule.split('|')
    graph[b].append(a)

def _pass(section):
    pages = section.split(',')
    for i in range(len(pages)):
        node = pages[i]
        for j in range(i+1, len(pages)):
            comp = pages[j]
            if comp in graph[node]:
                continue
            else:
                return False
    return True

# part 1 
# i = 0
# for section in sections.splitlines():
#     if _pass(section):
#         pages = section.split(',')
#         l = len(pages)
#         i += int(pages[int(l/2)])
# 
# print(i)

def _pass2(section):
    pages = section.split(',')
    c = defaultdict(lambda: 0)
    for i in range(len(pages)):
        node = pages[i]
        for j in range(len(pages)):
            if i == j:
                continue
            comp = pages[j]
            if comp in graph[node]:
                continue
            else:
                c[node] += 1
        if node not in c:
            c[node] = 0
    c = sorted(c.items(), key=lambda item: item[1])
    return int(c[int(len(c) / 2)][0])


# part 2
i = 0
for section in sections.splitlines():
    if not _pass(section):
        i += _pass2(section)
print(i)
