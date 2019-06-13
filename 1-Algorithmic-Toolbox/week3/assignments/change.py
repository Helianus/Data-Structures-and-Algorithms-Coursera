# Uses python3

def get_change_naive(m):
   count = m // 10
   m %= 10

   count += m // 5
   m %= 5

   count += m // 1
   return count


def get_change_greedy(m):
    #write your code here
    change, count = 0, 0
    coins = [1, 5, 10]
    index = len(coins) - 1

    while change < m:
        while (change <= m and (m - change) >= coins[index]):
            change += coins[index]
            count += 1
        index -= 1
    
    return count

if __name__ == '__main__':
    m = int(input())
    print(get_change_greedy(m))
