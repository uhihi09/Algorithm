a,b = map(int,input().split())
cnt1 = 1
cnt2 = 1
for i in range(b):
    cnt1 *= a
    a -= 1
for i in range(b):
    cnt2 *= b
    b -= 1
print(cnt1//cnt2)