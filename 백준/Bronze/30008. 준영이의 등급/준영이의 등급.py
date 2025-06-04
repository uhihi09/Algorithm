def per(cnt):
    return (cnt*100)//a
def love(ans):
    if 0 <= per(ans) <= 4:
        return 1
    elif 4 < per(ans) <= 11:
        return 2
    elif 11 < per(ans) <= 23:
        return 3
    elif 23 < per(ans) <= 40:
        return 4
    elif 40 < per(ans) <= 60:
        return 5
    elif 60 < per(ans) <= 77:
        return 6
    elif 77 < per(ans) <= 89:
        return 7
    elif 89 < per(ans) <= 96:
        return 8
    elif 96 < per(ans) <= 100:
        return 9
a,b = map(int,input().split())
c = list(map(int,input().split()))
for i in c:
    print(love(i),end=" ")