a = int(input())
ans = []
for i in range(a):
    b,c = map(int,input().split())
    ans.append(b+c)
print(min(ans))