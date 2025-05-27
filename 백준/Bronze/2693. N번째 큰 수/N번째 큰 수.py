a = int(input())
for i in range(a):
    b = list(map(int,input().split()))
    b.sort()
    b.pop()
    b.pop()
    print(b[-1])