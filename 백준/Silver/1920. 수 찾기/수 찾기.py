a = int(input())
b = list(map(int,input().split()))
c = int(input())
d = list(map(int,input().split()))
b = set(b)
for i in d:
    if i in b:
        print(1)
    else:
        print(0)