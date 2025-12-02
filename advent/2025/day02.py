
lines = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""

from aoc import get_input
lines = get_input(2)

s = 0
lines = lines.split(',')
for num_range in lines:
    num_range = num_range.strip()
    start, end = num_range.split('-')
    if len(start) % 2 != 0 and len(end) % 2 != 0:
        continue
    start, end = map(int, num_range.split('-'))
    for i in range(start, end + 1):
        i = str(i)
        mid = len(i) // 2
        if i[:mid] == i[mid:]:
            s += int(i)
print(s)
        

def is_repeating(i):
    i = str(i)
    for j in range(1, (len(i) // 2) + 1):
        start = 0
        end = j
        prev = i[start:end]

        repeat = True
        while end < len(i):
            if prev != i[start+j:end+j]:
                repeat = False
                break
            start += j
            end += j
        if repeat:
            return True
    return False

        
s = 0
print('# part 2')
for num_range in lines:
    num_range = num_range.strip()
    start, end = map(int, num_range.split('-'))
    for i in range(start, end + 1):
        if is_repeating(i):
            s += i
print(s)


