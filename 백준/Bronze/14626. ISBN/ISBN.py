a = list(input())
cnt = 0
for i in range(len(a)):
    if a[i] == "*":
        continue
    elif i % 2 == 0:
        cnt += int(a[i])
    else:
        cnt += int(a[i]) * 3
if cnt % 10 == 0:
    print(0)
elif a.index("*") % 2 == 0:
    print(10 - cnt % 10)
else:
    for i in range(10):
        if (cnt + 3 * i) % 10 == 0:
            print(i)
            break