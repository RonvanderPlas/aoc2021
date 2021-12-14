import itertools

def open_file_as_list():
    f = open('day14.txt')
    lines = f.readlines()
    file_list = list(lines)
    return file_list

def get_combo_lst(start_lst):
    rv = []
    for i, v in enumerate(start_lst[:-1]):
        rv.append(instructions[''.join(start_lst[i:i+2])])
    return(rv)

steps = 10

f = open_file_as_list()

polymer = f[0].strip()
print(polymer)
instructions = dict([x.strip().split(' -> ') for x in f[2:]])

for step in range(steps):
    print(step)
    combo_lst = get_combo_lst(polymer)
    polymer = list(itertools.chain.from_iterable(itertools.zip_longest(polymer,combo_lst)))[:-1]

most_common = polymer.count(max(set(polymer), key = polymer.count))
least_common =  polymer.count(min(set(polymer), key = polymer.count))
print(f'[{len(polymer)}] Result: {most_common - least_common}')

