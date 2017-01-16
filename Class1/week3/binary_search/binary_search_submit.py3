# Uses python 3
import sys


def binary_search(T, A):
    N = len(A)
    # set a floor
    floor = 0
    # set a ceiling
    ceil = N-1

    def _recurse(T, A, floor, ceil):
        
        # set the median
        mid = (ceil+floor)//2
        
        if (floor > ceil):
            return -1       
        
        if T < A[mid]:
            ceil = mid-1
            return _recurse(T, A, floor, ceil)
        elif T > A[mid]:
            floor = mid+1
            return _recurse(T, A, floor, ceil)
        elif T == A[mid]:
            return mid
        else:
            return "undefined search failure"
        
    return _recurse(T, A, floor, ceil)


input = sys.stdin.read()
data = list(map(int, input.split()))
n = data[0]
m = data[n + 1]
a = data[1 : n + 1]
for x in data[n + 2:]:
    # replace with the call to binary_search when implemented
    print(binary_search(x, a), end = ' ')