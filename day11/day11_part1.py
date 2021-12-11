def open_file_as_list():
    f = open('day11.txt')
    lines = f.readlines()
    file_list = list(lines)
    return file_list

def get_flashable_cell(grid):
    x_range = len(grid[0])
    y_range = len(grid)

    for y in range(y_range):
        for x in range(x_range):
            if grid[y][x] > 9:
                return x, y
    return None


def flash_cell(grid, x, y):
    x_limit = len(grid[0])-1
    y_limit = len(grid)-1

    grid[y][x] = -1
    #l up
    if x != 0 and y != 0:
        if grid[y-1][x-1] != -1:
            grid[y-1][x-1] += 1
    #m up
    if y != 0:
        if grid[y-1][x] != -1:
            grid[y-1][x] += 1
    #r up
    if x != x_limit and y != 0:
        if grid[y-1][x+1] != -1:
            grid[y-1][x+1] += 1
    #l
    if x != 0:
        if grid[y][x-1] != -1:
            grid[y][x-1] += 1
    #r
    if x != x_limit:
        if grid[y][x+1] != -1:
            grid[y][x+1] += 1
    #l down
    if x != 0 and y != y_limit:
        if grid[y+1][x-1] != -1:
            grid[y+1][x-1] += 1
    #m down
    if y != y_limit:
        if grid[y+1][x] != -1:
            grid[y+1][x] += 1
    #r down
    if x != x_limit and y != y_limit:
        if grid[y+1][x+1] != -1:
            grid[y+1][x+1] += 1

def reset_cells(grid):
    x_range = len(grid[0])
    y_range = len(grid)

    for y in range(y_range):
        for x in range(x_range):
            if grid[y][x] == -1:
                grid[y][x] = 0

steps = 100
flashes = 0

f = open_file_as_list()

grid = list(list(map(int, line.strip())) for line in f)

for step in range(steps):
    #grid +1
    grid = list(map(lambda row: list(map(lambda x: x+1, row)),grid))

    flasher = get_flashable_cell(grid)

    while flasher != None:
        flash_cell(grid, flasher[0],flasher[1])
        flashes+=1
        flasher = get_flashable_cell(grid)
        
    reset_cells(grid)
    

print(flashes)
