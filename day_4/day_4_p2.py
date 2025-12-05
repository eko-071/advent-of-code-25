with open("day_4/input_day_4.txt", 'r') as fp:
    grid = [list(line) for line in fp.read().splitlines()]

rows = len(grid)
cols = len(grid[0])
count = 0

directions = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1)
]

positions = list()

for k in range(rows):
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '.':
                continue
            
            condition = 0
            
            for x, y in directions:
                ni, nj = i + x, j + y
                if 0 <= ni < rows and 0 <= nj < cols:
                    if grid[ni][nj] == '@':
                        condition += 1
            
            if condition < 4:
                grid[i][j] = '.'
                count += 1

print(count)
