def open_file_as_list():
    f = open('day8.txt')
    lines = f.readlines()
    file_list = list(lines)
    return file_list


#open file
f = open_file_as_list()

counter = 0
for line in f:
    scan_lst, data_lst = [x.split() for x in line.split('|')]
    for digit in data_lst:
        if len(digit) == 2 or len(digit) == 3 or len(digit) == 4 or len(digit) == 7:
            counter += 1

print(counter)