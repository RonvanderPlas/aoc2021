class Card:
    def __init__(self, lst):
        self.data = []
        self.marked = [[0]*5 for i in range(5)]
        for entry in lst:
            self.data.append(entry.strip("\n").split())
    
    def find_number(self, number):
        for i, row in enumerate(self.data):
            for j, num in enumerate(row):
                if(int(num) == number):
                    self.marked[i][j] = 1
                    rv =  self.check_for_bingo(i,j)
                    if rv != 0:
                        return rv * number
        return 0
    
    def check_for_bingo(self, row, column):
        row_sum = 0
        column_sum = 0
        for i in range(5):
            row_sum += self.marked[i][column]
        
        for i in range(5):
            column_sum += self.marked[row][i]

        if row_sum == 5 or column_sum == 5:
            return (self.bingo())
        return 0

    def bingo(self):
        sum = 0
        for i, row in enumerate(self.data):
            for j, num in enumerate(row):
                if self.marked[i][j] == 0:
                    sum += int(self.data[i][j])
        return(sum)

def open_file_as_list():
    f = open('day4.txt')
    lines = f.readlines()
    file_list = list(lines)
    return file_list

#open file
f = open_file_as_list()

#get list of input numbers
input_numbers = f[0].strip().split(',')

#generate card objects
cards_list = []
for i, value in enumerate(f):
    if value == '\n':
        cards_list.append(Card(f[i+1:i+6]))

#Start the show
for number in input_numbers:
    stop = False
    for obj in cards_list:
        rv = obj.find_number(int(number))
        if rv != 0:
            stop = True
            print(rv)
            break
    if stop:
        break