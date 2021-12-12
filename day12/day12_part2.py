class cave:
    def __init__(self, id) -> None:
        self.id = id
        self.islarge = id.isupper()
        self.connections = []
    
    def add_connection(self, cave):
        if cave not in self.connections:
            self.connections.append(cave)
    
    def get_connections(self):
        return self.connections
    

def open_file_as_list():
    f = open('day12.txt')
    lines = f.readlines()
    file_list = list(lines)
    return file_list

def reset_caves():
    for x in cave_dict.values():
        x.visited = False
    cave_dict['start'].visited = True

def find_end(curent_cave, history, count):
    if curent_cave not in history or cave_dict[curent_cave].islarge or wildcard_dict[curent_cave] == 1:
        if wildcard_dict[curent_cave] == 1 and curent_cave in history:
            wildcard_dict[curent_cave] = 0
        history.append(curent_cave)    
        for connection in cave_dict[curent_cave].get_connections():
            # print(f'{curent_cave} - {connection}')
            if connection == 'end':
                #print(f'Found end! {history}')
                solutions.append(''.join(history))
                count+=1
            else:
                count = find_end(connection, history, count)
        history.pop()
        if wildcard_dict[curent_cave] == 0:
            wildcard_dict[curent_cave] = 1
        return count
    else: 
        return count

f = open_file_as_list()

cave_dict = {}
wildcard_dict = {}
history = []
solutions = []
count = 0

#build map
for line in f:
    a, b = line.strip().split('-')

    #add to known caves
    if a not in cave_dict:
        cave_dict[a] = cave(a)
    if b not in cave_dict:
        cave_dict[b] = cave(b)
    
    #add connections
    cave_dict[a].add_connection(b)
    cave_dict[b].add_connection(a)

#setup wildcards
for x in cave_dict.keys():
    wildcard_dict[x] = -1

wildcardable_list = list(filter(lambda x: 'start' not in x and 'end' not in x and x.islower(), wildcard_dict.keys()))
#find routes
for wildcard in wildcardable_list:
    #clear previous
    for x in wildcard_dict.keys():
        wildcard_dict[x] = -1
    wildcard_dict[wildcard] = 1
    count = find_end('start', history, count)
print(len(set(solutions)))
