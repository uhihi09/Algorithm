def solve(a):
    cnt = [0] * (a + 1)
    if a == 1:
        return 1
    cnt[0] = 1
    if a == 2:
        return 3
    cnt[1] = 3
    if a == 3:
        return 5
    cnt[2] = 5
    for i in range(3, a + 1):
        cnt[i] = 2 * cnt[i - 2] + cnt[i - 1]
    return cnt[a-1]
a = int(input())
print(solve(a)%10007)