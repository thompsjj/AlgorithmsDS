def get_fibonacci_last_digit(n):
    previous = 0
    current = 1
    for i in range(n-1):
        previous, current = current%10, (previous+current)%10
    return current

n = int(input())
print(get_fibonacci_last_digit(n))