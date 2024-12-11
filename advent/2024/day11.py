
line = '125 17'
from aoc import get_input
line = get_input(11)

num = list(map(int, line.split()))


memo = {}
def num_stones(n, i):
    key = (n, i)
    if key in memo:
        return memo[key]
    def ans():
        if i == 0:
            return 1
        if n == 0:
            return num_stones(1, i - 1)
        l = len(str(n))
        if l % 2 == 0:
            s = str(n)
            return num_stones(int(s[:l//2]), i - 1) + num_stones(int(s[l//2:]), i - 1)
        return num_stones(n * 2024, i - 1)
    a = ans()
    memo[key] = a
    return memo[key]


    


s = 0
i = 0
for n in num:
    i += 1
    n = num_stones(n, 75)
    s += n
print(s)
