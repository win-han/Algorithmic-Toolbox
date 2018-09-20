# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def bubblesort(bubble):

    counter = 1
    while counter != 0:
        counter = 0
        for i in range(len(bubble)-1):
            if bubble[i+1][1] < bubble[i][1]:
                bubble[i], bubble[i+1] = bubble[i+1], bubble[i]
                counter += 1
    return bubble


def optimal_points(segments):
    points = []
    for s in segments:
        points.append([s.start, s.end])
    bubblesort(points)
    a, ans = points[0][1], [points[0][1]]
    for i in range(len(points)):
        if points[i][0] > a:
            a = points[i][1]
            ans.append(a)
    return ans


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
