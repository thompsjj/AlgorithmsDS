def fibonacci_partial_sum(m,n):
    
    assert m<=n
    
    def fib(n):
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
            
    #using (fib((n+2)%_pisano_period(10))-1)%10
    
    return (fib((n+2)%_pisano_period(10))-fib((m+1)%_pisano_period(10)))%10

from_, to = map(int, input().split())
print(fibonacci_partial_sum(from_, to))