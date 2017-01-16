# uses python 3
import sys

def merge_sort(A,count):
    
    def merge(A, B, count):
    
        L = len(A)
        R = len(B)
        result = [0]*(L+R)
        i = j = k = 0
        while i<L and j<R:
            if A[i] <= B[j]:
                result[k] = A[i]
                i += 1
                k += 1
            else:
                result[k] = B[j]
                j += 1
                k += 1
                count[0] += (L-i)

        if i != L:
            while i<L:
                result[k] = A[i]
                i += 1
                k += 1

        if j != R:
            while j<R:
                result[k] = B[j]
                j += 1
                k += 1            


        return result 
    
    N = len(A)
    if N <= 1:
        return A
    
    left = merge_sort(A[:N//2],count)
    right = merge_sort(A[N//2:],count)
    
    return merge(left, right, count)


input = sys.stdin.read()
n, *a = list(map(int, input.split()))
count = [0]
merge_sort(a, count)
print(count[0])