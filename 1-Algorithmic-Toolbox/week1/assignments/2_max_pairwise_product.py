# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product

def max_pairwise_product_fast(numbers):
    re1 = max(numbers)
    numbers.remove(re1)
    re2 = max(numbers)
    return (re1 * re2)

from random import randint
def stress_test(N, M):
    while True:
        n = randint(2, N)
        arr = [None]*n
        for i in range(n):
            arr[i] = randint(0, M)
        print(arr)
        re1 = max_pairwise_product(arr)
        re2 = max_pairwise_product_fast(arr)
        if re1 == re2:
            print("OK")
        else:
            print("Wrong answer:", re1, re2)
            return

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_fast(input_numbers))
