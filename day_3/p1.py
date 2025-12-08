with open("day_3/input.txt", 'r') as fp:
    input = fp.read().splitlines()

banks = list()
for item in input:
    banks.append([int(i) for i in item])

# banks = [[9,8,7,6,5,4,3,2,1,1,1,1,1,1,1], [8,1,1,1,1,1,1,1,1,1,1,1,1,1,9], [2,3,4,2,3,4,2,3,4,2,3,4,2,7,8], [8,1,8,1,8,1,9,1,1,1,1,2,1,1,1]]

joltage = 0

for bank in banks:
    max = -1
    for i in range(len(bank)):
        for j in range(i+1, len(bank)):
            if bank[i]*10 + bank[j] > max:
                max = bank[i]*10 + bank[j]
    joltage += max

print(joltage)            
