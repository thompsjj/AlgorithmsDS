import sys

def optimal_summands(n):
    summands = []
    k = n
    l = 1
    while k:
        #print summands
        if k<=2*l:
            summands.append(k)
            break
        else:
            summands.append(l)
            k = k-l
            l+=1
    return summands

input = sys.stdin.read()
n = int(input)
summands = optimal_summands(n)
print(len(summands))
for x in summands:
    print(x, end=' ')