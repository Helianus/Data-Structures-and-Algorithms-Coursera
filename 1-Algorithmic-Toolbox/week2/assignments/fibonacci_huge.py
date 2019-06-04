# Uses python3

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def get_huge_fast(n, m):
    prev = 0
    curr = 1
    lst = [prev, curr]

    for _ in range(n):
        prev, curr = curr, (prev + curr) % m
        if prev == 0 and curr == 1:
            lst.pop()
            break
        else:
            lst.append(curr)
    return lst[n % len(lst)]

if __name__ == '__main__':
    n, m = map(int, input().split())
    print((get_huge_fast(n, m)))
