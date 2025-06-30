import sys
input = sys.stdin.readline
import heapq

n = int(input())
n_list = []
for _ in range(n):
    t = int(input())
    if t == 0:
        if len(n_list) == 0:
            print(0)
        else:
            p = heapq.heappop(n_list)
            print(p)
    else:
        heapq.heappush(n_list, t)