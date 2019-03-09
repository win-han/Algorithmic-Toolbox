# Uses python3
import sys
from itertools import chain


def sweep_line(starts, ends, points):
    cnt = [0] * len(points)
    zip_starts = zip(['a'] * len(starts), starts, range(len(starts)))
    zip_ends = zip(['x'] * len(ends), ends, range(len(ends)))
    zip_points = zip(['p'] * len(points), points, range(len(points)))
    line = chain(zip_starts, zip_ends, zip_points)
    line = sorted(line, key=lambda x: x[1])
    sweeper = 0
    for i in line:
        if i[0] == 'a':
            sweeper += 1
        elif i[0] == 'x':
            sweeper -= 1
        else:
            cnt[i[2]] += sweeper
    return cnt


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    cnt = sweep_line(starts, ends, points)
    for x in cnt:
        print(x, end=' ')