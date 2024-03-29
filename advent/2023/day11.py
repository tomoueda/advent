ex = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

actual = """.........#................................#................#.................#..........................#...........................#.......
.#............#...................................................................................#.........................................
...................................................................................................................#...........#............
.........................#......................................#........#..................................................................
...................#.....................................................................................................#..................
.......................................#..................................................#.......................................#.........
.............#..................#.....................................#............................#.....#.......#........................#.
...........................................#................................................................................................
#...................................#............................................#....................................#.....................
............................................................................................#...............................................
.............................................................................#.........#....................................................
....#....................#...............#.........#...............#....................................................................#...
..................#.........................................................................................................................
.........................................................#................................#......................#.............#............
...................................................................................#...................#....................................
.....................#...............#........#............................#................................................................
..#.....#......#................#......................................................#....................................................
.........................#......................................#............................................#..........#..............#....
..........................................................#.................................................................................
............................................................................................................................................
...................................#.................................#........#............#.......................#........................
.............#.............................#.........................................................#......................................
..................................................#............................................................................#.....#......
.........................#.....................................................................................#............................
.......#......................................#....................................#.........#..........#...................................
....................#.....................................#..............#..................................................................
.............................#......#.......................................................................................................
............................................................................................................................#.....#.........
...........#................................#...............................................................................................
....#............................#................................................................#..........#..............................
..................................................................................................................#.......................#.
................#........#..............#...................#..........................................#....................................
...................................................#........................#...................................................#...........
.........#....................................#..............................................#........................................#.....
..#...........................................................................................................#.............................
...................................................................................................#....................#...................
...........................................#.....................#.......................#.........................................#........
...................#.........#..............................#............#.....#............................................................
..............#..................................#...................................................................#......................
........................#...................................................................................................................
.......................................#...................................................#.....#.....#.................#..................
................................#............#......#...........................................................#...............#...........
........#.........#..................................................#..................................................................#...
..........................#.................................................................................#...............................
..........................................#.....................#........#........#.........................................#...............
.........................................................#....................................#.............................................
....................................#..........#............................................................................................
..#......#..................#...............................................#...........#................#........#.........................
......................................................................#.....................................................................
............................................................................................................................................
..........................................................#.................................#...........................#.............#.....
............................................................................................................................................
......................#.............................................................#............#..........#...............................
#..........#................................................................................................................................
.................#.................#................................#.........................................................#.............
............................................................................................................................................
..........................#.............#...................................#................#.......................#......................
............................................................................................................................................
........................................................#..................................................................................#
..........#.....................#............#...............#...................#..........................................................
#...................#..................................................................................#....................................
............................................................................................................................................
.........................................#.........................#......#......................#....................#.....................
..........................#.................................................................#...................#.................#.........
..................................................#.........................................................................#...............
............................................................................................................................................
.....#......................................................................#........................#..................#...................
................................................................#.....#...................................#.................................
..........#.......................#.....................#......................................................................#......#.....
................#................................#..............................................#...........................................
#.....................#......#.................................................#............................................................
............................................................................................................................................
..............................................................#.......................................................#.................#...
......#.............................#......#.......#...............#.......................#.............#.................#.....#..........
....................#....................................#..................................................................................
...............................#................................................................................#...........................
..........................#.......................................................................#.........................................
.#............................................#..........................#..................................................................
........#.....#...............................................#..........................#............#......#........................#.....
............................................................................................................................................
........................................................#.................................................................#.................
............................................................................................................................................
............#................#.........#.................................................................#.......#................#........#
.................................................#..........................#..............#...........................#....................
...#.............#.......#.................#................................................................................................
............................................................................................................................................
.....................................#....................#.............#.......................#...........................................
.....................#.............................#....................................................#...................................
............#..................................................................................................#............................
.............................................................................#.....#........................................#...............
..................#...........................................#............................................................................#
...............................#........#.............................#.....................................................................
.........#...............#................................#.................................................................................
...#...............................#...................................................................#....................................
...........................................................................#...........#....................................................
................................................................................#...........................................................
.............................#.................#...................#............................................................#..........#
............#...............................................................................#...............................................
.....................#..................#.....................#....................#...............................#......#.................
................#.......................................................................#.........#.........................................
..........................................................................#................................#................................
................................................#................#...............................................................#..........
.........................#......#..............................................#.................................#..........................
..................#..................#...............................#.....................#.........................................#......
............#......................................................................#..................#.....................................
.....#......................................................................................................#...............................
......................#.....#...............#......#..........................................#...........................#...............#.
............................................................#..........................#....................................................
......................................#.........................................................................#...........................
......................................................................#................................................#......#.............
....................#..........................................#...................#.......#................................................
#.........................................#.................................#............................................................#..
...................................................#...................................................#...................#................
............................................................#......#.................................................#......................
.....#.........................#.............................................................#..................#...........................
.........................................................................#........................................................#.........
............................................................................................................................................
.....................................#......................................................................................................
........................#..................................#...............................#................#.......#......#................
.............................#....................#....................................................#...................................#
..................#..........................#.....................................................................................#........
...............................................................#...........#..................#.............................................
.................................#.................................................................#........................................
.......................................................................................#....................................................
..#................................................#........#...............................................................................
...........#...............................#......................................#.............................#.......#...........#.......
........................#...................................................................................................................
......#................................#....................................#..................#.....#......................................
..................#.....................................#..........#........................................................#...............
.............................#.............................................................................................................#
............#.....................................................................................................................#.........
..............................................#.........................#.................#.................................................
.....#.......................................................#..............................................................................
.....................................#...................................................................#..............#...................
...................................................................................................................#........................
...................#......#.....#........#.........................#...............#........................................................
.....................................................................................................................................#......
...........#.......................................#............................................................#..........#................
......................#.................................#..............#.....#...................#.......................................#..
............................#........#...........................#..........................#..............................................."""


