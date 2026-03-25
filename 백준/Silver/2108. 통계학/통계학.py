import sys
input = sys.stdin.readline
def solve(array):
    cnt_dct = {}

    for j in array:
        if j in cnt_dct:
            cnt_dct[j] += 1
        else:
            cnt_dct[j] = 1

    cnt_max = max(cnt_dct.values())

    cnt_freq = [key for key, value in cnt_dct.items() if cnt_max == value]

    if len(cnt_freq) == 1:
        return cnt_freq[0]
    else:
        cnt_freq.sort()
        return cnt_freq[1]
a = int(input())
cnt = []
ans1, ans2, ans3, ans4 = 0, 0, 0, 0
for i in range(a):
    var = int(input())
    cnt.append(var)
    ans1 += var
cnt.sort()
ans1 = round(ans1 / a)
ans4 = cnt[-1] - cnt[0]
ans2 = cnt[a//2]
ans3 = solve(cnt)
print(ans1)
print(ans2)
print(ans3)
print(ans4)