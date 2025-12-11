def count_paths_with_required(graph, start='svr', end='out', required={'dac', 'fft'}):
    memo = {}
    
    def dfs(node, visited_required):
        key = (node, frozenset(visited_required))
        if key in memo:
            return memo[key]
        
        if node == end:
            result = 1 if visited_required == required else 0
            memo[key] = result
            return result
        
        if node not in graph:
            memo[key] = 0
            return 0
        
        new_visited = visited_required | ({node} if node in required else set())
        total = sum(dfs(neighbor, new_visited) for neighbor in graph[node])
        memo[key] = total
        return total
    
    return dfs(start, set())

with open('day_11/input.txt', 'r') as f:
    lines = f.read().strip().split('\n')

graph = {}
for line in lines:
    device, outputs = line.split(':')
    graph[device.strip()] = outputs.strip().split()

print(count_paths_with_required(graph))