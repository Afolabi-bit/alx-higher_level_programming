#!/usr/bin/python3
def pow(a, b):
    ind = 1
    if b < 0:
        b = abs(b)
        for i in range(b):
            ind *= a
        return (1 / ind)
    elif b > 0:
        for i in range(b):
            ind *= a
        return ind
    else:
        return 1
