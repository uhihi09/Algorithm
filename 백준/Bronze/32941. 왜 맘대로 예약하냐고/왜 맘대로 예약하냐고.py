a,b = map(int,input().split())
c = int(input())
cnt = False
for i in range(c):
    d = int(input())
    e = list(map(int,input().split()))
    if b in e:
        cnt = True
        continue
    else:
        print("NO")
        break
if cnt:
    print("YES")