def open_file_as_list():
    f = open('day3.txt')
    lines = f.readlines()
    file_list = list(lines)
    return file_list

def most_common(lst):
    ones = lst.count('1')
    zeros = lst.count('0')
    if ones >= zeros :
        return '1'
    else:
        return '0'

def least_common(lst):
    ones = lst.count('1')
    zeros = lst.count('0')
    if zeros <= ones :
        return '0'
    else:
        return '1'

def binlist_to_decimal(lst):
    rv = 0
    for bit in lst:
        rv = (rv << 1) | int(bit)
    return rv

f = open_file_as_list()
bit_length = len(f[0].strip())
generator = f
generator_value = 0

scrubber = f
scrubber_value = 0

for i in range(bit_length):
    gen_mask = int(most_common([line.strip()[i] for line in generator]))
    generator = [ x.strip() for x in generator if int(x[i]) == gen_mask]
    if len(generator) == 1:
        generator_value = binlist_to_decimal(generator[0])

    scrub_mask = int(least_common([line.strip()[i] for line in scrubber]))
    scrubber = [ x.strip() for x in scrubber if int(x[i]) == scrub_mask]
    if len(scrubber) == 1:
        srubber_value = binlist_to_decimal(scrubber[0])

print(f'Generator: {generator_value} Scrubber: {srubber_value} Multiplied: {srubber_value*generator_value}')