def open_file_as_list():
    f = open('day7.txt')
    lines = f.readlines()
    file_list = list(lines)
    return file_list

def calculate_fuel(value, target):
    steps = abs(value - target)
    fuel = 0
    while steps > 0:
        fuel += steps
        steps -= 1
    return fuel


#open file
f = open_file_as_list()

crab_list = list(map(int,f[0].split(',')))

min_value = min(crab_list)
max_value = max(crab_list)

lowest_value = None
for i in range(min_value,max_value):
    fuel = sum([calculate_fuel(crab,i) for crab in crab_list])
    if lowest_value == None:
        lowest_value = fuel
    if fuel < lowest_value:
        lowest_value = fuel
        #print(f'New Lowest: {fuel}[{i}]')

print(f'lowest: {lowest_value}')
