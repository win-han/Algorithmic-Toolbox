# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    stops += [distance, distance]
    fuel, count = tank, 0
    for i in range(len(stops)-1):
        if fuel < stops[i]:
            return -1
        if fuel < stops[i+1]:
            fuel += tank - fuel + stops[i]
            count += 1
    return count


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
