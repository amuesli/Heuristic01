p = [0, 7932, 10, 22, 42, 82, 418, 9026, 192, 3202, 2562, 13826, 2050, 2176]
d = [[0, 75, 60, 95, 122, 128, 121, 182, 68, 49, 112, 60, 160],
     [75, 0, 14, 73, 126, 158, 192, 224, 150, 146, 207, 143, 255],
     [60, 14, 0, 39, 88, 121, 156, 197, 122, 128, 196, 139, 231],
     [95, 73, 39, 0, 22, 71, 134, 153, 117, 141, 221, 180, 230],
     [122, 126, 88, 22, 0, 24, 102, 104, 107, 143, 228, 192, 211],
     [128, 158, 121, 71, 24, 0, 60, 56, 71, 126, 207, 196, 173],
     [121, 192, 156, 134, 102, 60, 0, 49, 32, 78, 146, 158, 90],
     [182, 224, 197, 153, 104, 56, 49, 0, 104, 151, 219, 230, 146],
     [68, 150, 122, 117, 107, 71, 32, 104, 0, 24, 104, 102, 88],
     [49, 146, 128, 141, 143, 126, 78, 151, 24, 0, 60, 56, 88],
     [112, 207, 196, 221, 228, 207, 146, 219, 104, 60, 0, 49, 85],
     [60, 143, 139, 180, 192, 196, 158, 230, 102, 56, 49, 0, 143],
     [160, 255, 231, 230, 211, 173, 90, 146, 88, 88, 85, 143, 0]]  # distance matrix
st = 2  # Start Node
ed = 8  # End node
m = 0  # Open/Closed node mask


def takeSecond(elem):
    return elem[1]


def heu_closest(n, e):
    t = []
    print('Available paths: ', end=" ")
    for i in range(1, p.__len__()):
        if n & (2 ** i) > 0:
            print(i, end=', ')
            t.append([i, d[i - 1][e - 1]])
    t.sort(key=takeSecond)
    print()
    print('In order of distance to node ' + str(e) + ':')
    print(t)
    print()
    return [row[0] for row in t]


def search(n, e):
    print('We are at Node: ' + str(n))
    global m
    m += (2 ** n)  # Add node to closed mask
    if p[n] & (2 ** e) == (2 ** e):
        print(e, end=" ← ")
        return True
    for i in heu_closest(p[n] & ~m, e):
        if search(i, e):
            print(i, end=" ← ")
            return True
    return False


if search(st, ed):
    print(st)
