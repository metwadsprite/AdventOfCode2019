fuel_sum = 0
for line in open("input.txt"):
    fuel = (int(line) // 3) - 2
    while fuel >= 1:
        fuel_sum += fuel
        fuel = (fuel // 3) - 2

print(fuel_sum)