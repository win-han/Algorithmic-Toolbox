#Uses python3

import sys


def largest_number(a):
    ans = ''
    while a:
        x = '0'
        for i in a:
            if int(x+i) < int(i+x):
                x = i
        ans += x
        a.remove(x)
    return ans


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))