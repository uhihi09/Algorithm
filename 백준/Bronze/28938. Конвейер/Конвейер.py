a = int(input())
b = list(map(int, input().split()))
c = 0
for i in range(a):
    c += b[i]
if c == 0:
    print("Stay")
elif c > 0:
    print("Right")
elif c < 0:
    print("Left")