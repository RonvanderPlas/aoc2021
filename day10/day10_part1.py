def open_file_as_list():
    f = open('day10.txt')
    lines = f.readlines()
    file_list = list(lines)
    return file_list


openings = ['(', '[', '{', '<']
closings = [')', ']', '}', '>']

points = {
    ')' : 3,
    ']' : 57,
    '}' : 1197,
    '>' : 25137
}

#open file
f = open_file_as_list()
score = 0
for line in f:
    stack = ['']*len(line)
    stackpointer = 0
    for char in line:
        if char in openings:
            stack[stackpointer] = char
            stackpointer+=1
        elif char in closings:
            stackpointer -=1
            if stack[stackpointer] == openings[closings.index(char)]:
                stack[stackpointer] = ''
            else:
                score += points[char]
                print(f'Expected {closings[openings.index(stack[stackpointer])]}, but found found {char} instead')

print(score)