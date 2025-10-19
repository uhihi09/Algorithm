while True:
    a = int(input())
    if a == 0:
        break
    cnt = []
    for i in range(a):
        cnt.append(int(input()))
    for i in range(len(cnt)-1,-1,-1):
        print(cnt[i])
    print(0)