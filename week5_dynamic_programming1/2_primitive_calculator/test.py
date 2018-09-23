from operator import itemgetter


def get_change(m):
    sol = [[1], [1, 2], [1, 3], [1, 2, 4]]
    for i in range(5, m + 1):
        if i % 2 == 0:
            sol.append(sol[(i - 1) // 2] + [i])
        elif i % 3 == 0:
            sol.append(sol[(i - 1) // 3] + [i])
        else:
            sol.append(sol[-1] + [i])

    return sol[-1]


def get_change2(m):
    sol = [[1], [1, 2], [1, 3], [1, 2, 4]]
    for i in range(5, m + 1):
        if i % 3 == 0:
            sol.append(sol[(i - 1) // 3] + [i])
        elif i % 2 == 0:
            sol.append(sol[(i - 1) // 2] + [i])
        else:
            sol.append(sol[-1] + [i])

    return sol[-1]

print(get_change(3072))
print(get_change2(3072))