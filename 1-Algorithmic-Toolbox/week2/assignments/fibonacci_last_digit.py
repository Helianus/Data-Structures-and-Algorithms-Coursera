# Uses python3

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

def get_digit_fast(n):
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(n - 1):
        prev, curr = curr, (prev + curr) % 10
    return curr

if __name__ == '__main__':
    n = int(input())
    print(get_digit_fast(n))
