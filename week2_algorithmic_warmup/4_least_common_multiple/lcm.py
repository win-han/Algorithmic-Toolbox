# Uses python3
import sys
import random

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def gcd(a, b):
    while a != 0 and b != 0:
        c, d = a, b
        a, b = a % b, b % a
    return (d if d < c else c)

def lcm(a, b):
    c = gcd(a,b)
    return (a//c)*b

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

