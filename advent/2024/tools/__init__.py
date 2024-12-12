
class V:
    def __init__(self, *args):
        self.coor = tuple(args) 
    
    def __add__(self, o):
        if isinstance(o, int):
            # makes it work for sum
            if o == 0:
                return self
            raise Exception('cant add a scalar')
        if len(self) != len(o):
            raise Exception('unequal lengths')
        return V(*[e[0] + e[1] for e in zip(self.coor, o)])

    def __sub__(self, o):
        if isinstance(o, int):
            # makes it work for sum
            if o == 0:
                return self
            raise Exception('cant add a scalar')
        if len(self) != len(o):
            raise Exception('unequal lengths')
        return V(*[e[0] - e[1] for e in zip(self.coor, o)])

    def __radd__(self, o):
        if isinstance(o, int):
            if o == 0:
                return self
            raise Exception('cant add a scalar')

        if len(self) != len(o):
            raise Exception('unequal lengths')
        return V(*[e[0] + e[1] for e in zip(self.coor, o)])

    def __rmul__(self, o):
        if isinstance(o, int):
            return V(*[o * e for e in self.coor])
        if len(self) != len(o):
            raise Exception('unequal lengths')
        return V(*[e[0] * e[1] for e in zip(self.coor, o)])

    def __getitem__(self, key):
        return self.coor[key]

    def __hash__(self):
        return hash(self.coor)

    def __eq__(self, o):
        if isinstance(o, tuple):
            return self.coor == o
        return self.coor == o.coor

    def __str__(self):
        return str(self.coor)

    def __repr__(self):
        return str(self.coor)

    def __len__(self):
        return len(self.coor)


fourd = [V(1, 0), V(-1, 0), V(0, 1), V(0, -1)]
diags = [V(1, 1), V(1, -1), V(-1, -1), V(-1, 1)]
def test():
    assert V(1, 2) + (3, 4) == (4, 6)
    assert 3 * V(1, 2) == (3, 6)
    assert (3, 4) * V(1, 2) == (3, 8)
    assert V(1, 2, 3) + (3, 4, 5) == (4, 6, 8)
test()


from collections import defaultdict

def get_grid(lines):
    grid = defaultdict(lambda: None)
    rows = lines.splitlines()
    for i in range(len(rows)):
        for j in range(len(rows[0])):
            grid[V(j, i)] = rows[i][j]
    return grid, len(rows[0]), len(rows)

def printg(grid, x, y):
    s = ''
    for i in range(y):
        for j in range(x):
            s += grid[(j, i)]
        s += '\n'
    print(s)
