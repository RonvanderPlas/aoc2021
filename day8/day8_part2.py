def open_file_as_list():
    f = open('day8.txt')
    lines = f.readlines()
    file_list = list(lines)
    return file_list


#open file
f = open_file_as_list()

counter = [0]*8
total_sum = 0
for line in f:
    digits = ['']*10
    scan_lst, data_lst = [x.split() for x in line.split('|')]

    #find 1, 4, 7 and 8
    for digit in scan_lst:
        if len(digit) == 2:
            digits[1] = digit
        elif len(digit) == 3:
            digits[7] = digit
        elif len(digit) == 4:
            digits[4] = digit
        elif len(digit) == 7:
            digits[8] = digit

    #analyze 5 and 6 len
    for digit in scan_lst:
        if len(digit) == 5:
            if all(s in digit for s in digits[1]):
                digits[3] = digit
            elif all(s in digit for s in digits[4].translate({ord(i): None for i in digits[1]})):
                digits[5] = digit
            else:
                digits[2] = digit
        elif len(digit) == 6:
            if all(s in digit for s in digits[4]):
                digits[9] = digit
            elif all(s in digit for s in digits[1]):
                digits[0] = digit
            else:
                digits[6] = digit
    
    #decode
    decoded_lst = []
    for digit in data_lst:
        for i in range(10):
            if len(digit) == len(digits[i]):
                if all(s in digit for s in digits[i]):
                    decoded_lst.append(i)

    total_sum += int(''.join(str(i) for i in decoded_lst))
    digits = ['']*10

print(total_sum)