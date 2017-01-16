import sys
import random

def partition3(a, l, r):
    
    if r-l <= 1:
        if a[r] < a[l]:
            a[l], a[r] = a[r], a[l]
        i = l
        j = r
        return i, j
        
    m = l
    pivot = a[r]

    while m <= r:
        if a[m] < pivot:
            a[l], a[m] = a[m], a[l]
            l += 1
            m += 1
        elif a[m]==pivot:
            m += 1
        elif a[m]>pivot:
            a[m], a[r] = a[r], a[m]
            r -= 1
    
    i = l
    j = m
    
    return i-1, j

def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    floor, mid = partition3(a, l, r)
    randomized_quick_sort(a, l, floor );
    randomized_quick_sort(a, mid , r);
 
input = sys.stdin.read()
n, *a = list(map(int, input.split()))
randomized_quick_sort(a, 0, n - 1)
for x in a:
    print(x, end=' ')