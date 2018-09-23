# Uses python3
import sys


def get_change(m):
    sol = [[1], [1, 1], [3], [4]]
    for i in range(5, m + 1):
        mini = sorted([sol[i-4], sol[i-3], sol[i-1]], key=len)

    return m // 4


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
