# Uses python3
import sys
from operator import itemgetter


def get_change(m):
    solution = [1, 2, 1, 1]
    if m < 5:
        return solution[m-1]

    for i in range(5, m + 1):
        mini = sorted([(solution[-1],1), (solution[-3],3), (solution[-4],4)], key=itemgetter(0))
        solution.append(mini[0][0]+1)
        solution = solution[-4:]

    return solution[-1]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
