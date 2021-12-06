def open_file_as_list():
    f = open('day6.txt')
    lines = f.readlines()
    file_list = list(lines)
    return file_list


#open file
f = open_file_as_list()

fishy_list = list(map(int,f[0].split(',')))
days = 80
for day in range(days):
    for i, fish in enumerate(fishy_list):
        if fish == 0:
            fishy_list.append(9)
            fishy_list[i] = 6
        else:
            fishy_list[i] = fish -1
    
    # print(f'Day[{day+1}] Fish: {len(fishy_list)} Lst:{fishy_list} ')


print(len(fishy_list))