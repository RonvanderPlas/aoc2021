import math

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

points2 = {
    ')' : 1,
    ']' : 2,
    '}' : 3,
    '>' : 4
}

#open file
f = open_file_as_list()
score = 0
score_lst = []

for line in f:
    stack = ['']*len(line)
    stackpointer = 0
    corrupted = False
    linescore = 0
    for char in line:
        if char in openings:
            stack[stackpointer] = char
            stackpointer+=1
        elif char in closings:
            stackpointer -=1
            if stack[stackpointer] == openings[closings.index(char)]:
                stack[stackpointer] = ''
            else:
                corrupted = True
                score += points[char]
                print(f'Expected {closings[openings.index(stack[stackpointer])]}, but found found {char} instead')
    if stackpointer != 0 and corrupted == False:
        while stackpointer != 0:
            stackpointer -=1
            linescore *= 5
            linescore += points2[closings[openings.index(stack[stackpointer])]]
            stack[stackpointer] = ''
        score_lst.append(linescore)
print(score)
print(sorted(score_lst)[math.floor(len(score_lst)/2)])