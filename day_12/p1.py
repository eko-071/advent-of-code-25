with open("day_12/input.txt", 'r') as fp:
    text = fp.read().splitlines()

print(text)
results = 0
for line in text:
    if "x" in line:
        dimensions, grids = line.split(":")
        width,height = dimensions.split("x")
        area = int(width)//3 * int(height)//3

        total = sum(int(x) for x in grids.split())
        if total <= area:
            results += 1
print(results)