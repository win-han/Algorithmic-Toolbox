#Uses python3
import sys
import math
from operator import itemgetter


def closest_pair(x, y):
    if len(x) <= 3:
        return

    x1, x2 = x[:mid], x[mid:]
    y1, y2 = y[:mid], y[mid:]
    closest_pair(y1, y1)
    closest_pair(x2, y1)
    closest_split_pair(x, y)

    return 1


def closest_split_pair(x, y):
    pass



    return 1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    x_y = sorted(zip(x, y), key=itemgetter(0, 1))
    y_x = sorted(zip(x, y), key=itemgetter(1, 0))
    print("{0:.9f}".format(closest_pair(x_y, y_x)))
