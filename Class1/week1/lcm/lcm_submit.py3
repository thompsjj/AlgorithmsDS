def lcm(a, b):
    def _gcd(a, b):
        if b > a:
            (a, b) = (b, a)

        if b == 0:
            return a
        else:
            return _gcd(b, a%b)
            
    return int((a*b)//_gcd(a,b))

a, b = map(int, input().split())
print(lcm(a, b))