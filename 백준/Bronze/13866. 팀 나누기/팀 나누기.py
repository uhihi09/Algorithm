a = list(map(int,input().split()))
t1 = max(a)+min(a)
t2 = sum(a)-t1
ans1 = t1-t2
ans2 = t2-t1
if ans1 < 0:
    print(ans2)
else:
    print(ans1)