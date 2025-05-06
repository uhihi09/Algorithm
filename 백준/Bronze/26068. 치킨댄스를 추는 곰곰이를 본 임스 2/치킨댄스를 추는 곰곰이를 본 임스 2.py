a = int(input())
cnt = 0
for i in range(a):
    b,c = input().split("-")
    if int(c) <= 90:
        cnt += 1
print(cnt)