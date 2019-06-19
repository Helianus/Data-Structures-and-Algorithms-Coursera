# python3
import sys

def compute_min_refills(distance, tank, stops):
    # write your code here

    if distance <= tank:
        return 0
    else:

        stops.append(distance)
        n_stops = len(stops) - 1
        count = 0
        refill = tank

        for i in range(n_stops):
            if refill < stops[i] or (stops[-2] + tank < distance):
                return -1
            if refill < stops[i + 1]:
                refill = tank + stops[i]
                count += 1 

    return count

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
