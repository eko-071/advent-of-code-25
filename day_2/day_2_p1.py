with open("day_2/input_day_2.txt", 'r') as fp:
    input = fp.readline().split(",")

ranges = list()
for item in input:
    ranges.append(list(map(int, item.split("-"))))

# ranges = [[11, 22], [95,115], [998,1012], [1188511880,1188511890], [222220,222224], [1698522,1698528], [446443,446449], [38593856,38593862]]

count = 0

for item in ranges:
    low = item[0]
    high = item[1]
    for i in range(low, high+1):
        num = str(i)
        if len(num)%2 == 1:
            continue
        part1 = num[:len(num)//2]
        part2 = num[len(num)//2:]
        if part1 == part2:
            count += i

print(count)