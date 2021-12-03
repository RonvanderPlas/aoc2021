def open_file_as_list():
    f = open('temp.txt')
    lines = f.readlines()
    file_list = list(lines)
    return file_list

def most_common(lst):
    ones = lst.count('1')
    zeros = lst.count('1')
    if ones >= zeros :
        return '1'
    else:
        return '0'

def least_common(lst):
    ones = lst.count('1')
    zeros = lst.count('1')
    if zeros >= ones :
        return '0'
    else:
        return '1'

def binlist_to_decimal(lst):
    rv = 0
    for bit in lst:
        rv = (rv << 1) | int(bit)
    return rv

def get_generator(lst, bit, mask):
    return [ x for x in lst if lst[bit] == mask ]

f = open_file_as_list()
bit_length = len(f[0].strip())
generator = f
scrubber = f 

print(int(most_common([line.strip()[0] for line in f]))^1)
print(least_common([line.strip()[0] for line in f]))
for i in range(bit_length):
    gen_mask = int(most_common([line.strip()[i] for line in f]))^1
    print([ x for x in generator if generator[i] == gen_mask ])

# gamma = binlist_to_decimal(gamma_lst)
# epsilon = gamma ^ ((2**bit_length) - 1)

print(f'Gamma: {gamma} Epsilson {epsilon} Multiplied: {gamma * epsilon}')
    