# new_universe = ''
# rows = ex.split('\n')
# for row in rows:
#     if '#' not in row:
#         new_universe += '.' * len(row) + '\n'
#     new_universe += row + '\n'
# new_universe = new_universe.strip()
# 
# final_universe = ''
# rows = new_universe.split('\n')
# for i in range(len(rows[0])):
#     col = ''
#     for j in range(len(rows)):
#         col += rows[j][i]
#     if '#' not in col:
#         final_universe += '.' * len(col) + '\n'
#     final_universe += col + '\n'
# final_universe = final_universe.strip()
# 
# quads = final_universe.split('\n')
# from collections import defaultdict
# uni = defaultdict(lambda: None)
# galaxies = []
# for y in range(len(quads)):
#     for x in range(len(quads[0])):
#         if quads[y][x] == '#':
#             galaxies.append((x, y))
#         uni[(x, y)] = quads[y][x]
# 
# 
# s = 0
# for i in range(len(galaxies)):
#     for j in range(i + 1, len(galaxies)):
#         g1 = galaxies[i]
#         g2 = galaxies[j]
#         s += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
# print(s)
# 

# part 2 
new_universe = ''
rows = actual.split('\n')
ex_rows = []
ex_cols = []
for i in range(len(rows)):
    row = rows[i]
    if '#' not in row:
        ex_rows.append(i)

for i in range(len(rows[0])):
    col = ''
    for j in range(len(rows)):
        col += rows[j][i]
    if '#' not in col:
        ex_cols.append(i)

galaxies = []
for y in range(len(rows)):
    for x in range(len(rows[0])):
        if rows[y][x] == '#':
            galaxies.append((x, y))

def dist(x1, x2):
    if x1 > x2:
        t = x2
        x2 = x1
        x1 = t
    d = x2 - x1
    for r in ex_cols:
        if x1 < r and r < x2:
            d += 999999
    return d

def dist_c(x1, x2):
    if x1 > x2:
        t = x2
        x2 = x1
        x1 = t
    d = x2 - x1
    for r in ex_rows:
        if x1 < r and r < x2:
            d += 999999
    return d


s = 0
for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        g1 = galaxies[i]
        g2 = galaxies[j]
        s += dist(g1[0], g2[0]) + dist_c(g1[1], g2[1])
print(s)
