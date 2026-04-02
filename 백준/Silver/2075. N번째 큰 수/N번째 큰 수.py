import heapq
import sys
input = sys.stdin.readline
a = int(input().strip())
cnt = []
for i in range(a):
    for ii in map(int, input().strip().split()):
        heapq.heappush(cnt, ii)
        if len(cnt) > a:
            heapq.heappop(cnt)
cnt.sort()
print(cnt[0])