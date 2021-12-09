def open_file_as_list():
    f = open('day9.txt')
    lines = f.readlines()
    file_list = list(lines)
    return file_list


def get_adjacent_cells(x,y):
    rv_lst = []
    #cell up
    if y != 0:
        if grid[y-1][x] < 9 and checked_grid[y-1][x] == False:
            rv_lst.append([x,y-1])
    #cell down
    if y != y_range-1:
        if grid[y+1][x] < 9 and checked_grid[y+1][x] == False:
            rv_lst.append([x,y+1])
    #cell left
    if x != 0:
        if grid[y][x-1] < 9 and checked_grid[y][x-1] == False:
            rv_lst.append([x-1,y])
    #cell right
    if x != x_range-1:
        if grid[y][x+1] < 9 and checked_grid[y][x+1] == False:
            rv_lst.append([x+1,y])
    return rv_lst
    

#--check cell--
#Mark starting cell as checked 
#find adjacent not checked cells
#if no cells
#return value +1
#for each adjacent not checked cell  -> check cell
def check_cell(x,y,sum):
    if checked_grid[y][x] == True:
        return sum
    else:
        checked_grid[y][x] = True
        sum +=1
        adjacent = get_adjacent_cells(x,y)
        for cell in adjacent:
            sum = check_cell(cell[0],cell[1],sum)
        return sum

#open file
f = open_file_as_list()

grid = list(list(map(int, line.strip())) for line in f)

x_range = len(f[0])-1
y_range = len(f)

checked_grid = [[False]*x_range for i in range(y_range)]
lowest_points = []

print(f'Xr {x_range} Yr {y_range}')

#get all lowest points
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
        lowest_points.append([x,y])

basins = []
for point in lowest_points:
    basins.append(check_cell(point[0],point[1],0))

sbasins = sorted(basins, reverse=True)
print(sbasins[0]*sbasins[1]*sbasins[2])
