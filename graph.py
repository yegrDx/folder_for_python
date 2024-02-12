matrix = []
def genBin(length, digits):
    if len(digits) == length:
        global matrix
        matrix.append(list(digits))
    else:
        for i in [1, 0]:
            digits.append(i)
            genBin(length, digits)
            digits.pop()
def permutations(length, digits, l):
    if len(digits) >= length:
        checkPath(digits, l)
    else:
        for i in range(length):
            if i not in digits:
                digits.append(i)
                permutations(length, digits, l)
                digits.pop()

def checkPath(vertex, listOfPaths):
    edges = [(0, 1), (0, 2), (0, 4), (1, 2), (1, 4), (2, 3), (3, 4)]
    probabilities = [0.2, 0.3, 0.2, 0.1, 0.4, 0.4, 0.3]
    #нужно искать пути от вершины 0 до 3
    prob = 1
    isPath = True
    for i in range(4):
        pair = (vertex[i], vertex[i + 1])
        revers_pair = (vertex[i + 1], vertex[i])
        if pair not in edges and revers_pair not in edges:
            isPath = False
            break
        if vertex[i] == 3 and i != 4:
            vertex = vertex[:i + 1]
            break
        elif pair in edges:
            prob *= probabilities[edges.index(pair)]
        elif revers_pair in edges:
            prob *= probabilities[edges.index(revers_pair)]

    if isPath and vertex[0] == 0:
        t = list(vertex)
        listOfPaths.append((t, prob))

listOfPaths = []
permutations(5, [], listOfPaths)
print(listOfPaths)
genBin(7, [])
