
import numpy as np
import sys

def edit_distance(s, t):
    nS = len(s)
    nT = len(t)
    D = np.zeros((nS+1, nT+1))
    
    for i in range(1, nS+1):
        D[i, 0] = D[i-1, 0]+1
        
        for j in range(1, nT+1):
            D[0,j] = D[0,j-1]+1
            
            if s[i-1] != t[j-1]:
                D[i,j] = min(D[i, j-1]+1, D[i-1,j]+1, D[i-1,j-1]+1)
            else:
                D[i,j] = D[i-1,j-1]
            
            
    
    return(int(D[nS, nT]))


print(edit_distance(input(), input()))