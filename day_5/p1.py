with open("day_5/input.txt", 'r') as fp:
    input = fp.read().splitlines()

index = input.index("")
temp = input[:index]
ids = list(map(int, input[index+1:]))
ranges = list()

for elem in temp:
    ranges.append(list(map(int, elem.split("-"))))

count = 0

for item in ids:
    for span in ranges:
        low = span[0]
        high = span[1]
        if low <= item and item <= high:
            count += 1
            break
        
print(count)