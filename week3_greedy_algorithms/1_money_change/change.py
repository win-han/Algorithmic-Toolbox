# Uses python3
import sys

def get_change(m):
    #write your code here
    a, b = 0, [10, 5, 1]
    j = []
    for i in b:
        while m - i >= 0:
            m -= i
            a += 1
            j.append(m)
    return a

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
