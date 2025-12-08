with open("day_3/input.txt", 'r') as fp:
    input = fp.read().splitlines()

banks = list()
for item in input:
    banks.append([int(i) for i in item])

# banks = [[9,8,7,6,5,4,3,2,1,1,1,1,1,1,1], [8,1,1,1,1,1,1,1,1,1,1,1,1,1,9], [2,3,4,2,3,4,2,3,4,2,3,4,2,7,8], [8,1,8,1,8,1,9,1,1,1,1,2,1,1,1]]

joltage = 0

for bank in banks:
    result = []
    i = 0

    while len(result) < 12:
        ranges = len(bank) - 12 + len(result)
        maxi, index = -1, -1
        for j in range(i, ranges+1):
            if bank[j] > maxi:
                maxi = bank[j]
                index = j
        result.append(maxi)
        i = index+1
    
    total = 0
    for num in result:
        total = total*10 + num
    joltage += total

print(joltage)      