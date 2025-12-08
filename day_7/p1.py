with open("day_7/input.txt", 'r') as fp:
    input = fp.read().splitlines()

grid = list()
for line in input:
    grid.append(list(line))

rows = len(grid)
cols = len(grid[0])

start = grid[0].index("S")
grid[1][start] = "|"

count = 0

for i in range(1, rows-1):
    for j in range(cols):
        if grid[i][j] != '|':
            continue
        if grid[i+1][j] != '^':
            grid[i+1][j] = '|'
            continue
        count += 1
        if j == 0:
            grid[i+1][j+1] = '|'
        elif j == cols-1:
            grid[i+1][j-1] = '|'
        else:
            grid[i+1][j+1] = '|'
            grid[i+1][j-1] = '|'

# for i in range(rows):
#     for j in range(cols):
#         print(grid[i][j], end = "")
#     print()

print(count)