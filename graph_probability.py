def permutations(length, digits):
    if len(digits) == length:
        checkPath(digits)
    else:
        for i in range(length):
            if i not in digits:
                digits.append(i)
                permutations(length, digits)
                digits.pop()

def checkPath(vertex):
    edges = [(0, 1), (0, 2), (0, 4), (1, 2), (1, 4), (2, 3), (3, 4)]
    #нужно искать пути от вершины 0 до 3
    isPath = True
    for i in range(4):
        pair = (vertex[i], vertex[i + 1])
        revers_pair = (vertex[i + 1], vertex[i])
        if pair not in edges and revers_pair not in edges:
            isPath = False
            break
        if vertex[i] == 3:
            vertex = vertex[:i + 1]
            break

    if isPath and vertex[0] == 0:
        print(vertex)

edges = [(0, 1), (0, 2), (0, 4), (1, 2), (1, 4), (2, 3), (3, 4)]

permutations(5,[])