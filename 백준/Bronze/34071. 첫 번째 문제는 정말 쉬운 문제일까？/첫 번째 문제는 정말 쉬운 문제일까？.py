a = int(input())
cnt = []
for i in range(a):
    cnt.append(int(input()))
if cnt[0] == min(cnt):
    print("ez")
elif cnt[0] == max(cnt):
    print("hard")
else:
    print("?")