t1 = []
t2 = []
cnt1 = 0
cnt2 = 0
for i in range(10):
    a = int(input())
    t1.append(a)
for i in range(10):
    a = int(input())
    t2.append(a)
for i in range(3):
    b = max(t1)
    cnt1 += b
    t1.remove(b)
for i in range(3):
    b = max(t2)
    cnt2 += b
    t2.remove(b)
print(cnt1,cnt2)