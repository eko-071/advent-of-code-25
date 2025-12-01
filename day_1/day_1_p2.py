input = list()

with open("day_1/input_day_1.txt", 'r') as fp:
    for line in fp:
        input.append(line.strip())

# input = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']
count = 0
state = 50

for item in input:
    direction = item[0]
    num = int(item[1:])
    count += num // 100
    num %= 100

    if direction == 'L':
        if state - num < 0 and state != 0:
            count += 1
        # print(f"{state} - {num} + 100 =", end = " ")
        state = (state - num + 100) % 100
        # print(state)
    else:
        if state + num > 100:
            count += 1
        # print(f"{state} + {num} =", end = " ")
        state = (state + num) % 100
        # print(state)

    if state == 0:
        count += 1

print(count)