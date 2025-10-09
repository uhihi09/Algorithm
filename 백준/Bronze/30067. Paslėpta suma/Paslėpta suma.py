a = []
for i in range(10):
    a.append(int(input()))
cnt = sum(a)
for i in a:
    if cnt - i == i:
        print(i)
        break