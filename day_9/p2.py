from collections import deque
from bisect import bisect_left, bisect_right


with open("day_9/input.txt", 'r') as fp:
    input = fp.read().splitlines()

tiles = [tuple(map(int, line.split(','))) for line in input]
L = len(tiles)

xs = sorted({x + dx for x, _ in tiles for dx in (-1, 0, 1)}) 
ys = sorted({y + dy for _, y in tiles for dy in (-1, 0, 1)})

x_ind = {x: i for i, x in enumerate(xs)}
y_ind = {y: i for i, y in enumerate(ys)}

W = len(xs) - 1
H = len(ys) - 1

wx = [xs[i + 1] - xs[i] for i in range(W)]
wy = [ys[j + 1] - ys[j] for j in range(H)]

wall = [[False] * W for _ in range(H)]

for k in range(L):
    x1, y1 = tiles[k]
    x2, y2 = tiles[(k + 1) % L]

    if x1 == x2:
        cx = x_ind[x1]
        if y1 > y2:
            y1, y2 = y2, y1
        j_start = y_ind[y1]
        j_end = y_ind[y2]
        for j in range(j_start, j_end):
            if cx > 0:
                wall[j][cx - 1] = True
            if cx < W:
                wall[j][cx] = True
    elif y1 == y2:
        cy = y_ind[y1]
        if x1 > x2:
            x1, x2 = x2, x1
        i_start = x_ind[x1]
        i_end = x_ind[x2]
        for i in range(i_start, i_end):
            if cy > 0:
                wall[cy - 1][i] = True
            if cy < H:
                wall[cy][i] = True
    else:
        raise Exception("Input segment is non axis-aligned")
    
outside = [[False] * W for _ in range(H)]
q = deque()
for j in range(H):
    for i in (0, W - 1):
        if not wall[j][i] and not outside[j][i]:
            outside[j][i] = True
            q.append((i, j))

for i in range(W):
    for j in (0, H - 1):
        if not wall[j][i] and not outside[j][i]:
            outside[j][i] = True
            q.append((i, j))

DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
while q:
    x, y = q.popleft()
    for dx, dy in DIRS:
        nx, ny = x + dx, y + dy
        if 0 <= nx < W and 0 <= ny < H:
            if not wall[ny][nx] and not outside[ny][nx]:
                outside[ny][nx] = True
                q.append((nx, ny))

floorspace = [[0] * W for _ in range(H)]

for j in range(H):
    for i in range(W):
        if wall[j][i]:
            floorspace[j][i] = wx[i] * wy[j]
        elif not outside[j][i]:
            floorspace[j][i] = wx[i] * wy[j]

prefix_sum = [[0] * (W + 1) for _ in range(H + 1)]
for j in range(H):
    for i in range(W):
        prefix_sum[j + 1][i + 1] = (
            floorspace[j][i]
            + prefix_sum[j][i + 1]
            + prefix_sum[j + 1][i]
            - prefix_sum[j][i]
        )

def rs(x1, y1, x2, y2):
    return prefix_sum[y2][x2] - prefix_sum[y1][x2] - prefix_sum[y2][x1] + prefix_sum[y1][x1]

best_area = 0

for i in range(L):
    x1, y1 = tiles[i]
    for j in range(i + 1, L):
        x2, y2 = tiles[j]
        area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        if area <= best_area:
            continue
        xmin = min(x1, x2)
        xmax = max(x1, x2)
        ymin = min(y1, y2)
        ymax = max(y1, y2)

        cx1 = bisect_right(xs, xmin) - 1
        cx2 = bisect_left(xs,  xmax + 1)
        cy1 = bisect_right(ys, ymin) - 1
        cy2 = bisect_left(ys,  ymax + 1)

        total_floorspace = rs(cx1, cy1, cx2, cy2)

        if total_floorspace == area:
            best_area = area

print(best_area)