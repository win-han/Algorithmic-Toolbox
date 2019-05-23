# Uses python3
import sys
import random


def get_optimal_value(capacity, weights, values):
    a = sorted(zip(values, weights),  key=lambda x: x[0]/x[1])
    value = 0
    for v, w in a[::-1]:
        if capacity - float(w) >= 0:
            capacity -= float(w)
            value += float(v)
        else:
            value += capacity * (v/w)
            break
    return value


def get_optimal(capacity, weights, values):
    value = 0.
    proportion = [float(v) / float(w) for v, w in zip(values, weights)]
    for _ in range(len(weights) + 1):
        if capacity == 0:
            break
        max_weight = max(proportion)
        index = proportion.index(max_weight)
        proportion[index] = -1
        add_capacity = min(capacity, weights[index])
        value += add_capacity * max_weight
        weights[index] -= add_capacity
        capacity -= add_capacity
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
