a = int(input())
b = input()
cnt1 = 0
cnt2 = 0
for i in b:
    if int(i)%2 == 0 or int(i)==0:
        cnt1 += 1
    else:
        cnt2 += 1
if cnt1 > cnt2:
    print(0)
elif cnt2 > cnt1:
    print(1)
else:
    print(-1)