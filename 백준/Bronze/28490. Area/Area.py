a = int(input())
cnt = []
for i in range(a):
    b,c = map(int,input().split())
    cnt.append(b*c)
print(max(cnt))