def open_file_as_list():
    f = open('day2.txt')
    lines = f.readlines()
    file_list = list(lines)
    return file_list


f = open_file_as_list()
distance = 0
depth = 0
for line in f:
    command, amount = line.split(' ')
    if 'forward' in command:
        distance += int(amount)
    if 'up' in command:
        depth -= int(amount)
    if 'down' in command:
        depth += int(amount)

print(f"Distance:{distance} Depth:{depth} X:{distance*depth}")