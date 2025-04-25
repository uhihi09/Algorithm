y1,m1,d1 = map(int, input().split())
y2,m2,d2, = map(int, input().split())
man = 0
yean = y2-y1
sae = yean+1
if (m2 < m1) or (m2 == m1 and d2 < d1):
    man = yean - 1
else:
    man = yean
print(man)
print(sae)
print(yean)