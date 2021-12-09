def open_file_as_list():
    f = open('day9.txt')
    lines = f.readlines()
    file_list = list(lines)
    return file_list


#open file
f = open_file_as_list()

grid = list(list(map(int, line.strip())) for line in f)

x_range = len(f[0])-1
y_range = len(f)
risk = 0

print(f'Xr {x_range} Yr {y_range}')

for y in range(y_range):
    for x in range(x_range):
        #if up is higher
        if y != 0:
            if grid[y-1][x] <= grid[y][x]:
                continue
        #if down is higher
        if y != y_range-1:
            if grid[y+1][x] <= grid[y][x]:
                continue
        #if left is higher
        if x != 0:
            if grid[y][x-1] <= grid[y][x]:
                continue
        #if right is higher
        if x != x_range-1:
            if grid[y][x+1] <= grid[y][x]:
                continue
        risk += (int(f[y][x]) +1)

print(risk)