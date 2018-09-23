# Uses python3
import sys


def get_change(m):
    sol = [[1], [1, 2], [1, 3], [1, 3, 4]]

    for i in range(5, m + 1):
        sollist = [sol[-1]+[i]]
        if i % 3 == 0:
            sollist.append(sol[(i // 3) - 1] + [i])
        if i % 2 == 0:
            sollist.append(sol[(i // 2) - 1] + [i])
        sol.append(min(sollist, key=len))

    return sol[-1]


input = sys.stdin.read()
n = int(input)
sequence = get_change(n)
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
