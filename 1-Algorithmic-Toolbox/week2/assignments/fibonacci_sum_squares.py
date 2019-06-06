# Uses python3

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

def fib_sum_squares_fast(n):
    if n <= 1:
        return n
    
    period = int(n % 60)

    curr = 0
    next = 1

    for _ in range(period):
        curr, next = next, (curr + next) % 10

    return (curr * next) % 10



if __name__ == '__main__':
    n = int(input())
    print(fib_sum_squares_fast(n))
