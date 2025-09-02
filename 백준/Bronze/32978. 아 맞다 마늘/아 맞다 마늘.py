a = int(input())
b = list(input().split())
c = list(input().split())
for i in b:
    if i not in c:
        print(i)