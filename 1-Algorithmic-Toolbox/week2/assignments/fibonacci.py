# Uses python3

# Naive
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def fib_list(n):
    if n <= 1:
        return n
    else:
        F = [None]*(n+1)
        F[0] = 0
        F[1] = 1
        for i in range(2, n+1):
            F[i] = F[i - 1] + F[i - 2]
    return F[n]

n = int(input())
print(fib_list(n))
