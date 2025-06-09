a = int(input())
cnt = []
for i in range(a):
    cnt.append(input())
p1 = 0
p2 = 0
for i in range(len(cnt)):
    if p1 - p2 == 2 or p2 - p1 == 2:
        break
    if "D" == cnt[i]:
        p1 += 1
    elif "P" == cnt[i]:
        p2 += 1
print(f"{p1}:{p2}")