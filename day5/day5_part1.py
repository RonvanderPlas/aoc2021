import re

def open_file_as_list():
    f = open('day5.txt')
    lines = f.readlines()
    file_list = list(lines)
    return file_list

def get_numbers(str):
    return re.findall(r'[0-9]+', str)

def get_increment(a,b):
    if a < b:
        return 1
    elif a == b:
        return 0
    else:
        return -1

#open file
f = open_file_as_list()

#find maximum x and y
max_x = max([int(get_numbers(line)[0]) for line in f]+[int(get_numbers(line)[2]) for line in f])
max_y = max([int(get_numbers(line)[1]) for line in f]+[int(get_numbers(line)[3]) for line in f])
# print(f'X:{max_x} Y:{max_y}')

#create canvas
canvas = [[0]*(max_x+1) for i in range((max_y+1))]

for line in f:
    x1, y1, x2, y2  = list(map(int,get_numbers(line)))

    x_range = x1-x2 - get_increment(x1,x2)
    y_range = y1-y2 - get_increment(y1,y2)
    # print('')
    if x_range == 0 or y_range == 0:
        for i in range(max(abs(x_range),abs(y_range))):
            new_x = x1 + (i*get_increment(x1,x2))
            new_y = y1 + (i*get_increment(y1,y2))

            canvas[new_x][new_y] += 1
            # print(f'newX: {new_x} newY: {new_y}')

#calculate total points
total_points = 0
for row in canvas:
    for column in row:
        if column >= 2:
            total_points += 1
    # print(row)
print(total_points)