def open_file_as_list():
    f = open('day3.txt')
    lines = f.readlines()
    file_list = list(lines)
    return file_list

def most_common(lst) -> int:
    return max(set(lst), key=lst.count)

def binlist_to_decimal(lst):
    rv = 0
    for bit in lst:
        rv = (rv << 1) | int(bit)
    return rv

f = open_file_as_list()
bit_length = len(f[0].strip())
gamma_lst = []
gamma = 0
epsilon = 0

for i in range(bit_length):
    gamma_lst.append(most_common([line.strip()[i] for line in f]))

gamma = binlist_to_decimal(gamma_lst)
epsilon = gamma ^ ((2**bit_length) - 1)

print(f'Gamma: {gamma} Epsilson {epsilon} Multiplied: {gamma * epsilon}')
    
