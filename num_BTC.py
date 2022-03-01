import math


def num_BTC(b):
    n = 0
    bar = 210000
    reward = 50
    halves = int(b/bar)
    c = float(0)

    while n < halves:
        factor = pow(0.5, n)
        c += bar * reward * factor
        b -= bar
        n += 1

    c += b * reward * pow(0.5, halves)

    return c

#print(num_BTC(1))
#print(num_BTC(210000))