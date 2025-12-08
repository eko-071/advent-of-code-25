with open("day_5/input.txt", 'r') as fp:
    input = fp.read().splitlines()

index = input.index("")
temp = input[:index]
ranges = list()

for elem in temp:
    ranges.append(list(map(int, elem.split("-"))))

ranges.sort(key=lambda x: x[0])

merged = [ranges[0]]
for i in range(1, len(ranges)):
    if merged[-1][1] >= ranges[i][0]:
        merged[-1] = (merged[-1][0], max(merged[-1][1], ranges[i][1]))
    else:
        merged.append(ranges[i])

count = 0

for span in merged:
    low = span[0]
    high = span[1]
    count += high - low + 1

print(count)

