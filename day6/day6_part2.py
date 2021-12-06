from functools import lru_cache
import math
import time
start_time = time.time()

def open_file_as_list():
    f = open('day6.txt')
    lines = f.readlines()
    file_list = list(lines)
    return file_list

@lru_cache(maxsize=None)
def calculate_fish(days, age):
    grand_children = 0
    if age > days:
        return 0
    else:
        children = math.floor((days-age)/7)+1
        
        for i in range(0, children):
            new_days = days-age-(i*7)
            grand_children += calculate_fish(new_days, 9)
        return grand_children + children

#open file
f = open_file_as_list()

fishy_list = list(map(int,f[0].split(',')))
days = 255

total_fish = len(fishy_list)

for i in range(len(fishy_list)):
    total_fish += calculate_fish(days, fishy_list[i])

print(total_fish)
print("--- %s seconds ---" % (time.time() - start_time))
