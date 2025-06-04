human = list(map(int,input().split()))
coordinate = list(map(int,input().split()))
cnt = 0
for i in human:
    if i == coordinate[0]:
        cnt = i
if cnt == 0:
    print(cnt)
else:
    print(human.index(cnt)+1)