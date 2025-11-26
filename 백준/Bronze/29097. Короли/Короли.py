a1,b1,c1,a2,b2,c2 = map(int,input().split())
cnt = {
    "Joffrey": a1 * a2,
    "Robb":    b1 * b2,
    "Stannis": c1 * c2
}
big = max(cnt.values())
cnt1 = []
for i in cnt:
    if cnt[i] == big:
        cnt1.append(i)
cnt1.sort()
print(" ".join(cnt1))