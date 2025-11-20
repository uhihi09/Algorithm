def find(cnt):
    if cnt[0] >= 1000:
        return True
    elif cnt[1] >= 1600:
        return True
    elif cnt[2] >= 1500:
        return True
    elif cnt[3] <= 30 and cnt[3] != -1:
        return True
    return False


a = int(input())
ans = 0
for i in range(a):
    b = list(map(int,input().split()))
    c = find(b)
    if c:
        ans+=1
print(ans)