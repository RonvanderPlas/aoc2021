def open_file_as_list():
    f = open('day13.txt')
    lines = f.readlines()
    file_list = list(lines)
    return file_list


f = open_file_as_list()

points = [x.strip() for x in list(filter(lambda x: ',' in x, f))]
folds = [x.strip() for x in list(filter(lambda x: 'fold' in x, f))]

x_max = max([int(x.split(',')[0]) for x in points])+ 1 
y_max = max([int(x.split(',')[1]) for x in points])+ 1 

#make sure it's uneven
x_max += (1-x_max%2)
y_max += (1-y_max%2)

#make grid
grid = [['.']*x_max for i in range(y_max)]

#fill grid
for point in points:
    x,y = map(int, point.split(','))
    grid[y][x] = '#'

#start folding
# for fold in folds:
fold = folds[0]
#get values
count = int(fold.split('=')[1])
x_grid = len(grid[0])
y_grid = len(grid)

#cycle through ranges (count to 0) and (count to end)
list1 = list(range(count-1,-1,-1))
list2 = list(range(count+1,(count*2)+1))
for i, j in zip(list1,list2):
    if 'x' in fold:
        for y in range(y_grid):
            # print(f'i:{i} j:{j} y:{y}')
            grid[y][i] = '#' if grid[y][i] == '#' or grid[y][j] == '#' else '.'
    if 'y' in fold:
        for x in range(x_grid):
            grid[i][x] = '#' if grid[i][x] == '#' or grid[j][x] == '#' else '.'

#shrink grid
if 'x' in fold:
    for v in grid[:]:
        del v[count:]
if 'y' in fold:
    del grid[count:]

count = 0
#print grid
for row in grid:
    for char in row:
        if char == '#':
            count+=1
    # print(''.join(row))
print(count)