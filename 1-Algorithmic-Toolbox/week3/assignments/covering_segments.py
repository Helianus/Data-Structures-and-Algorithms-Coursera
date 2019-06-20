# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #write your code here
    for s in segments:
        points.append([s.start, s.end])
    
    points.sort(key = lambda x: x[1])

    p = points[0][1]
    ans = [points[0][1]]
    for i in range(len(points)):
        if points[i][0] > p:
            p = points[i][1]
            ans.append(p)
    
    return ans

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
