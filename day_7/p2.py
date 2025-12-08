with open("day_7/input.txt", 'r') as fp:
    input = fp.read().splitlines()

grid = list()
for line in input:
    grid.append(list(line))

rows = len(grid)
cols = len(grid[0])

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == '.':
            grid[i][j] = 0


start = grid[0].index("S")
grid[1][start] = 1

count = 0

for i in range(1, rows-1):
    for j in range(cols):
        if type(grid[i][j]) != type(1):
            continue
        if grid[i+1][j] != '^':
            grid[i+1][j] += grid[i][j]
            continue
        count += 1
        if j == 0:
            grid[i+1][j+1] += grid[i][j]
        elif j == cols-1:
            grid[i+1][j-1] += grid[i][j]
        else:
            grid[i+1][j+1] += grid[i][j]
            grid[i+1][j-1] += grid[i][j]

# for i in range(rows):
#     for j in range(cols):
#         print(grid[i][j], end = "")
#     print()

# print(count)
print(sum(grid[rows-1]))