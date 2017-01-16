# Uses python 3

import numpy as np
import sys
def optimal_weight(W, weights):
    w = len(weights)    
    S = np.zeros((w+1, W+1))

    for i in range(w):
        for j in range(W+1):
            if weights[i] > j:
                S[i,j] = S[i-1,j]
            else:
                S[i,j] = max(S[i-1,j], weights[i]+S[i-1,j-weights[i]])
    return(int(S[w-1,W]))

input = sys.stdin.read()
W, n, *w = list(map(int, input.split()))
print(optimal_weight(W, w))