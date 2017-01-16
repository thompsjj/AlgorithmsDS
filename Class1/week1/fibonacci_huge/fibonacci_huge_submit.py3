# Uses python 3
def get_fibonacci_huge(n, m):
    
    def fib(n):
        if n<=1:
            return n
        
        before = 0
        current = 1
        for i in range(n-1):
            before, current = current, current+before
        return current
    
    def _pisano_period(m):
        a=0
        b=1
        c=a+b
        for i in range(m*m):
            c = (a+b)%m
            a = b
            b = c

            if (a==0) & (b==1):
                return i+1
        
    return fib(n%_pisano_period(m))%m

n, m = map(int, input().split())
print(get_fibonacci_huge(n, m))