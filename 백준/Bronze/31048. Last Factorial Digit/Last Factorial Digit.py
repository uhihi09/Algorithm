def pac(a):
    cnt = 1
    for i in range(1,a+1):
        cnt *= i
    return cnt
a = int(input())
for i in range(a):
    b = int(input())
    print(str(pac(b))[-1])