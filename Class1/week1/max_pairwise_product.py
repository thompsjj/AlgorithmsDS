# Uses python3
#n = int(input())
#a = [int(x) for x in input().split()]

#a = [int(x) for x in input().split()] # need to use long ints

def max_product_1(a, n):

    assert (len(a) == n)
    result = 0
    h1 = 0 # highest valued integer
    h2 = 0 # 2nd highest valued integer
    h1_i = 0
    h2_i = 0
    for i in range(0, n):
        for j in range(i + 1, n):
            if a[i] * a[j] > result:
                h1 = a[i] # highest valued integer
                h2 = a[j] # 2nd highest valued integer
                h1_i = i
                h2_i = j
                result = a[i] * a[j]

    print("mp1 h1: ", h1, "#", h1_i, "h2:", h2, "#", h2_i)

    return result

def max_product_2(a, n):
    assert (len(a) == n)

    h1 = 0 # highest valued integer
    h2 = 0 # 2nd highest valued integer
    h1_i = 0
    h2_i = 0
    # if you were going to include negative integers, you'd have
    # to keep tabs on the lowest and 2nd lowest

    for i in range(0, n):
        if a[i] >= h1:
            h1 = a[i]
            h1_i = i

    for i in range(0,n):
        if a[i] >= h2:
            if i != h1_i:
                h2 = a[i]
                h2_i = i

    print("mp2 h1: ", h1, "#", h1_i, "h2:", h2, "#", h2_i)

    max_product = h1*h2
    return max_product

#print(result)
