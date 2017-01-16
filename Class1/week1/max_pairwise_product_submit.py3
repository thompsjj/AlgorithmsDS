n = int(input())
a = [int(x) for x in input().split()]

def max_product_2(a, n):
    assert (len(a) == n)

    h1 = 0 # highest valued integer
    h2 = 0 # 2nd highest valued integer
    h1_i = 0
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

    max_product = h1*h2
    return max_product

print(max_product_2(a, n))