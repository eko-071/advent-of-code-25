input = list()

with open("day_1/input_day_1.txt", 'r') as fp:
    for line in fp:
        input.append(line.strip())

count = 0
state = 50

for item in input:
    direction = item[0]
    num = int(item[1:])
    if direction == 'L':
        state = (state + 100 - num%100) % 100
    else:
        state = (state + num) % 100
    if state == 0:
        count += 1

print(count)