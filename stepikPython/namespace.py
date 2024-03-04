n = int(input())
spaces = {'global':{'parent': None, 'vars': []}}

def create(namesp, parent):
    global spaces
    spaces[namesp] = {'parent': None, 'vars': []}
    spaces[namesp]['parent'] = parent

def add(namesp, var):
    global spaces
    spaces[namesp]['vars'].append(var)

def get(namesp, var):
    if namesp == None or var in spaces[namesp]['vars']:
        print(namesp)
    else:
        get(spaces[namesp]['parent'], var)

for i in range(n):
    cmd, arg1, arg2 = input().split()
    if cmd == 'get':
        get(arg1, arg2)
    elif cmd == 'add':
        add(arg1, arg2)
    elif cmd == 'create':
        create(arg1, arg2)

