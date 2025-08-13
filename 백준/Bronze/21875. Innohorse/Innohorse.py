a = list(input())
ans1 = ord(a[0])
ans2 = int(a[1])
b = list(input())
ans3 = ord(b[0])
ans4 = int(b[1])
cnt1 = 0
cnt2 = 0
if ans1 - ans3 < 0:
    cnt1 += (ans1 - ans3)*-1
else:
    cnt1 += (ans1 - ans3)
if ans2 - ans4 < 0:
    cnt2 += (ans2 - ans4)*-1
else:
    cnt2 += (ans2 - ans4)
if cnt1 > cnt2:
    print(cnt2,cnt1)
else:
    print(cnt1,cnt2)