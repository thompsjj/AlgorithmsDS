import sys

def get_change(V):
    denom = [1, 5, 10]
    change_left = V
    min_change = 0
    while change_left:
        left = [c for c in denom if c <= change_left]
        if left:
            change_left -= max(left)
            min_change += 1
        else:
            return min_change
    return min_change

m = int(sys.stdin.read())
print(get_change(m))