a = int(input())
cnt = ""
if a % 8 == 0:
    cnt += "h"
elif a % 8 == 1:
    cnt += "a"
elif a % 8 == 2:
    cnt += "b"
elif a % 8 == 3:
    cnt += "c"
elif a % 8 == 4:
    cnt += "d"
elif a % 8 == 5:
    cnt += "e"
elif a % 8 == 6:
    cnt += "f"
elif a % 8 == 7:
    cnt += "g"
if a % 8 == 0:
    cnt += str(a//8)
else:
    cnt += str(a//8+1)
print(cnt)