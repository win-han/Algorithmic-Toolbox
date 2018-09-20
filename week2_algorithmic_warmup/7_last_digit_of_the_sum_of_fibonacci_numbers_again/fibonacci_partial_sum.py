# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10

def fib_fast(n, m):

    a = [0, 1]
    while True:
        a.append((a[-1]+a[-2]) % m)
        if a[-1] == 1 and a[-2] == 0:
            a.pop()
            a.pop()
            break

    return a[n % len(a)]


def fib_fix(n, m):
    a = fib_fast(m + 2, 10) - fib_fast(n + 1, 10)
    return a if a >= 0 else 10 + a


if __name__ == '__main__':
    input = sys.stdin.read()
    from_, to = map(int, input.split())
    print(fib_fix(from_, to))