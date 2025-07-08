a = list(map(int, input().split()))
cnt = a.copy()
cnt.remove(max(cnt))
cnt.remove(min(cnt))
if max(a) == min(a) or max(a) == cnt[0] or min(a) == cnt[0]:
    print("S")
elif max(a) == min(a)+cnt[0]:
    print("S")
else:
    print("N")