ans = []
a = int(input())
for i in range(a):
    b = int(input())
    if b == 0:
        ans.pop()
    else:
        ans.append(b)
print(sum(ans))