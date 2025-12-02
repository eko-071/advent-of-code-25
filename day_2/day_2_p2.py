with open("day_2/input_day_2.txt", 'r') as fp:
    input = fp.readline().split(",")

ranges = list()
for item in input:
    ranges.append(list(map(int, item.split("-"))))

# ranges = [[11, 22], [95,115], [998,1012], [1188511880,1188511890], [222220,222224], [1698522,1698528], [446443,446449], [38593856,38593862], [565653,565659], [824824821,824824827], [2121212118,2121212124]]

count = 0

for item in ranges:
    low = item[0]
    high = item[1]
    for i in range(low, high+1, 1):
        num = str(i)
        if len(num) == 1:
            continue
        for j in range(1, len(num)//2 + 1):
            if len(num)%j != 0:
                continue
            parts = [num[k:k+j] for k in range(0, len(num), j)]
            # print(parts)
            if len(set(parts)) == 1:
                count += i
                # print(count)
                break

print(count)