import sys
input = sys.stdin.readline
n,m = list(map(int,input().strip().split()))
cnt = list(map(int,input().strip().split()))
new_cnt = []
cnt_sum = []
var = 0
cnt_sum.append(0)
for i in cnt:
    new_cnt.append(i)
    var += i
    cnt_sum.append(var)
for i in range(m):
    a,b = map(int,input().strip().split())
    print(cnt_sum[b]-cnt_sum[a-1])