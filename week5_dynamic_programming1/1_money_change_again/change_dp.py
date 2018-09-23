# Uses python3
import sys
from operator import itemgetter


def get_change(m):
    sol = [1, 2, 1, 1]
    for i in range(5, m + 1):
        mini = sorted([(sol[-1],1), (sol[-3],3), (sol[-4],4)], key=itemgetter(0))
        sol.append(mini[0]+1)

    return sol[-1]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
