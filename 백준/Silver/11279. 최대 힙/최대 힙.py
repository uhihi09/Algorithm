import heapq
import sys
input = sys.stdin.readline
n = int(input())
cnt = []
for i in range(n):
    x = int(input())
    if x > 0:
        heapq.heappush(cnt,-x)
    elif len(cnt) == 0:
        print(0)
    elif x == 0:
        print(abs(heapq.heappop(cnt)))