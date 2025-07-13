a = int(input())
cnt = []
for i in range(2,10):
    for ii in range(1,10):
        cnt.append(i*ii)
        cnt.append(i)
        cnt.append(ii)
if a in cnt:
    print(1)
else:
    print(0)