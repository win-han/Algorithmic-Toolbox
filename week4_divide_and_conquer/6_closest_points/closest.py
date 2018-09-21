#Uses python3
import sys
import math
from operator import itemgetter


def closest_pair(x_sorted, y_sorted):
    if len(x_sorted) <= 3:
        return less_than_3(x_sorted)

    mid = len(x_sorted) // 2

    x_left, x_right = x_sorted[:mid], x_sorted[mid:]
    y_left, y_right = y_sorted[:mid], y_sorted[mid:]
    a1 = closest_pair(x_left, y_left)
    a2 = closest_pair(x_right, y_right)
    a3 = closest_split_pair(x_sorted, y_sorted)
    return min(a1, a2, a3)


def less_than_3(x):
    pass


def closest_split_pair(x_sorted, y_sorted):

    return -1


def dist_(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    x_y = sorted(zip(x, y), key=itemgetter(0, 1))
    y_x = sorted(zip(x, y), key=itemgetter(1, 0))
    print("{0:.9f}".format(closest_pair(x_y, y_x)))
