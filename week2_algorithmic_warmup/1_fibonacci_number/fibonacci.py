# Uses python3
def calc_fib_slow(n):
    if (n <= 1):
        return n

    return calc_fib_slow(n - 1) + calc_fib_slow(n - 2)


def fib_fast(n):
    a = [0, 1]
    if n == 0 or n == 1:
        return a[n]
    for i in range(n-1):
        a.append((a[-1]+a[-2]))
    return a[-1]

n = int(input())
print(fib_fast(n))
