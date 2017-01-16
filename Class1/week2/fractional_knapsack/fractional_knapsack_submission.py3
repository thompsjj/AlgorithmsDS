# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    remaining_capacity = capacity
    # index the values by weight
    assert len(weights) == len(values)
    
    index = range(len(weights))

    ratios = zip(index, [float(v)/float(weights[i]) for i, v in enumerate(values)])

    indexOrdered = [i[0] for i in sorted(ratios, key=lambda x: x[1], reverse=True)]
   
    # while there is capacity remaining
    for i in indexOrdered:
        if remaining_capacity:
            # take as much of the most profitable item you can.
            if weights[i] < remaining_capacity:
                # if weight < capacity
                    # take all
                    # add value to the value
                value += values[i]
                remaining_capacity -= weights[i]
            else:
                value += (remaining_capacity/float(weights[i]))*values[i]
                # add capacity/weight*value to the value
                remaining_capacity = 0
                

    return value


data = list(map(int, sys.stdin.read().split()))
n, capacity = data[0:2]
values = data[2:(2 * n + 2):2]
weights = data[3:(2 * n + 2):2]
opt_value = get_optimal_value(capacity, weights, values)
print("{:.10f}".format(opt_value))