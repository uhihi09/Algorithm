import sys
input = sys.stdin.readline

a = int(input())
ans = []
for i in range(a):
    b = list(map(int,input().split()))
    ans.append(b)
for i in range(len(ans)):
    ans[i] = ans[i][::-1]
ans.sort()
for i in range(len(ans)):
    ans[i] = ans[i][::-1]
for i in ans:
    print(*i)