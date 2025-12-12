a = int(input())
cnt = 0
if a == 0:
    print(0)
elif a == 1:
    print(1)
else:
    for i in range(1,a+1):
        cnt += i
        if cnt > a:
            print(i-1)
            break