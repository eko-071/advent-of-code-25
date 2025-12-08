from math import sqrt

def distance(x, y):
    return sqrt(pow(x[0]-y[0], 2) + pow(x[1]-y[1], 2) + pow(x[2]-y[2], 2))

class kruskal:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)

        if rx == ry:
            return False
        if self.size[rx] < self.size[ry]:
            rx, ry = ry, rx

        self.parent[ry] = rx
        self.size[rx] += self.size[ry]      
        return True

    def sizes(self):
        roots = {}
        for i in range(len(self.parent)):
            root = self.find(i)
            if root not in roots:
                roots[root] = self.size[root]
        return sorted(roots.values(), reverse=True)  

with open("day_8/input_day_8.txt", 'r') as fp:
    input = fp.read().splitlines()

coordinates = list()
for line in input:
    coordinates.append(list(map(int, line.split(","))))

edges = list()
n = len(coordinates)

for i in range(n):
    for j in range(i+1, n):
        dist = distance(coordinates[i], coordinates[j])
        edges.append([dist, i, j])

edges.sort(key=lambda x: x[0])

uf = kruskal(n)
connections = 0

for dist, i, j in edges:
    uf.union(i, j)
    connections += 1
    if connections == 1000:
        break

sizes = uf.sizes()
print(sizes)

print(sizes[0]*sizes[1]*sizes[2])