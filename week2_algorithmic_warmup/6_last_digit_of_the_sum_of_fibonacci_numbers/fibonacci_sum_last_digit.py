# Uses python3
import sys


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current % 10, (previous + current) % 10
        sum = (sum + current) % 10

    return sum


def fib_fast(n, m):
    if n == 0:
        return 0
    n = n + 2
    a = [0, 1]
    while True:
        a.append((a[-1]+a[-2]) % m)
        if a[-1] == 1 and a[-2] == 0:
            a.pop()
            a.pop()
            break

    z = a[n % len(a)] - 1
    return z if z != -1 else 9


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fib_fast(n, 10))
