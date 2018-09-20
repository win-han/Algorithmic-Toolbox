# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0
    # write your code here
    v_per_w = [values[i]/weights[i] for i in range(len(weights))]

    while v_per_w and capacity != 0:
        a, j = 0, None
        for i in v_per_w:
            if i > a:
                a = i
        j = v_per_w.index(a)
        if capacity - weights[j] > 0:
            capacity -= weights[j]
            value += values[j]
            values.pop(j)
            weights.pop(j)
            v_per_w.pop(j)
        else:
            value += capacity * v_per_w[j]
            break

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))

    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
