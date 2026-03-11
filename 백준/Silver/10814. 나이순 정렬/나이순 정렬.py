a = int(input())
cnt = []
idx = 0
for i in range(a):
    b,c = input().split()
    b = int(b)
    cnt.append((b,c,idx))
    idx += 1
cnt.sort(key= lambda x : (x[0],x[2]))
for i in range(len(cnt)):
        print(cnt[i][0],cnt[i][1])