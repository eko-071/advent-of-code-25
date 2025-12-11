def calculate_area(x, y):
    breadth = abs(x[0]-y[0]) + 1
    length = abs(x[1]-y[1]) + 1
    return breadth*length

with open("day_9/input.txt", 'r') as fp:
    input = fp.read().splitlines()

coordinates = [list(map(int, line.split(","))) for line in input]

max = -1
for i in range(len(coordinates)):
    for j in range(i+1, len(coordinates)):
        area = calculate_area(coordinates[i], coordinates[j])
        if area>max:
            max = area

print(max)