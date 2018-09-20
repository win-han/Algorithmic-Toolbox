# Uses python3
import sys
import random

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def gcd(a, b):
    while a != 0 and b != 0:
        c, d = a, b
        a, b = a % b, b % a
    return (d if d < c else c)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))
