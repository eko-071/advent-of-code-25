from ast import literal_eval
from z3 import *

with open("day_10/input.txt", 'r') as fp:
    input_data = fp.read().splitlines()

states = []
button_list = []
joltages = []

for line in input_data:
    parts = line.split(" ")
    
    item = []
    for i in range(1, len(parts[0])-1):
        if parts[0][i] == '.':
            item.append(0)
        else:
            item.append(1)
    states.append(item)
    
    parsed_buttons = []
    for btn in parts[1:len(parts)-1]:
        val = literal_eval(btn)
        if isinstance(val, int):
            parsed_buttons.append((val,))
        else:
            parsed_buttons.append(tuple(val))
    button_list.append(parsed_buttons)
    
    jolt_str = parts[-1][1:-1]
    joltages.append([int(x) for x in jolt_str.split(',')])

total = 0

for index in range(len(states)):
    target = joltages[index]
    buttons = button_list[index]
    
    opt = Optimize()
    presses = [Int(f'button_{i}') for i in range(len(buttons))]
    
    for p in presses:
        opt.add(p >= 0)
    
    for counter_idx in range(len(target)):
        counter_sum = 0
        for button_idx in range(len(buttons)):
            if counter_idx in buttons[button_idx]:
                counter_sum += presses[button_idx]
        opt.add(counter_sum == target[counter_idx])
    
    opt.minimize(Sum(presses))
    
    if opt.check() == sat:
        total += opt.model().eval(Sum(presses)).as_long()

print(total)