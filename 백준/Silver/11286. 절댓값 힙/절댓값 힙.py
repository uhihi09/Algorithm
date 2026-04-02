import heapq
import sys
input = sys.stdin.readline
a = int(input().strip())
ans = []
for i in range(a):
    n = int(input().strip())
    if n != 0:
        heapq.heappush(ans,(abs(n),n))
    elif len(ans) == 0:
        print(0)
    elif n == 0:
        print(min(heapq.heappop(ans)))