import sys
cnt = ""
cnt2 = 0
while True:
    try:
        cnt += input()
    except:
        break
cnt=cnt.split(",")
for i in cnt:
    cnt2 += int(i)
print(cnt2)