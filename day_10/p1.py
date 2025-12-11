from ast import literal_eval
from itertools import combinations

with open("day_10/input.txt", 'r') as fp:
    input = fp.read().splitlines()

states = []
button_list = []
joltages = []

for line in input:
    parts = line.split(" ")
    item = []
    for i in range(1, len(parts[0])-1):
        if parts[0][i] == '.':
            item.append(0)
        else:
            item.append(1)
    states.append(item)
    
    parsed_buttons = [literal_eval(item) for item in parts[1:len(parts)-1]]    
    button_list.append(parsed_buttons)
    joltages.append(list(literal_eval(parts[-1])))

total = 0
for index in range(len(states)):
    target = states[index]
    button = button_list[index]
    num_lights = len(target)
    num_buttons = len(button)
    min_presses = 999999
    
    for presses in range(num_buttons+1):
        found = False
        for button_combo in combinations(range(num_buttons), presses):
            current = [0]*num_lights
            for i in button_combo:
                # Convert to tuple if it's a single integer
                button_toggles = button[i] if isinstance(button[i], (list, tuple)) else (button[i],)
                for j in button_toggles:
                    if j < num_lights:
                        current[j] ^= 1
            if current == target:
                min_presses = presses
                found = True
                break
        if found:
            break
    
    total += min_presses

print(total)