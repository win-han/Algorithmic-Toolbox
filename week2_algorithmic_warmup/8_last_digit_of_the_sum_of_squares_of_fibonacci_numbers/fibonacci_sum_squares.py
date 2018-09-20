# Uses python3
from sys import stdin


def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10


def fib_fast(n, m):
    if n <= 1:
        return n
    a = [0, 1]
    while True:
        a.append((a[-1]+a[-2]) % m)
        if a[-1] == 1 and a[-2] == 0:
            a.pop()
            a.pop()
            break
    return a[n % len(a)]


if __name__ == '__main__':
    n = int(stdin.read())
    print(fib_fast(n+1,10)*fib_fast(n,10) % 10)

