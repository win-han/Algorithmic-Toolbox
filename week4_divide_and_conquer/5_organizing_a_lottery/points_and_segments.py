# Uses python3
import sys
import math


def MergeSort(a):
    if len(a) == 1:
        return [a[0]]
    mid = len(a) // 2
    m1 = MergeSort(a[:mid])
    m2 = MergeSort(a[mid:])
    k = merge(m1, m2)
    return k


def merge(a, b):
    c = []
    while a and b:
        if a[0][0] <= b[0][0]:
            c.append(a[0])
            a.pop(0)
        else:
            c.append(b[0])
            b.pop(0)
    c = c + a + b
    return c


def binary_search(arr, low, high, key):
    if high < low:
        return high
    mid = low + (high - low) // 2
    if key == arr[mid][0]:
        return mid
    elif key < arr[mid][0]:
        return binary_search(arr, low, mid - 1, key)
    elif key > arr[mid][0]:
        return binary_search(arr, mid + 1, high, key)


def fast_count_segments(starts, ends, points):

    cnt = [0] * len(points)

    for start, end in zip(starts, ends):


        while a < len(points):

            if start <= points[a][0] <= end:
                cnt[points[a][1]] += 1
                a += 1
            else:
                break
    return cnt


def faster_count_segments(starts, ends, points):
    maxi, mini = -1 * math.inf, math.inf
    for i, j in zip(starts, ends):
        if i < mini:
            mini = i
        if j > maxi:
            maxi = j
    length = abs(maxi - mini + 1)
    cnt = [0] * length
    count = [0] * len(points)

    for start, end in zip(starts, ends):
        for i in range(abs(end - start + 1)):
            cnt[start - mini] += 1
            start += 1

    for i in range(len(points)):
        try:
            count[i] += cnt[points[i] - mini]
        except IndexError:
            pass

    return count


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


def fastest_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    start_points = zip(starts, ['s'] * len(starts), range(len(starts)))
    end_points = zip(ends, ['e'] * len(ends), range(len(ends)))
    point_points = zip(points, ['.'] * len(points), range(len(points)))

    sort_list = it.chain(start_points, end_points, point_points)
    sort_list = sorted(sort_list, key = lambda a: (a[0], a[1]))
    segment = 0
    i = 0
    for num, letter, index in sort_list:
        if letter == 's':
            segment += 1
        elif letter == 'e':
            segment -= 1
        else:
            cnt[index] = segment
            i += 1
    return cnt


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fastest_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
