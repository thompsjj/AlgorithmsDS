#Uses python3

import sys

def max_dot_product(a, b):
    #write your code here
    res = 0
    
    a = sorted(a)
    b = sorted(b)
    
    for i, a in enumerate(a):
        res+=a*b[i]
    
    return res

input = sys.stdin.read()
data = list(map(int, input.split()))
n = data[0]
a = data[1:(n + 1)]
b = data[(n + 1):]
print(max_dot_product(a, b))