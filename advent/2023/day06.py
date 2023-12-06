
sample = """Time:      7  15   30
Distance:  9  40  200"""

actual = """Time:        54     81     70     88
Distance:   446   1292   1035   1007"""

inps = sample.split('\n')
times = list(map(int, inps[0].split(':')[1].split()))
distances = list(map(int, inps[1].split(':')[1].split()))


#m = 1
#for i in range(len(times)):
#    time = times[i]
#    distance = distances[i]
#    c = 0
#    for j in range(time):
#        if j * (time - j) > distance:
#            c += 1
#    m *= c

#part 2
inps = actual.split('\n')
time = int(inps[0].split(':')[1].replace(' ', ''))
distance = int(inps[1].split(':')[1].replace(' ', ''))
s = 0
for i in range(time):
    if i * (time - i) > distance:
        s += 1 
print(s)
# distances = list(map(int, inps[1].split(':')[1].split()))

