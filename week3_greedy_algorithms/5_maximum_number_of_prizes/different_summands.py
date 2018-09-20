# Uses python3
import sys


def optimal_summands(n):
    summands, i = [], 1

    #write your code here
    while n != 0:
        if n - i > i:
            n -= i
            summands.append(i)
            i += 1
        else:
            summands.append(n)
            break

    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
