# Uses python3

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm_fast(a, b):
    return (a * b) // gcd(a, b)

from random import randint
def stress_test():
    while True:
        n = 226553150
        m = 1023473145
        print("The n is " + str(n) + ", m is " + str(m))
        re1 = lcm_naive(n, m)
        re2 = lcm_fast(n, m)
        if re1 == re2:
            print("OK")
        else:
            print("Wrong answer:", re1, re2)
            return

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm_fast(a, b))