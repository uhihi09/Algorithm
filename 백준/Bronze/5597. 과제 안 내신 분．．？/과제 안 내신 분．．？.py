import sys
input = sys.stdin.readline
cnt = []
ans = []
legend = []
for i in range(1,31):
    ans.append(i)
for i in range(28):
    cnt.append(int(input()))
for i in ans:
    if i not in cnt:
        legend.append(i)
for i in legend:
    print(i)