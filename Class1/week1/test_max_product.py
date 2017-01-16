from max_pairwise_product import *
import random




for n in range(0, 100):
    # generate a long list of numbers and determine max product
    k = random.randrange(0, 10000)
    a = random.sample(range(2*10**5), k)
    n = int(len(a))

    print("testing %s" % n)

    if max_product_1(a, n) != max_product_2(a, n):
        print("failed case: ", k, n)
