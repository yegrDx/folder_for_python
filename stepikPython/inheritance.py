from collections import deque

classes = {}

def addClass(classes, name, parents):
    if name not in classes:
        classes[name] = []
    for p in parents:
        if p not in classes:
            classes[p] = []
        classes[name].append(p)


def check(graph, start, target):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node == target:
            return True
        if node not in visited:
            visited.add(node)
            queue.extend(graph[node])
    return False

def answer(classes, parent, child):
    if not(parent or child) in classes or not check(classes, child, parent):
        return 'No'
    return 'Yes'

n = int(input())
for _ in range(n):
    classAndParents = input().split()
    name = classAndParents[0]
    parents = classAndParents[2:]
    addClass(classes, name, parents)

q = int(input())
for _ in range(q):
    parentAndName = input().split()
    name = parentAndName[1]
    parent = parentAndName[0]
    print(answer(classes, parent, name))

