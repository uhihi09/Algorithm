a = int(input())
cnt = 0
for i in range(3):
    b = list(map(int, input().split()))
    if 7 in b:
        cnt += 1
if cnt == 3:
    print(777)
else:
    print(0)