a = int(input())
b = int(input())
cnt = a * 10
if a >= 3:
    cnt += 20
if a == 5:
    cnt += 50
if b > 1000:
    cnt -= 15
print(max(cnt, 0))