#Uses python3

import sys


def largest_number(a):
    #write your code here
    res = ""
    
    while len(a) > 0:
        n = '0'
        for i in a:
            if int(n+i) < int(i+n):
                n = i
        res += n
        a.remove(n)
    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
