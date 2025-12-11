def count_paths(graph, start='you', end='out'):
    def dfs(node):
        if node == end:
            return 1
        if node not in graph:
            return 0
        return sum(dfs(neighbor) for neighbor in graph[node])
    return dfs(start)

with open('day_11/input.txt', 'r') as f:
    lines = f.read().strip().split('\n')

graph = {}
for line in lines:
    device, outputs = line.split(':')
    graph[device.strip()] = outputs.strip().split()

print(count_paths(graph))