p = [3966, 5, 11, 21, 41, 209, 4513, 96, 1601, 1281, 6913, 1025, 1088]
s = 2
e = 8

for n in p:
    print(n)
    for i in range(1, 14):
        if n & (2**(i-1)) > 0:
            print(i, end=",  ")

    print()