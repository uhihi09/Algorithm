a = list(input())
for i in range(len(a)):
    if a[i] == '0':
        a.pop(i)
    else:
        break
for i in range(len(a)-1,-1,-1):
    if a[i] == '0':
        a.pop(i)
    else:
        break
print(a.count('0'))