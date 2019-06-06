# Uses python3

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10


def fib_partial_sum_fast(from_, to):

    m = int(from_ % 60)
    n = int(to % 60)

    if n < m:
        n += 60
    
    curr = 0
    next = 1
    sum = 0
    for i in range(n+1):
        if i >= m:
            sum += curr
        curr, next = next, curr + next
    return int(sum % 10)


if __name__ == '__main__':
    from_, to = map(int, input().split())
    print(fib_partial_sum_fast(from_, to))