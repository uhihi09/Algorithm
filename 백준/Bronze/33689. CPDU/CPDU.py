a = int(input())
cnt = 0
for i in range(a):
    b = input()
    if b[0] == "C":
        cnt += 1
print(cnt)