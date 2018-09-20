# Uses python3
import sys


def get_majority_element(arr, left, right):
    curr, counter = arr[0], 0
    for i in arr[1:]:
        if i == curr:
            counter += 1
        elif i != curr and counter != 0:
            counter -= 1
        elif i != curr and counter == 0:
            curr = i
            counter += 1
    counter = 0
    for i in arr:
        if i == curr:
            counter += 1

    if counter > len(arr) // 2:
        return 1
    else:
        return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(get_majority_element(a, 0, n))
