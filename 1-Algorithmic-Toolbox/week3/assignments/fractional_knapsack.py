# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here

    for _ in range(len(values)):
        if capacity <= 0:
            return value

        max_value = 0
        max_per_unit = values[0] / weights[0]
        for i in range(len(values)):
            if weights[i] > 0 and values[i] > 0:
                unit = values[i] / weights[i]
                if unit > max_per_unit:
                    max_per_unit, max_value = unit, i

        a = min(capacity, weights[max_value])
        value += (a * values[max_value]) / weights[max_value]
        weights[max_value] -= a
        capacity -= a
    
    return value



if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
