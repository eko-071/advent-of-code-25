with open("day_6/input_day_6.txt", 'r') as fp:
    input = fp.read().splitlines()[::-1]

equations = [item.split(" ") for item in input]
for item in equations:
    count = item.count("")
    for i in range(count):
        item.remove("")

operations = equations[0]
result = list(map(int, equations[1]))

for i in range(2, len(equations)):
    numbers = list(map(int, equations[i]))
    for j in range(len(numbers)):
        if operations[j] == '+':
            result[j] += numbers[j]
        elif operations[j] == '*':
            result[j] *= numbers[j]

print(sum(result))
