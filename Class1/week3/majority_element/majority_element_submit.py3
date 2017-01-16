# Uses python 3
import sys

def frequency(S, x):
    counts = 1
    for s in S:
        if s == x:
            counts+=1    
    return counts
    
def majority(A):
    N = len(A)
    
    if N==1:
        return A[0]
    
    k = N//2
    Al = A[:k]
    Ar = A[k:]
    
    ml = majority(Al)
    mr = majority(Ar)
    
    if ml==mr:
        return ml
    
    countL = frequency(A, ml)
    countR = frequency(A, mr)

    if countL and (countL > k+1):
        return ml
    elif countR and (countR > k+1):
        return mr
    else:
        return None

input = sys.stdin.read()
n, *a = list(map(int, input.split()))
if majority(a) != None:
    print(1)
else:
    print(0)

