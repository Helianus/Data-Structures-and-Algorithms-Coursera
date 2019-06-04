# Uses python3

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

def fib_sum_fast(n):
    if n <= 1:
        return n
    
    prev = 0
    curr = 1

    period = int(n % 60)

    for _ in range(period + 1):
        prev, curr = curr, (prev + curr) % 10
    sum = curr - 1
    return sum if sum != -1 else 9

from random import randint
def stress_test():
    while True:
        n = randint(2, 1000)
        print("The n is " + str(n))
        re1 = fibonacci_sum_naive(n)
        re2 = fib_sum_fast(n)
        if re1 == re2:
            print("OK")
        else:
            print("Wrong answer:", re1, re2)
            return



if __name__ == '__main__':
    n = int(input())
    print(fib_sum_fast(n))
