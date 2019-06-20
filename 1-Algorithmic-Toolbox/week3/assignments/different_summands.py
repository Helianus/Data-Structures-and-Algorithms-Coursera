# Uses python3
import sys

def optimal_summands(n):
    summands = []
    #write your code here
    inx = 1
    while n > 0:
        if n - inx > inx:
            n -= inx
            summands.append(inx)
            inx += 1
        else:
            summands.append(n)
            break
    return summands

if __name__ == '__main__':
    #input = sys.stdin.read()
    #n = int(input)
    summands = optimal_summands(8)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
