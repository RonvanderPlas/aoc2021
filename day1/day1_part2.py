def open_file_as_list():
    f = open('day1.txt')
    lines = f.readlines()
    file_list = list(lines)
    return file_list


f = open_file_as_list()
prev_value = 0
total_increases = 0
total_lines = len(f)
for index, line in enumerate(f):
    if index < (total_lines-2):
        new_value = int(f[index]) + int(f[index+1]) + int(f[index+2])
        if new_value > prev_value and prev_value != 0:
            total_increases += 1
        prev_value = new_value
print(total_increases)
