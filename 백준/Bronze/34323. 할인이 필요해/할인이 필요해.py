N, M, S = map(int, input().split())
cnt1 = S * (M + 1) * (100 - N) // 100
cnt2 = S * M
print(min(cnt1, cnt2))