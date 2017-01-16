# Uses python3

def fib(n):
    F = {}
    def _fib(n, F):
        if n in F:
            return F[n]
        elif n <= 1:
            return n
        else:
            F[n] = _fib(n-1, F)+_fib(n-2, F)
            return F[n]
    return _fib(n,F)

n = int(input())
print(fib(n))
