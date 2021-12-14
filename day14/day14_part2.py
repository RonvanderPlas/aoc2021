import itertools

def open_file_as_list():
    f = open('day14.txt')
    lines = f.readlines()
    file_list = list(lines)
    return file_list

def get_combo_lst(start_lst):
    rv = []
    for i, v in enumerate(start_lst[:-1]):
        rv.append(''.join(start_lst[i:i+2]))
    return(rv)

def add_to_counter(dict, char, amount):
    if char not in dict:
        dict.update({char:amount})
    else:
        dict[char] += amount

steps = 40

f = open_file_as_list()

polymer = f[0].strip()
instructions = dict([x.strip().split(' -> ') for x in f[2:]])
combo_count = dict.fromkeys(instructions.keys(),0)
individual_count = {}

#fill initial combo counter
for combo in get_combo_lst(polymer):
    combo_count[combo] += 1

#fill initial indidivual counter
for char in polymer:
    add_to_counter(individual_count,char,1)

for step in range(steps):
    new_combo_count = combo_count.copy()
    for combo, amount in combo_count.items():
        new_combo_count[combo] -= amount
        new_combo_count[combo[0] + instructions[combo]] += amount
        new_combo_count[instructions[combo] + combo[1]] += amount
        add_to_counter(individual_count,instructions[combo], amount)
    combo_count = new_combo_count.copy()
    

#create individual counter
print(combo_count)
print(individual_count)
max_count = max(individual_count.values())
min_count = min(individual_count.values())
print(f'Max: {max_count} Min: {min_count} Delta: {max_count - min_count}')


