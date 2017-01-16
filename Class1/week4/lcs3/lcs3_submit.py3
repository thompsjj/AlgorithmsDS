import numpy as np
import sys

def lcs3(a,b,c):
    I = len(a)
    J = len(b)
    K = len(c)
    
    D = np.zeros((I+1, J+1, K+1))
    
    for i in range(1, I+1):
        for j in range(1, J+1):
            for k in range(1, K+1):
                if a[i-1] == b[j-1] == c[k-1]:
                    D[i,j,k] = D[i-1, j-1, k-1] + 1
                else:
                    D[i,j,k] = max(D[i-1, j, k], D[i, j-1, k], D[i, j, k-1])
    
    return int(D[I, J, K])

input = sys.stdin.read()
data = list(map(int, input.split()))
an = data[0]
data = data[1:]
a = data[:an]
data = data[an:]
bn = data[0]
data = data[1:]
b = data[:bn]
data = data[bn:]
cn = data[0]
data = data[1:]
c = data[:cn]
print(lcs3(a, b, c))