with open("day_6/input_day_6.txt", 'r') as fp:
    input = fp.read()

lines = input.splitlines()
width = max(len(line) for line in lines)
rows = [line.ljust(width) for line in lines]
H = len(rows)

sep = [all(rows[r][c] == ' ' for r in range(H)) for c in range(width)]

blocks = []
c = 0
while c < width:
    if sep[c]:
        c += 1
        continue
    start = c
    while c < width and not sep[c]:
        c += 1
    blocks.append((start, c - 1))

total = 0

for (start, end) in blocks:
    op = rows[-1][start:end+1].strip()

    numbers = []

    for col in range(start, end+1):
        digits = []
        for row in range(H - 1):
            ch = rows[row][col]
            if ch.isdigit():
                digits.append(ch)

        if digits:
            numbers.append(int("".join(digits)))

    if op == "+":
        value = sum(numbers)
    else:
        value = 1
        for x in numbers:
            value *= x

    total += value

print(total)