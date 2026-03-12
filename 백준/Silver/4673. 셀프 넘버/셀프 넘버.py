cnt = []
for iii in range(10000):
    ans = str(iii)
    cnt2 = int(ans)
    for ii in range(len(ans)):
        cnt2 += int(ans[ii])
    ans = str(cnt2)
    if int(ans) <= 10000:
        cnt.append(int(ans))
cnt = set(cnt)
cnt2 = []
for i in range(1,10001):
    cnt2.append(i)
cnt2 = set(cnt2)
legend = cnt2-cnt
legend = list(legend)
legend.sort()
for i in legend:
    print(i)