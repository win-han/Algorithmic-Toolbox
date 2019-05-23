# Uses python3
import sys


def lcm(c, d):
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    return c * d // gcd(c, d)


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))
